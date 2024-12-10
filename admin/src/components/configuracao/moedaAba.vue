<template>
   <section class='main-contents'>
        <form class="form1 rounded" @submit.prevent>
            <p style="opacity: .8;">Moeda</p>
            <input type="text" placeholder="nome" v-model="data.nome">
            <input type="text" placeholder="cifrão" v-model="data.cifrao">
            <input type="text" placeholder="abreviatura" v-model="data.abreviatura">
            <span class="flex gap s-between">
                <button v-if="!isFormEMpty" @click="clearForm" style="background-color: #222;">Limpar</button>
                <button @click="submitForm">{{ action }}</button>
            </span>
        </form>
        <section class="table_section">
            <CustomTable :tableData="moedasData" @returnData="returnData"  />
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
                current_aba: 'moeda',
                data: {
                    nome: '',
                    cifrao: '',
                    abreviatura: '',
                },

                action: 'registrar',
                moedasData: [],
                fakeMoedas: [
                    {nome: 'Dólar', cifrao: '$', abreviatura: 'USD', status: 'ativo'},
                    {nome: 'Euro', cifrao: '€', abreviatura: 'EUR', status: 'ativo'},
                    {nome: 'Libra', cifrao: '£', abreviatura: 'GBP', status: 'ativo'},
                    {nome: 'Franco', cifrao: '₣', abreviatura: 'CHF', status: 'ativo'},
                ],

                propsData: {
                    data: this.fakeMoedas,
                    columns: ['nome', 'cifrão', 'abreviatura'],
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
                // this.data.cifrao = data.cifrão;
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
                    cifrao: '',
                    abreviatura: '',
                }
                this.action = 'registrar';
            },


            async setMoedasData(){
                // console.log("setMoedasData chamado..............................");
                
                try {
                    let moedas = await req.fetch('moeda/');
                    // let moedas = await axios.get('http://localhost:8000/api/v1/moeda/');
                    console.log("moedas do Fetch: ", moedas);
                    
                    this.moedasData = moedas.data;
                } catch (error) {
                    console.log("Erro ao buscar moedas: ", error);

                    this.$swal.fire({
                        position: 'bottom-end',
                        icon: 'error',
                        title: 'Erro ao listas moedas!',
                        showConfirmButton: false,
                        timer: 2000,
                        toast: true
                    })
                }
                
                
                // this.moedasData = moedas.data;
            },

            async registerData(){
                console.log("Data to register: ", this.data);
                try {
                    let res = await req.create('moeda/registrar', this.data);
                    console.log("Resposta do registro: ", res);
                    this.setMoedasData();
                    this.clearForm();
                } catch (error) {
                    console.log("Erro ao registrar moeda: ", error);
                    this.$swal.fire({
                        position: 'bottom-end',
                        icon: 'error',
                        title: 'Erro ao registrar moeda!',
                        showConfirmButton: false,
                        timer: 2000,
                        toast: true
                    })
                }
            },

            async editData(){
                console.log("Data to edit: ", this.data);
                try {
                    let res = await req.update(`moeda/${this.data?.id??0}/atualizar/`, this.data);
                    console.log("Resposta da edição: ", res);
                    this.setMoedasData();
                    this.clearForm();
                } catch (error) {
                    console.log("Erro ao editar moeda: ", error);
                    this.$swal.fire({
                        position: 'bottom-end',
                        icon: 'error',
                        title: 'Erro ao editar moeda!',
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
            this.setMoedasData();
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

</style> 