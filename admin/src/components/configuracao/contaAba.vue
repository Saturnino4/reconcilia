<template>
  <section class='main-contents'>
    <form class="form1 rounded" @submit.prevent>
      <p style="opacity: .8;" class="bold">Conta</p>
      <hr>
      <span class="flex gap s-between">
        <span class="flex gap-1">
          <label for="tipo_nostro">Nostro</label>
          <input type="radio" name="tipo" id="tipo_nostro" :value="true" v-model="isNostro">
        </span>
        <span class="flex gap-1">
          <label for="tipo_vostro">Vostro</label>
          <input type="radio" name="tipo" id="tipo_vostro" :value="false" v-model="isNostro">
        </span>
      </span>
      <span class="flex s-between a-center" style="width: 100%;">
        <label for="conta-select">Já tem conta?</label>
        <select style="width:60%" name="conta" id="conta-select" v-model="selectedContaId">
          <option :value="0">---- Selecione conta ----</option>
          <option v-for="conta in contasData" :key="conta.id" :value="conta.id">{{ conta?.numero }}</option>
        </select>
      </span>            
      <input :disabled="selectedContaId != 0" type="text" placeholder="numero" v-model="data.numero">
      <select :disabled="selectedContaId != 0" name="banco" id="banco" v-model="data.banco_id" >
        <option value="0">-------- Selecione banco -----------</option>
        <option v-for="banco in bancosData" :key="banco.id" :value="banco.id">{{ banco?.nome }}</option>
      </select>
      <select :disabled="selectedContaId != 0" name="moeda" id="moeda" v-model="data.moeda_id" >
        <option value="0">-------- Selecione moeda -----------</option>
        <option v-for="moeda in moedasData" :key="moeda.id" :value="moeda.id">{{ moeda?.abreviatura }}</option>
      </select>
      <textarea :disabled="selectedContaId != 0" v-model="data.descricao" name="descricao" id="descricao" placeholder="descrição..."></textarea>
      <input  v-if="isNostro" type="text" placeholder="Nome da conta contabilista.." v-model="data.subconta_nome">
      <span class="flex gap s-between">
        <button v-if="!isFormEMpty" @click="clearForm" style="background-color: #222;">Limpar</button>
        <button @click="submitForm">{{ action }}</button>
      </span>
    </form>
    <section class="table_section">
      <CustomTable :tableData="contasData" @returnData="returnData" />
    </section>
  </section>
</template>
  
