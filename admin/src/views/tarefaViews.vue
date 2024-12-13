<script setup>
    import asideNavBar from '@/components/AsideNavBar.vue';
    import headerNav from '@/components/headerNav.vue';
</script>
<template >

    <asideNavBar />
    <section class="right-side">
            <headerNav />
            <section class="main-content">
                <header class="crud-title">
                    <h2></h2>
                </header>
                <section class="table-container" style="width: 100%;">

                    <section class="options-crud">
                        <button v-if="0" @click="openPopUp(null,'Registrar')" class="criar-btn">Registrar</button>
                    </section>



                    <section class="tarefa-card">
                        <header style="border-bottom: 1px solid #111;">
                            <h2 >Minhas tarefas</h2>
                            
                        </header>
                        <ul class="flex column flex-col">
                            <li>Aprovar eliminacao de linha extrato</li>
                            <li>Aprovar eliminacao de linha extrato</li>
                            <li>Aprovar eliminacao de linha extrato</li>

                        </ul>
                    </section>

                    <!-- <CustomTable :tableData="extrato" /> -->

               
                </section>
            </section>

            <popUp v-if="false"  >
                <ClienteForm :props-data="propsData" />
            </popUp>

    </section>
    
</template>

<script>
    
    import ClienteForm from '@/components/clienteForm.vue';
    import popUp from '@/components/popUp.vue';
    import axios from 'axios';
    import { BASE_URL, KEY } from '@/config';
    import { mapState } from 'vuex';
    import CustomTable from '@/components/table.vue';
    import { fakeExtrato } from '@/services/fakeData';

    export default {
        components:{
            ClienteForm,
            popUp,
            CustomTable,

        },
        data() {
            return {
                status: 0,
                clientes: [],
                propsData: {title: '', data: {}, action: '' },
                extrato: [],

            }
        },
        methods: {

            getExtrato(){
                this.extrato = fakeExtrato()
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
            this.getExtrato()
        },

        computed:{
            ...mapState(['emiter'])
        },

        watch:{
            emiter(newValue, oldValue) {
                this.getAllClientes()
            }
        }  
        
        
    }
</script>

<style scoped>
    .tarefa-card{
        background-color: #fff9;
        color: #0009;
        padding: 1em;
        max-width: 30em;
        min-height: 50dvh;
        border-radius: .5em;
        margin: 1em 0;
        border: 1px solid var(--secondary_v2);

    }

    .tarefa-card header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1em;
        color: var(--secondary_v2);
    }

    .tarefa-card ul{
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: .5em;
    }

    .tarefa-card ul li{
        background-color: #0003;
        padding: .5em;
        border-radius: .5em;
        cursor: pointer;
    }

    .tarefa-card ul li:hover{
        background-color: #0006;
        color: #fff;
    }


</style>
