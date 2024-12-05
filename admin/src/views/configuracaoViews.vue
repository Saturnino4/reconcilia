<script setup>
    import asideNavBar from '@/components/AsideNavBar.vue';
    import headerNav from '@/components/headerNav.vue';
</script>
<template >

    <asideNavBar />
    <section class="right-side">
            <headerNav />
            <section class="main-content2" >
                <header class="crud-title">
                    <h2></h2>
                </header>
                <section class="table-container" style="width: 100%;" @click="console.log('Clicouuuuu')">
                    
                    <section v-if="0" class="options-crud">
                        <button @click="openPopUp(null,'Registrar')" class="criar-btn">Registrar</button>
                    </section>
                    
                    <section v-if="0" class="table-results flex gap j-center ">
                        <CustomTable title="Resultado" :tableData="extrato" />
                    </section>
                    
                    <section class="options-crud">
                        <span>
                            <div class="abas">Contas</div>
                            <div class="abas">Bancos</div>
                            <div class="abas">Moedas</div>
                        </span>
                        <span>
                            <!-- <div class="abas">Contas</div>
                            <div class="abas">Bancos</div>
                            <div class="abas">Moedas</div> -->
                        </span>
                        
                        
                    </section>

                    <section v-if="0" class="options-crud">

                        <span>
                            <button v-if="1" @click="vistaCompleta" class="criar-btn">Ver completo</button>
                            <button v-if="1" @click="melanger('registro')" class="criar-btn">mesclar</button>
                        </span>

                        <span>
                            <button v-if="1" @click="removeFiltro" class="criar-btn">remover filtros</button>
                            <button v-if="1" @click="restoreFiltro" class="criar-btn">c/ filtro</button>
                        </span>

                    </section>
                    <section v-if="1" style="width:100%;" class="table-wrap2 flex gap s-between">
                        <MoedaAba :props-data="propsData" />
                    </section>

                    <section v-if="0" class="table-wrap flex gap s-between">
                        <!-- <CustomTable title="Registros externo" :tableData="registroExterno" 
                        :itemStatus="{naoFeito: naoFeito_registro, feito: feito_registro, porConferir: porConferir_registro} " @returnData="handleRegistroReturn" :isSelectedRow="isSelectRegistro" /> -->
                        
                        <!-- <CustomTable title="Nosso extrato" :tableData="extrato" 
                        :itemStatus="{naoFeito: naoFeito_extrato, feito: feito_extrato, porConferir: porConferir_extrato} " @returnData="handleExtratoReturn" :isSelectedRow="isSelectExtrato" /> -->
                    </section>

                
                </section>
            </section>

            <popUp v-if="0"  >
            </popUp>

    </section>
    
</template>

