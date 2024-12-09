<template>
    <section class='main-contents'>
         <form class="form1 rounded" @submit.prevent>
             <p style="opacity: .8;">Banco</p>
             <input type="text" placeholder="nome" v-model="data.nome">
             <select name="local" id="local" v-model="data.local_id" >
                <option value="0" disabled>-------- Selecione local -----------</option>
                <option v-for="local in localsData" :value="local.id">{{ local?.cidade + ' -' }} {{ local?.pais }}</option>
             </select>
             <textarea :value="data.descricao" name="descricao" id="descricao" placeholder="descrição..."></textarea>
             <span class="flex gap s-between">
                 <button v-if="!isFormEMpty" @click="clearForm" style="background-color: #222;">Limpar</button>
                 <button @click="submitForm">{{ action }}</button>
             </span>
         </form>
         <section class="table_section">
             <CustomTable :tableData="bancosData" @returnData="returnData"  />
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
 
         }, 
         data(){
            return{ 
                 isFormEMpty: true,
                 current_aba: 'banco',
                 data: {
                     nome: '',
                     local_id: 0,
                     descricao: '',
                 },
 
                 action: 'registrar',
                 bancosData: [],
                 localsData: [],
                 fakeBancos: [
                     {nome: 'Dólar', local_id: '$', descricao: 'USD', status: 'ativo'},
                     {nome: 'Euro', local_id: '€', descricao: 'EUR', status: 'ativo'},
                     {nome: 'Libra', local_id: '£', descricao: 'GBP', status: 'ativo'},
                     {nome: 'Franco', local_id: '₣', descricao: 'CHF', status: 'ativo'},
                 ],
 
                 propsData: {
                     data: this.fakeBancos,
                     columns: ['nome', 'Local', 'descricao'],
                 },
 
                 // dbRequests: new DBrequests(),
                 errorMessage: '',
 
 
            } 
         }, 
         methods: {  
 
             returnData(data){
                 console.log(data);
                 this.data = data;
                 this.action = 'editar';
                 // this.data.local_id = data.Local;
             },
     
 
             checkEmptyFields(){
                 let formFields = Object.values(this.data);
                 this.isFormEMpty = formFields.some(field => field === '');
             },
 
 
             async submitForm(){
                 if(this.action === 'registrar'){
                     this.registerData();
                 }else{
                     this.editData();
                 }
             },
 
             
             clearForm(){
                 this.data = {
                     nome: '',
                     local_id: '',
                     descricao: '',
                 }
                 this.action = 'registrar';
             },
 
 
             async setBancosData(){
                 // console.log("setBancosData chamado..............................");
                 
                 try {
                     let bancos = await req.fetch('banco/');
                     // let bancos = await axios.get('http://localhost:8000/api/v1/banco/');
                     console.log("bancos do Fetch: ", bancos);
                     
                     this.bancosData = bancos.data;
                 } catch (error) {
                     console.log("Erro ao buscar bancos: ", error);
 
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao listas bancos!',
                         showConfirmButton: false,
                         timer: 2000,
                         toast: true
                     })
                 }
                 
                 
                 // this.bancosData = bancos.data;
             },

             async getLocais(){
                 try {
                     let locais = await req.fetch('local/');
                     console.log("Locais do Fetch: ", locais);
                     this.localsData = locais.data;
                 } catch (error) {
                     console.log("Erro ao buscar locais: ", error);
                    //  this.$swal.fire({
                    //      position: 'bottom-end',
                    //      icon: 'error',
                    //      title: 'Erro ao listas locais!',
                    //      showConfirmButton: false,
                    //      timer: 2000,
                    //      toast: true
                    //  })
                 }
             },
 
             async registerData(){
                 console.log("Data to register: ", this.data);
                 try {
                     let res = await req.create('banco/registrar/', this.data);
                     console.log("Resposta do registro: ", res);
                     this.setBancosData();
                     this.clearForm();
                 } catch (error) {
                     console.log("Erro ao registrar banco: ", error);
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao registrar banco!',
                         showConfirmButton: false,
                         timer: 2000,
                         toast: true
                     })
                 }
             },
 
             async editData(){
                 console.log("Data to edit: ", this.data);
                 try {
                     let res = await req.update(`banco/${this.data?.id??0}/atualizar/`, this.data);
                     console.log("Resposta da edição: ", res);
                     this.setBancosData();
                     this.clearForm();
                 } catch (error) {
                     console.log("Erro ao editar banco: ", error);
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao editar banco!',
                         showConfirmButton: false,
                         timer: 2000,
                         toast: true
                     })
                 }
             },
 
 
        }, 
        watch: {  
 
             data(){
                 this.checkEmptyFields();
             },
 
         },
 
        created(){
            this.setBancosData();
            this.getLocais();
        } 
 
    }
 </script>
  
 <style scoped>
 
     .form1{
         background-color: #41414157;
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
 
 </style> 