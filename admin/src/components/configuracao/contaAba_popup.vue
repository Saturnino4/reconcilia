<template>
    <section class="popup" style="flex: 1">
        <div class="popup-wrap">

            <span class="close flex j-end w-100">
                    <Icon icon="mdi:close-circle" class="close-icon__" color="#fffa" width="24" height="24" @click="close" />
            </span>
            <span class="flex gap">
                <span>
                    <label class="c-white mb-1">Nostro</label>
                    <CustomTable :noActions="1" :tableData="subContasByNumeroData" @returnData="setSelectedSubConta" />
                </span>
                <span>
                    <label class="c-white mb-1" >Vostro</label>
                    <CustomTable :noActions="1" :tableData="contaVostra" @returnData="setSelectedContaVostra" />
                </span>
            </span>
            <footer class="">
                    <span class="flex gap ">
                        <label class="c-white" for="contaNostra">Conta nostra: </label>
                        <select id="contaNostra" class="input" v-model="selectedContaNostra">
                            <option value="0">---selecionar---</option>
                            <option v-for="item in contaNostra" :value="item">{{ item.numero }}</option>
                        </select>
                    </span>
                    <span class="flex gap ">
                        <label class="c-white ">Nostro:</label>
                        <i v-if="isSubContaSelected" class="c-white ">{{ selectedSubConta?.nome +' - ' + selectedSubConta?.numero  }}</i>
                        <i v-else style="opacity: .5;font-size: .9em;" class="c-white "> N/A </i>
                    </span>
                    <span class="flex gap ">
                        <label class="c-white ">Vostro:</label>
                        <i v-if="isVostraSelected" class="c-white ">{{ selectedContaVostra?.numero }}</i>
                        <i v-else style="opacity: .5;font-size: .9em;" class="c-white "> N/A </i>
                    </span>
                    <button v-if="isVostraSelected && isSubContaSelected" class="btn btn-primary" @click="close">Associar</button>
            </footer>
        </div>
    </section>
</template>
  
<script>
 
    import CustomTable from '@/components/table.vue'
    import { DBrequestsObj as req } from '@/services/requests';
    export default { 
 
        components: {   
            CustomTable
        }, 
        props: {   
            propsData: {
                type: Object,
                required: true,
                default: () => ({
                    data: {},
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

            isVostraSelected(){
                return Object.keys(this.selectedContaVostra).length > 0
            },

            isSubContaSelected(){
                return Object.keys(this.selectedSubConta).length > 0
            },

        },

        data(){
            return{ 

                contaVostra: [],
                contaNostra: [],
                selectedSubConta: {},
                selectedContaVostra: {},
                selectedContaNostra: {},

            } 
        }, 
        methods: {  
            close(){
                this.$emit('close');
            },

            setSelectedSubConta(subConta){
                this.selectedSubConta = subConta;
            },

            setSelectedContaVostra(contaVostra){
                this.selectedContaVostra = contaVostra;
            },

            async setNostraVostraConta(nostra=0){
                try{
                    let conta = await req.fetch(`conta/?nostro=${nostra}`);
                    console.log("conta do Fetch: ", conta);

                    if(nostra){
                        this.contaNostra = conta.data;
                        return
                    }
                    this.contaVostra = conta.data;

                } catch (error) {
                    console.log("Erro ao buscar conta: ", error);
                }

            }, 
            async getSusContasByNumero(numero=null){
                if(!numero){
                    return
                }
                try {
                let contas = await req.fetch(`subconta/?numero=${numero}`);
                console.log("contas do Fetch: ", contas);
                
                this.subContasByNumeroData = contas.data;
                // this.customContaData = contas.data;

                } catch (error) {
                console.log("Erro ao buscar contas: ", error);

                // this.$swal.fire({
                //     position: 'bottom-end',
                //     icon: 'error',
                //     title: 'Erro ao listar contas!',
                //     showConfirmButton: false,
                //     timer: 2000,
                //     toast: true
                // })
                }
            },

        }, 
        watch: {
            selectedContaNostra: {
                handler: function(val){
                    this.getSusContasByNumero(val?.numero);
                    console.log('selectedContaNostra mudou: ', val);
                    
                },
                deep: true
            }
        },
        created(){

            this.selectedContaNostra = this.propsData.data;
            console.log("selectedContaNostra: ", this.selectedContaNostra);
            

            this.setNostraVostraConta(1);
            this.setNostraVostraConta(0);
            this.getSusContasByNumero(this.selectedContaNostra?.numero ?? 11111);

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


    button{
        margin-top: .5em;
        padding: .5em 1em;
        border-radius: 5px;
        background-color: var(--primary);
        color: var(--white);
        border: none;
        cursor: pointer;
    }

</style> 