<script>
    
    import ClienteForm from '@/components/clienteForm.vue';
    import popUp from '@/components/popUp.vue';
    import axios from 'axios';
    import { BASE_URL, KEY } from '@/config';
    import { mapState } from 'vuex';
    import CustomTable from '@/components/table_lite.vue';
    import { fakeRegistroInterno, fakeExtrato } from '@/db/fakeData';
    import MoedaAba from '@/components/configuracao/moedaAba.vue';

    export default {
        components:{
            ClienteForm,
            popUp,
            CustomTable,
            MoedaAba,

        },

        data() {
            return {
                status: 0,
                clientes: [],
                propsData: {title: '', data: {}, action: '' },
                registroExterno: [],
                extrato: [],

                naoFeito_extrato: [],
                feito_extrato: [],
                porConferir_extrato: [],

                naoFeito_registro: [],
                feito_registro: [],
                porConferir_registro: [],
                isSelectExtrato: false,
                isSelectRegistro: false,


            }
        },

        computed: {
            itemStatus_extrato(){
                return {
                    naoFeito: this.naoFeito_extrato,
                    feito: this.feito_extrato,
                    porConferir: this.porConferir_extrato,
                }
            },

            itemStatus_registro(){
                return {
                    naoFeito: this.naoFeito_registro,
                    feito: this.feito_registro,
                    porConferir: this.porConferir_registro,
                }
            },

        },
        methods: {

            handleExtratoReturn(data){
                this.feito_registro = data.tipo_movimento.split(' ').pop()
                this.feito_extrato = []

                this.isSelectRegistro = !this.isSelectRegistro
                
            },
            
            handleRegistroReturn(data){
                this.feito_extrato = data.tipo_movimento.split(' ').pop()
                this.feito_registro = []
                
                this.isSelectExtrato = !this.isSelectExtrato
            },

            getRegistroExterno(){
                this.registroExterno = fakeRegistroInterno()
            },

            getExtrato(){
                this.extrato = fakeExtrato()
            },


            vistaCompleta(){
                this.getRegistroExterno(),
                this.getExtrato()
            },

            removeFiltro(){
                this.feito_registro = []
                this.feito_extrato = []
                this.naoFeito_registro = []
                this.naoFeito_extrato = []

                this.porConferir_registro = []
                this.porConferir_extrato = []
            },

            restoreFiltro(){
                this.getRegistroExterno()
                this.getExtrato()
                this.reconciliarExtrato_de_registro()
                this.reconciliarRegistro_de_extrato()
            },


            reconciliarExtrato_de_registro() {
                const referenciasExtrato = this.extrato.map(item => item.tipo_movimento.split(' ').pop());
                const referenciasRegistro = this.registroExterno.map(item => item.tipo_movimento.split(' ').pop());

                const referenciasNaoEncontradas = referenciasExtrato.filter(ref => !referenciasRegistro.includes(ref));

                this.naoFeito_extrato = referenciasNaoEncontradas;

                // console.log('Referências não encontradas no registroExterno:', referenciasNaoEncontradas);
            },

            reconciliarRegistro_de_extrato() {
                const referenciasExtrato = this.extrato.map(item => item.tipo_movimento.split(' ').pop());
                const referenciasRegistro = this.registroExterno.map(item => item.tipo_movimento.split(' ').pop());

                const referenciasNaoEncontradas = referenciasRegistro.filter(ref => !referenciasExtrato.includes(ref));

                this.naoFeito_registro = referenciasNaoEncontradas;

                // console.log('Referências não encontradas no extrato:', referenciasNaoEncontradas);
            },

            melanger(tipo){
                if(tipo === 'registro'){

                
                    const map = new Map();

                    this.registroExterno.forEach(item => {
                        const reference = item.tipo_movimento.split(' ').pop();
                                if (!map.has(reference)) {
                                    map.set(reference, {
                                        // id: item.id,
                                        data_mov: item.data_mov,
                                        da_ccb: item.da_ccb,
                                        documento: item.documento,
                                        tipo_movimento: `ORE + Extra ref. ${reference}`,
                                        debito: 0,
                                        credito: 0,
                                        saldo_pos: item.saldo_pos
                                    });
                                }
                                const existingItem = map.get(reference);
                                existingItem.debito += item.debito;
                                existingItem.credito += item.credito;
                            });

                            const unifiedArray = Array.from(map.values());
                            console.log('Unified Array:', unifiedArray);
                            
                    
                            
                this.registroExterno = unifiedArray



                }else{
                    this.extrato = fakeExtrato()
                }
            },



            getAllClientes(){
                axios.get(`${BASE_URL}/cliente/?key=${KEY}`)
                .then(res =>{
                    this.clientes = res.data.data
                    this.status = res.status
                })
                .catch(err =>{
                    console.log(err.response.data.message);
                    this.$swal({
                        title: 'Error!',
                        text: 'Falha ao listar cliente',
                        icon: 'error',
                        confirmButtonText: 'OK',
                        timer: 3000,
                        showCancelButton: false,
                        cancelButtonText: 'Cancelar',
                        reverseButtons: false
                    })
                })
            },
            
            openPopUp(item = {},action = 'editar' ) {
                console.log('Opeeen');
                if ( action === 'editar' ){
                    this.propsData.title = 'Editar Funcionários'
                    this.propsData.data = item
                    this.propsData.action = 'editar'
                }else{
                    this.propsData.title = action+' Funcionários'
                    this.propsData.data = {}
                    this.propsData.action = action
                    
                }

                this.$store.state.popUp = {...this.$store.state.popUp, show:true, title: 'Editar Funcionários' }
            },

            deleteRegister(id){
                this.$swal({
                    title: 'Tem certeza?',
                    text: "Você não poderá reverter isso!",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Sim, deletar!',
                    cancelButtonText: 'Cancelar',
                }).then((result) => {
                    if (result.isConfirmed) {
                        try {
                            axios.delete(`${BASE_URL}/cliente/${id}/deletar/?key=${KEY}`,this.formData)
                            .catch(err =>{
                                this.$swal.fire({
                                    position: 'top',
                                    icon: 'warning',
                                    title: 'Algo deu errado!',
                                    showConfirmButton: false,
                                    timer: 5000,
                                    toast: true
                                })
                            })

                            this.$store.state.emiter = !this.$store.state.emiter
                            this.$swal({
                                title: 'Deletado!',
                                text: 'Seu registro foi deletado.',
                                icon: 'success',
                                confirmButtonText: 'OK',
                                timer: 3000,
                                showCancelButton: false,
                                cancelButtonText: 'Cancelar',
                                reverseButtons: false
                            })

                        } catch (error) {
                            this.$swal.fire({
                                position: 'top',
                                icon: 'warning',
                                title: 'Falha ao eliminar registro!',
                                showConfirmButton: false,
                                timer: 5000,
                                toast: true
                            })
                        }


                        
                    }
                })
            },
            
        },
        created() {
            this.getRegistroExterno()
            this.getExtrato()

            this.reconciliarExtrato_de_registro()

            this.reconciliarRegistro_de_extrato()


            console.log('--------------------------------------');
            console.log('Referências não encontradas no registroExterno:', this.itemStatus_registro);
            console.log('Referências não encontradas no extrato:', this.itemStatus_extrato);
            console.log('--------------------------------------');
            

        },

        computed:{
            ...mapState(['emiter'])
        },

        watch:{
            
        }  
        
        
    }
</script>


<style scoped>

    .main-content2{
        min-height: 90dvh;
    }

    .options-crud{
        
        display: flex;
    }
    .options-crud:first-child{
        padding: 0px;
    } 
    .options-crud:first-child > span{
        gap: .1em;
    }

    .options-crud:first-child .abas{
        display: flex;
        padding: .5em;
        background-color: var(--secondary_v2);
        background-color: var(--secondary-2);
        color: #fff;
    }

    .options-crud:first-child .abas:hover{
        opacity: .9;
        cursor: pointer;
    }

    .table-wrap, .table-wrap2{
        flex-wrap: wrap;
    }

</style>