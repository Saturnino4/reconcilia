<template>
   <section class='main-content_table'>
    <br>
    <table class="table-1" >
        <caption v-if="title != '0'">
            <h3>{{title}}</h3>
        </caption>
        <thead >
            <tr>
                <th v-for="item in tableHeders" :key="item">{{ item }}</th>
                <th v-if="!noActions">ações</th>
            </tr>
        </thead>
        <tbody>
            <tr 
                v-for="(item,index) in tableData" :key="item.id"
                :class="{ 'active-row': activeRow === index }"
                @click="handleRowClick(index, item)"
                @contextmenu.prevent="handleRightClick(index, item)"
                :style="statusColoryze(item.tipo_movimento)"
                 >
                <td v-for="(value, key) in item" :key="key">
                    {{ formatValue(value,item) }}
                </td>

                <!-- <td v-if="!noActions">
                    <div class="btn-form-row">
                        <button @click="openPopUp (item ?? {})" title="editar">
                            <Icon  class="edit icon" icon="raphael:edit" />
                        </button>
                        <button title="eliminar" @click="deleteRegister(item.id)" >
                            <Icon class="delete icon" icon="ic:round-delete" />
                        </button>
                    </div>
                </td> -->
            </tr>
            <tr v-if="status === 208">
                <td style="text-align: center;padding: 1em;opacity: .8;" colspan="8" > Sem registros </td>
            </tr>
        </tbody>
    </table>
    <br>
   </section>
</template>
  
<script>
 
   export default { 
 
       components: {   
       }, 
       props:{
        tableData:{
            type: Array,
            required: true,
            default: () => [
                {
                    header: 'No data',
                }
            ],
            
        },

        title: {
                type: String,
                default: () => '0',
        },
        noActions: {
            type: Boolean,
            default: () => false,
        },
        itemStatus: {
            type: Object,
            default: () => {
                return {
                    feito: [],
                    naoFeito: [],
                    porConferir: [],
                }
            },
        },

        isSelectedRow: {
            type: Boolean,
            default: () => false,
        },

       
    },
       data(){
           return{ 
                tableHeders: [],
                noActions: true,
                activeRow: null,
                
           } 
       }, 
       methods: { 

            setTableHeaders(){
                
                
                for (const key in this.tableData[0]) {
                    this.tableHeders.push(key)
                }
            },

            handleRowClick(index,data) {
                this.activeRow = index;

                this.$emit('returnData', data)

            },


            handleRightClick(index,data){
                this.activeRow = index;
                console.log('Right click', data);
                
            },

            formatValue(value,item) {
                // if (item === 'debito' || item === 'credito') {
                // if (typeof value === 'number') {
                //     return value.toFixed(2);
                // }
                return value;
            },


            unselectRow(){
                this.activeRow = null
            },


            statusColoryze(tipo){

                return {
                    fontSize: '1.2em',
                }

                // try {
                    
                //     const refer = tipo.split(' ').pop()
                //     if(this.itemStatus.naoFeito.includes(refer)){
                //         return {
                //             backgroundColor: '#8c1f288a',
                //             color: 'white',
                //             borderBotton: '1px solid black',
                //             marginBotton: '1px'
                //         }
                //     }else if(this.itemStatus.feito.includes(refer)){
                //         return {
                //             backgroundColor: 'green',
                //             color: 'white'
                //         }
                //     }else if(this.itemStatus.porConferir.includes(refer)){
                //         return {
                //             backgroundColor: 'yellow',
                //             color: 'black',
                //         }
                //     }
                // } catch (error) {
                //     console.log('Error: ', error);
                // }

            },
        
       }, 
       watch: {

            isSelectedRow(){
               this.activeRow = null
            },

            tableData: {
                handler() {
                    this.setTableHeaders();
                },
                deep: true
            }
        },



       created(){
            this.setTableHeaders()

            console.log('Table data: ', this.tableData);
            
            // console.log('--------------------------------------');
            // console.log(`Item status ${this.title}: `, this.itemStatus);
            // console.log('--------------------------------------');
            
            
       } 

   }
</script>
 
<style scoped>

    

   .main-content_table{ 



   } 


   tbody tr{

       cursor: pointer;
   }

   tbody tr:hover{
       background-color: var(--terciary);
       color: #fff6;
   }

   .active-row{
       background-color: green;
       color: blue;
   }





</style> 