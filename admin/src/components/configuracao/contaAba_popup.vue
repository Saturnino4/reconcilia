<template>
    <section class="popup" style="flex: 1">
        <div class="popup-wrap">
            <span class="flex gap">
                <span>
                    <label class="c-white mb-1">Nostro</label>
                    <CustomTable :noActions="1" :tableData="subContasByNumeroData" />
                </span>
                <span>
                    <label class="c-white mb-1" >Vostro</label>
                    <CustomTable :noActions="1" :tableData="contaVostra" />
                </span>
            </span>
        </div>
    </section>
</template>
  
<script>
 
    import CustomTable from '@/components/table.vue'
    export default { 
 
        components: {   
            CustomTable
        }, 
        props: {   
            propsData: {
                type: Object,
                required: true,
                default: () => ({
                    subContasByNumeroData: [],
                    contaVostra: [],
                }),
            },
        }, 
        computed: {
            subContasByNumeroData(){
                return this.propsData.subContasByNumeroData
            },
            contaVostra(){
                return this.propsData.contaVostra
            },

        },

        data(){
            return{ 

            } 
        }, 
        methods: {  

        }, 
        created(){

        } 

   }
</script>
 
<style scoped>
    .popup{
        background-color: #41414157;
        padding: .8em;
        border-radius: 5px;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;

        display: flex; 
        flex-direction: column;/*
        justify-content: center;*/

        align-items: center;
        gap: 1em;

        padding: 2em;
        padding-top: 4em;

        backdrop-filter: blur(1px);

    }

    .popup-wrap{
        background-color: var(--secondary-2);
        padding: 1em;
        border-radius: 5px;
        min-width: 20em;
        width: fit-content;
    } 

</style> 