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
                <section class="">

                </section>
                <section class="table-container" style="width: 100%;">
                    <section>
                        <select name="bank_choice" id="bank_choice" v-model="bank_choice">
                            <option value="bank_1">Banco_1</option>
                            <option value="bank_2">Banco_2</option>
                            <!-- <option value="3">Banco 3</option> -->
                        </select>
                    </section>
                    <section class="options-crud">
                        <span>
                            <span>
                                <input id="import_reg" style="display: none;" type="file" @change="handleFileUpload('registro')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_reg')" class="criar-btn">Importar R.Externo</button>
                            </span>
                            <span>
                                <input id="import_extr" style="display: none;" type="file" @change="handleFileUpload('extrato')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_extr')" class="criar-btn">Importar Extrato</button>
                            </span>
                            <span v-if="bank_choice == 'bank_2'">
                                <input id="import_swift" style="display: none;" type="file" @change="handleFileUpload('swift')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_swift')" class="criar-btn">Importar Swift</button>
                            </span>
                        </span>

                        <span>
                            <button @click="openPopUp(null,'Registrar')" class="criar-btn">Registrar</button>
                        </span>

                    </section>
                    <section class="table-wrap flex gap s-between">
                        <CustomTable  :tableData="extrato" />
                        <CustomTable  :tableData="registro_externo" />
                        <CustomTable  :tableData="swift_data" />
                    </section>

                </section>
            </section>

            <popUp v-if="false"  >
                <!-- <ClienteForm :props-data="propsData" /> -->
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
    import { fakeExtrato } from '@/db/fakeData';
    import * as XLSX from 'xlsx';

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
                registro_externo: [],
                swift_data: [],
                bank_choice: 'bank_2',
            }
        },

        computed:{
            isExtrato_empty(){
                return this.extrato.length === 0 
            },
            isRegistro_empty(){
                return this.registro_externo.length === 0 
            },
            isSwift_empty(){
                return this.swift_data.length === 0 
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
                // console.log('Opeeen');
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

            
            triggerFileInput(id) {
                document.getElementById(id).click();
            },
            
            handleFileUpload(type) {
                const input = document.getElementById(
                    type === 'registro' ? 'import_reg' :
                    type === 'extrato' ? 'import_extr' :
                    'import_swift'
                );
                const file = input.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                    const data = new Uint8Array(e.target.result);
                    const workbook = XLSX.read(data, { type: 'array' });
                    const firstSheetName = workbook.SheetNames[0];
                    const worksheet = workbook.Sheets[firstSheetName];
                    const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
                    this.processExcelData(jsonData, type);
                    };
                    reader.readAsArrayBuffer(file);
                }
            },

            processExcelData(data, type) {
                const headers = data[0];
                const rows = data.slice(1);
                const result = rows.map(row => {
                    const obj = {};
                    headers.forEach((header, index) => {
                    obj[header] = row[index];
                    });
                    return obj;
                });
                
                if (type === 'registro') {
                    this.registro_externo = result;
                } else if (type === 'extrato') {
                    this.extrato = result;
                }else if (type === 'swift') {
                    this.swift_data = result;
                }

                console.log(`Processed ${type} data:`, result);
            },



            
        },
        created() {
            // this.getExtrato()
        },

        computed:{
            
        },

        watch:{
           
        }  
        
        
    }
</script>
