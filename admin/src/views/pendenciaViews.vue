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

                    <CustomTable :tableData="extrato" />

                    <!-- <table class="table-1">
                        <thead>
                            <tr>
                                <th>id</th>
                                <th>nome</th>
                                <th>email</th>
                                <th>telefone</th>
                                <th>Endereço</th>
                                <th v-if="true">ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in clientes">
                                <td>{{ item?.id ?? 'N/A' }}</td>
                                <td>{{ item?.nome ?? 'N/A' }}</td>
                                <td>{{ item?.email ?? 'N/A' }}</td>
                                <td>{{ item?.telefone ?? 'N/A' }}</td>
                                <td>{{ item?.endereco ?? 'N/A' }}</td>

                                <td>
                                    <div class="btn-form-row">
                                        <button @click="openPopUp (item ?? {})" title="editar">
                                            <Icon  class="edit icon" icon="raphael:edit" />
                                        </button>
                                        <button title="eliminar" @click="deleteRegister(item.id)" >
                                            <Icon class="delete icon" icon="ic:round-delete" />
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="status === 208">
                                <td style="text-align: center;padding: 1em;opacity: .8;" colspan="8" > Sem registros </td>
                            </tr>
                        </tbody>
                    </table> -->
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
