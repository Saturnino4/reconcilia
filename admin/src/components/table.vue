<template>
    <section class='main-content_table'>
        <table class="table-1" v-if="tableData.length > 0">
            <caption v-if="title != '0'">
                <h3>{{ title }}</h3>
            </caption>
            <thead>
                <tr>
                    <th :style="{ fontSize: sizeStyle }" 
                        v-for="(item, index) in visibleColumns" 
                        :key="index">
                        {{ item }}
                    </th>
                    <th v-if="!noActions">Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in processedTableData" 
                    :key="item.id || index"
                    :class="{ 'active-row': activeRow === index }"
                    @click="handleRowClick(index, item)"
                    @contextmenu.prevent="handleRightClick(index, item)"
                    :style="statusColoryze(item.tipo_movimento)" >
                    
                    <td v-for="(col, colIndex) in visibleColumns" 
                        :key="colIndex">
                        {{ formatValue(item[col], item) }}
                    </td>

                    <td v-if="!noActions">
                        <div class="btn-form-row">
                            <button @click.stop="openPopUp(item)" title="Editar">
                                <Icon class="edit icon" icon="raphael:edit" />
                            </button>
                            <button @click.stop="deleteRegister(item.id)" title="Eliminar">
                                <Icon class="delete icon" icon="ic:round-delete" />
                            </button>
                        </div>
                    </td>
                </tr>
                <tr v-if="status === 208">
                    <td style="text-align: center; padding: 1em; opacity: .8;" 
                        :colspan="visibleColumns.length + (noActions ? 0 : 1)">
                        Sem registros
                    </td>
                </tr>
            </tbody>
        </table>
        <div v-if="status !== 200" class="no-data">
            <p>{{ statusMessage }}</p>
        </div>
        <br>
    </section>
</template>

<script>
export default { 
    props: {
        tableData:{
             type: Array,
             required: true,
             default: () => [
                 {
                     header: 'No data',
                 }
             ],
         },
 
         status: {
             type: [Number, String],
             default: 200,
         },
 
         title: {
             type: String,
             default: '0',
         },
         noActions: {
             type: Boolean,
             default: false,
         },
         size: {
             type: String,
             default: 'small',
         },
         hiddenColumns: {
             type: Array,
             default: () => ['id','isnostra'],
         },
         itemStatus: {
             type: Object,
             default: () => ({
                 feito: [],
                 naoFeito: [],
                 porConferir: [],
             }),
         },
 
         isSelectedRow: {
             type: Boolean,
             default: false,
         },
    },
    data() {
        return { 
            tableHeaders: [], 
            activeRow: null,
             sizeValue: '1em',
             tableHeaders: [],
        };
    },
    computed: {
        sizeStyle(){
             if(this.size === 'small'){
                 return '1em'
             } else if(this.size === 'large'){
                 return '2em'
             }
             return '1.5em'
         },
 
         numericStatus() {
             const num = Number(this.status);
             return !isNaN(num) ? num : 200; // Retorna 200 se a conversão falhar
         },
 
         statusMessage(){
             switch (this.numericStatus) {
                 case 404:
                     return 'Nenhum registro encontrado';
                 case 500:
                     return 'Erro interno do servidor';
                 case 208:
                     return 'Sem registros';
                 default:
                     return 'Erro desconhecido';
             }
         },
 
         // Computed property para determinar as colunas visíveis
         visibleColumns() {
             return this.tableHeaders.filter(col => !this.hiddenColumns.includes(col));
         },
 
         // Mantém `processedTableData` sem remover o campo `id`
         processedTableData() {
             return this.tableData;
         }, 
    },
    methods: { 
        setTableHeaders() {
            // Redefine os cabeçalhos da tabela
            this.tableHeaders = [];

            console.log('tableHeaders antes:', this.tableHeaders);

            if (this.processedTableData.length === 0) {
                return;
            }

            if (this.tableHeaders.length > 0) {
                return;
            }

            // Extrai as chaves do primeiro objeto para definir os cabeçalhos
            this.tableHeaders = Object.keys(this.processedTableData[0]);
            console.log('------------------------------------------------------------');
            console.log('ProccessedTableData depois:', this.processedTableData);
            console.log('tableHeaders depois:', this.tableHeaders);
            console.log('------------------------------------------------------------');
            
            
        },
        handleRowClick(index, data) {
             this.activeRow = index;
             this.$emit('returnData', data)
         },
 
         handleRightClick(index, data){
             this.activeRow = index;
             console.log('Right click', data);
         },
 
         formatValue(value, item) {
             if (typeof value === 'number' && item === 'Banco_id') {
                 return value.toFixed(2); // Exemplo de formatação de números
             }
             if(value === null || value === undefined || value === ''){
                 return 'N/A';
             }
             
             return value;
         },
 
         unselectRow(){
             this.activeRow = null
         },
 
         statusColoryze(tipo){
             const styles = {         
                 fontSize: this.sizeStyle,              
                 borderBottom: '1px solid black',
                 marginBottom: '1px'
             };
 
             if (!tipo) {
                 return styles;
             }
 
             const refer = tipo.split(' ').pop();
 
             if(this.itemStatus.naoFeito.includes(refer)){
                 return {
                     ...styles,
                     backgroundColor: '#8c1f288a',
                     color: 'white',
                 };
             } else if(this.itemStatus.feito.includes(refer)){
                 return {
                     ...styles,
                     backgroundColor: 'green',
                     color: 'white'
                 };
             } else if(this.itemStatus.porConferir.includes(refer)){
                 return {
                     ...styles,
                     backgroundColor: 'yellow',
                     color: 'black',
                 };
             }
 
             return styles;
         },
 
         openPopUp(item) {
             // Emite o evento 'openPopUp' com o item selecionado
             this.$emit('openPopUp', item);
         },
 
         deleteRegister(id) {
             // Emite o evento 'deleteRegister' com o id do item
             this.$emit('deleteRegister', id);
         },
    },
    watch: {
        tableData: {
            handler() {
                // console.log('tableData mudooooooooou!');
                this.setTableHeaders();
            },
            deep: true,
            immediate: true,
        },
        isSelectedRow(){
             this.activeRow = null
         },
 
    },
    created() {
        this.setTableHeaders();
    },
};
</script>

<style scoped>


tr:hover{
    cursor: pointer;
    color: #7f0909;
  }

.active-row{
    background-color: #c2c2c2;
}

    </style>