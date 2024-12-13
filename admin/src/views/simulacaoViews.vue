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
                <section class="table-container gap" style="width: 100%;">
                    <!-- <section> 
                        <select name="bank_choice" id="bank_choice" v-model="bank_choice">
                            <option value="bank_1">Banco_1</option>
                            <option value="bank_2">Banco_2</option>
                        </select>
                    </section> -->
                    <span class="flex gap ">
                        <span class="flex gap-1">
                          <label for="tipo_nostro">Nostro</label>
                          <input type="radio" name="tipo" id="tipo_nostro" :value="1" v-model="isNostro">
                        </span>
                        <span class="flex gap-1">
                          <label for="tipo_vostro">Vostro</label>
                          <input type="radio" name="tipo" id="tipo_vostro" :value="0" v-model="isNostro">
                        </span>
                      </span>
                    <section class="options-crud">
                        <span>
                            
                            <!-- <span v-if="0">
                                <input id="import_reg" style="display: none;" type="file" @change="handleFileUpload('registro')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_reg')" class="criar-btn">Importar R.Externo</button>
                            </span>
                            <span v-if="0">
                                <input id="import_extr" style="display: none;" type="file" @change="handleFileUpload('extrato')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_extr')" class="criar-btn">Importar Extrato</button>
                            </span> -->
                        </span>
                        <span>
                            <span>
                                <input id="import_swift" style="display: none;" type="file" @change="handleFileUpload('swift')">
                                <button style="background-color: #333;" @click="triggerFileInput('import_swift')" class="criar-btn">Importar Swift</button>
                                <button v-if="0" @click="openPopUp(null,'Registrar')" class="criar-btn">Registrar</button>
                            </span>
                        </span>
                        
                        
                    </section>
                    <form class="flex gap c-black max-w-30" style="width: 22em;" v-if="1">
                        <span  class="flex gap f_column s-between w-100 " style="padding: 1em;">
                            
                            <span class="flex" >
                                <input v-if="isNostro" class="ped w-100" style="color:#0009;padding:.2em .3em" type="text" value="BCN - Banco Cabo Verdeano de Negócios, S.A." disabled>
                            </span>
                            <span class="flex gap" >
                                <label for="banco-select">banco: </label>
                                <select v-if="!isNostro" class="w-100"  name="banco" id="banco-select" v-model="selectedbancoId">
                                  <option :value="0">---- Selecione banco ----</option>
                                  <option  v-for="banco in bancosData" :key="banco.id" :value="banco.id">{{ banco?.nome }}</option>
                                </select>
                            </span>

                            <span class="flex gap" >
                                <label for="conta-select">Conta: </label>
                                <select v-if="!isNostro" class="w-100"  name="conta" id="conta-select" v-model="selectedContaId">
                                  <option :value="0">---- Selecione conta ----</option>
                                  <option  v-for="conta in contasData" :key="conta.id" :value="conta.id">{{ conta?.numero }}</option>
                                </select>
                                <select v-else class="w-100"  name="conta" id="conta-select" v-model="selectedContaId">
                                    <option :value="0">---- Selecione conta ----</option>
                                    <option  v-for="conta in subContasData" :key="conta.id" :value="conta.id">{{ conta?.nome +' - '+ conta?.conta }}</option>
                                </select>
                            </span>
                            <span class="flex gap" >
                                <label for="conta-select">Inicio: </label>
                                <input type="date" name="inicio" id="">
                            </span>
                            <span class="flex gap" >
                                <label for="conta-select">Fim: </label>
                                <input type="date" name="fim" :value="getToday()">
                            </span>

                            <span>
                                <button class="b_ped">Aplicar</button>
                            </span>
                            
                          </span>
                        </form>
                    <section v-if="0" class="table-wrap flex gap s-between">
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
    import CustomTable from '@/components/table_lite.vue';
    import { fakeExtrato } from '@/services/fakeData';
    import { DBrequestsObj as req } from '@/services/requests';
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
                selectedContaId: 0,
                selectedbancoId: 0,
                clientes: [],
                contasData: [],
                subContasData: [],
                bancosData: [],
                propsData: {title: '', data: {}, action: '' },
                extrato: [],
                registro_externo: [],
                swift_data: [],
                bank_choice: 'bank_2',
                isNostro: 1,
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

            getToday() {
                const today = new Date();
                const yyyy = today.getFullYear();
                const mm = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
                const dd = String(today.getDate()).padStart(2, '0');
                return `${yyyy}-${mm}-${dd}`;
            },
                getTodayFormatted() {
                const today = new Date();
                const yyyy = today.getFullYear();
                const mm = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
                const dd = String(today.getDate()).padStart(2, '0');
                return `${dd}/${mm}/${yyyy}`;
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

            async setContasData(){
                try {
                let contas = await req.fetch(`conta/?nostro=0&banco_id=${this.selectedbancoId}`);
                console.log("contas do Fetch: ", contas);
                
                this.contasData = contas.data;
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
            async setSubContasData(){
                try {
                let contas = await req.fetch('subconta/?full=1');
                console.log("contas do Fetch: ", contas);
                
                this.subContasData = contas.data;
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


            async getBancos(){
                try {
                let bancos = await req.fetch(`banco/?nostro=0`);
                console.log("Bancos do Fetch: ", bancos);
                this.bancosData = bancos.data;

                this.bancosData.map(banco => {
                    if (banco.nome && banco.nome.toLowerCase().includes('bcn')) {
                    this.data.banco_id = banco.id;
                    }
                });

                } catch (error) {
                console.log("Erro ao buscar bancos: ", error);
                this.bancosData = [];
                }
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
            this.setContasData()
            this.setSubContasData()
            this.getBancos()
            // this.getExtrato()
        },

        activated() {
            // this.getAllClientes()
        },

        computed:{
           
        },

        watch:{

            isNostro(val){
                this.selectedContaId = 0
            },

            selectedbancoId(val){
                this.setContasData()
            }
           
        }  
        
        
    }
</script>

<style scoped>

    form input, form select{
        padding: .2em .3em;
        color: #0009;
        display: flex;
        width: 100%;
    }

    form input[type="date"]{
        display: flex;
        justify-content: end;
    }

    form label{
        min-width: 3em;
    }

    form button{
        padding: .3em .5em;
        color: #fff;
        background-color: #333;
        border: none;
        cursor: pointer;
    }

</style>