<script>
  import CustomTable from '@/components/table.vue';
  import { DBrequestsObj as req } from '@/db/requests';
  
  export default { 
    components: {   
      CustomTable,
    }, 
    
    props: {   
      // Suas props aqui, se houver
    }, 
    
    data(){
      return { 
        isNostro: true,
        isFormEMpty: true,
        current_aba: 'conta',
        
        // Separar o ID da conta selecionada
        selectedContaId: 0,

        // Objeto completo da conta selecionada
        selectedConta: {
          id: 0,
          numero: '',
          subconta_nome: '',
          banco_id: 0,
          moeda_id: 0,
          descricao: '',
        },
        
        data: {
          numero: '',
          subconta_nome: '',
          banco_id: 0,
          moeda_id: 0,
          descricao: '',
        },

        action: 'registrar',
        contasData: [],
        customContaData: [],
        bancosData: [],
        moedasData: [],
        
        fakeContas: [
          {numero: 'Dólar', banco_id: '$', descricao: 'USD', status: 'ativo'},
          {numero: 'Euro', banco_id: '€', descricao: 'EUR', status: 'ativo'},
          {numero: 'Libra', banco_id: '£', descricao: 'GBP', status: 'ativo'},
          {numero: 'Franco', banco_id: '₣', descricao: 'CHF', status: 'ativo'},
        ],

        propsData: {
          data: this.fakeContas,
          columns: ['numero', 'Local', 'descricao'],
        },

        errorMessage: '',
      } 
    }, 
    
    methods: {  
      returnData(data){
        console.log(data);
        this.data = data;
        this.action = 'editar';
        // this.data.banco_id = data.Local;
      },

      checkEmptyFields(){
        console.log("Checking empty fields..............................");
        
        // Corrigir a lógica de verificação
        if (this.data.numero !== '' && this.data.banco_id !== 0 && this.data.moeda_id !== 0 && this.data.descricao !== '') {
          this.isFormEMpty = false;
        } else {
          this.isFormEMpty = true;
        }
      },

      async submitForm(){
        if(this.action === 'registrar'){
          this.registerData();
        } else {
          this.editData();
        }
      },

      clearForm(){
        this.data = {
          numero: '',
          subconta_nome: '',
          banco_id: 0,
          moeda_id: 0,
          descricao: '',
        }
        this.selectedContaId = 0; // Resetar o ID selecionado
        this.action = 'registrar';
      },

      async setContasData(){
        try {
          let contas = await req.fetch('conta/');
          console.log("contas do Fetch: ", contas);
          
          this.contasData = contas.data;
          this.customContaData = contas.data;

        } catch (error) {
          console.log("Erro ao buscar contas: ", error);

          this.$swal.fire({
            position: 'bottom-end',
            icon: 'error',
            title: 'Erro ao listar contas!',
            showConfirmButton: false,
            timer: 2000,
            toast: true
          })
        }
      },

      async getBancos(){
        try {
          let bancos = await req.fetch(`banco/?nostro=${this.isNostro ? 1 : 0}`);
          console.log("Bancos do Fetch: ", bancos);
          this.bancosData = bancos.data;
        } catch (error) {
          console.log("Erro ao buscar bancos: ", error);
          this.bancosData = [];
        }
      },

      async setSelectedConta(contaId){
        try {
          let conta = await req.fetch(`conta/${contaId}/`);
          console.log("Conta do Fetch: ", conta);
          this.selectedConta = conta.data;

          this.data = {
            numero: this.selectedConta.numero,
            subconta_nome: this.selectedConta.subconta_nome,
            banco_id: this.selectedConta.banco_id,
            moeda_id: this.selectedConta.moeda_id,
            descricao: this.selectedConta.descricao,
          }

        } catch (error) {
          console.log("Erro ao buscar conta: ", error);
        }
      },
      
      async getMoeda(){
        try {
          let moeda = await req.fetch('moeda/');
          console.log("moeda do Fetch: ", moeda);
          this.moedasData = moeda.data;
        } catch (error) {
          console.log("Erro ao buscar moeda: ", error);
        }
      },

      async registerData(){
        console.log("Data to register: ", this.data);
        try {
          const finalData = {
            ...this.data,
            isnostra: this.isNostro
          }

          let res = await req.create('conta/registrar/', this.data);
          console.log("Resposta do registro: ", res);
          this.setContasData();
          this.clearForm();
        } catch (error) {
          console.log("Erro ao registrar conta: ", error);
          this.$swal.fire({
            position: 'bottom-end',
            icon: 'error',
            title: 'Erro ao registrar conta!',
            showConfirmButton: false,
            timer: 2000,
            toast: true
          })
        }
      },

      async editData(){
        console.log("Data to edit: ", this.data);
        try {
          let res = await req.update(`conta/${this.data?.id??0}/atualizar/`, this.data);
          console.log("Resposta da edição: ", res);
          this.setContasData();
          this.clearForm();
        } catch (error) {
          console.log("Erro ao editar conta: ", error);
          this.$swal.fire({
            position: 'bottom-end',
            icon: 'error',
            title: 'Erro ao editar conta!',
            showConfirmButton: false,
            timer: 2000,
            toast: true
          })
        }
      },
    }, 
    
    watch: {  
      // Watcher para selectedContaId
      selectedContaId: {
        handler(newVal, oldVal) {
          console.log("Selected conta id: ", newVal);
          
          if (newVal == 0) {
            console.log("Desabilitando campos..............................");
            this.clearForm();
          } else {
            console.log("Habilitando campos..............................");
            this.setSelectedConta(newVal);
          }
        },
        immediate: true,
      },

      isNostro(){
        this.getBancos();
      },
    },

    created(){
      this.setContasData();
      this.getBancos();
      this.getMoeda();
    } 
  }
</script>
 
<style scoped>
  .form1{
    /*
    background-color: #41414157;
    */
    padding: .8em;
  }

  .form1 button{
    text-transform: capitalize;
    min-width: 5em;
  }

  .main-contents{ 
    padding: .5em;
    width: 100%;
    display: flex;
    gap: 2em;
    flex-wrap: wrap;
  } 

  input{
    outline: none;
    border: none;
  }

  /* Outros estilos... */
</style>