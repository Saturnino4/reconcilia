<template>
    <section class='main-contents'>
         <form class="form1 rounded" @submit.prevent>
             <p style="opacity: .8;">Local</p>
             <input type="text" placeholder="pais" v-model="data.pais">
             <input type="text" placeholder="cidade" v-model="data.cidade">
             <textarea :value="data.descricao" name="descricao" id="descricao" placeholder="descrição..."></textarea>
             <!-- <input type="text" placeholder="descricao" v-model="data.descricao"> -->
             <span class="flex gap s-between">
                 <button v-if="!isFormEMpty" @click="clearForm" style="background-color: #222;">Limpar</button>
                 <button @click="submitForm">{{ action }}</button>
             </span>
         </form>
         <section class="table_section">
             <CustomTable :tableData="localsData" @returnData="returnData" :status="localStatus"  />
         </section>
    </section>
 </template>
   
 <script>
  
    import CustomTable from '@/components/table.vue';
    import { DBrequestsObj as req } from '@/services/requests';
    export default { 
  
         components: {   
             CustomTable,
         }, 
         
         props: {   
 
         }, 
         data(){
            return{ 
                 isFormEMpty: true,
                 current_aba: 'local',
                 data: {
                     pais: '',
                     cidade: '',
                     descricao: '',
                 },
 
                 action: 'registrar',
                 localsData: [],
                 fakeLocals: [
                     {pais: 'Dólar', cidade: '$', descricao: 'USD', status: 'ativo'},
                     {pais: 'Euro', cidade: '€', descricao: 'EUR', status: 'ativo'},
                     {pais: 'Libra', cidade: '£', descricao: 'GBP', status: 'ativo'},
                     {pais: 'Franco', cidade: '₣', descricao: 'CHF', status: 'ativo'},
                 ],
 
                 propsData: {
                     data: this.fakeLocals,
                     columns: ['pais', 'cifrão', 'descricao'],
                 },
 
                 // dbRequests: new DBrequests(),
                 errorMessage: '',
                 localStatus: 200,
 
 
            } 
         }, 
         methods: {  
 
             returnData(data){
                 console.log(data);
                 this.data = data;
                 this.action = 'editar';
                 // this.data.cidade = data.cifrão;
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
                     pais: '',
                     cidade: '',
                     descricao: '',
                 }
                 this.action = 'registrar';
             },
 
 
             async setLocalsData(){
                 // console.log("setLocalsData chamado..............................");
                 
                 try {
                     let locals = await req.fetch('local/');
                     // let locals = await axios.get('http://localhost:8000/api/v1/local/');
                     console.log("locals do Fetch: ", locals);
                     
                     this.localsData = locals.data;
                     this.localStatus = locals.status;
                 } catch (error) {
                     console.log("Erro ao buscar locals: ", error);
                    this.localStatus = 500;
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao listas locals!',
                         showConfirmButton: false,
                         timer: 2000,
                         toast: true
                     })
                 }
                 
                 
                 // this.localsData = locals.data;
             },
 
             async registerData(){
                 console.log("Data to register: ", this.data);
                 try {
                     let res = await req.create('local/registrar/', this.data);
                     console.log("Resposta do registro: ", res);
                     this.setLocalsData();
                     this.clearForm();
                 } catch (error) {
                     console.log("Erro ao registrar local: ", error);
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao registrar local!',
                         showConfirmButton: false,
                         timer: 2000,
                         toast: true
                     })
                 }
             },
 
             async editData(){
                 console.log("Data to edit: ", this.data);
                 try {
                     let res = await req.update(`local/${this.data?.id??0}/atualizar/`, this.data);
                     console.log("Resposta da edição: ", res);
                     this.setLocalsData();
                     this.clearForm();
                 } catch (error) {
                     console.log("Erro ao editar local: ", error);
                     this.$swal.fire({
                         position: 'bottom-end',
                         icon: 'error',
                         title: 'Erro ao editar local!',
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
             this.setLocalsData();
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