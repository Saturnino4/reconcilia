<template>
   <section class='main-contents'>
        <form class="form1" @submit.prevent>
            <input type="text" placeholder="nome" v-model="data.nome">
            <input type="text" placeholder="cifrão" v-model="data.cifrao">
            <input type="text" placeholder="abreviatura" v-model="data.abreviatura">
            <button>{{ action }}</button>
        </form>
        <section class="table_section">
            <CustomTable :tableData="fakeMoedas" @returnData="returnData"  />
        </section>
   </section>
</template>
  
<script>
 
   import CustomTable from '@/components/table.vue';
   export default { 
 
        components: {   
            CustomTable,
        }, 
        
        props: {   

       }, 
       data(){
           return{ 

                data: {
                    nome: '',
                    cifrao: '',
                    abreviatura: '',
                },

                action: 'registrar',

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


           } 
       }, 
       methods: {  

        returnData(data){
            console.log(data);
            this.data = data;
            this.action = 'editar';
            // this.data.cifrao = data.cifrão;
        }

       }, 
       created(){

       } 

   }
</script>
 
<style scoped>

    .form1 button{
        text-transform: capitalize;
    }

   .main-contents{ 
        padding: .5em;

        width: 100%;

        display: flex;
        gap: 2em;
        flex-wrap: wrap;
   
   } 

</style> 