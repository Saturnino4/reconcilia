<template>
    <div class="card">
        <div class="img-container">
            <!-- <picture> -->
                <img v-if="produto.foto != null" :src="imgSrc" alt="foto do produto">
                <img v-else src="@/assets/sem-foto.png" alt="foto do produto">
                <!-- <img :src="imgSrc" alt="foto do produto" @error="this.src='/assets/sem-foto.png'"> -->
                <!-- <div style="display: flex;justify-content: center;align-items: center;width: 100%;height: 100%;"> [foto] </div> -->
            <!-- </picture> -->
        </div>
        <footer>
            <h3>{{ produto.nome ?? 'N/A' }} ( {{ produto.quantidade ?? 'N/A' }} ) </h3>
            <p>
                {{ produto.descricao ?? 'N/A' }}
            </p>
            <div class="btn-form-row btn-container">
                <button @click="setProduto(produto)" title="editar" >
                    <Icon  class="edit icon" icon="raphael:edit" />
                </button>
                <button title="eliminar" @click="deleteRegister(produto.id)" >
                    <Icon class="delete icon" icon="ic:round-delete" />
                </button>
            </div>
        </footer>
    </div>
</template>

<script>

    import { BASE_URL, KEY } from '@/config';
    import axios from 'axios';
    export default {
        data() {
            return {
                produto: this.propsData.data ?? {}
            }
        },
        computed: {
            // imgSrc(){
            //     return `${BASE_URL}/produto/foto/${this.produto.id}/?key=121212121`;
            // },
            imgSrc(){
                console.log('Produto solo: ',`${this.produto.foto}`);
                console.log('Url-produto completo: ',`${BASE_URL}${this.produto.foto}`);
                // return  `${BASE_URL}/produto/foto/${this.$store.state.produto?.data.id}/?key=121212121`;

                let newBaseUrl = BASE_URL.split('/api')[0]

                return  `${newBaseUrl}${this.produto.foto}`;
            },
        },
        props: {
            propsData: {
                type: Object,
                required: true
            }
        },

        methods: {
            setProduto(produto){
                this.$store.state.produto.data = produto;
                this.$store.state.produto.action = 'update';
                console.log('Produto from card: ', this.$store.state.produto);
            },
            async deleteProduto(id){
                try {
                    await axios.delete(`${BASE_URL}/produto/${id}/eliminar/?key=121212121`);
                    this.$swal.fire({
                        position: 'top',
                        icon: 'success',
                        title: 'Produto eliminado com sucesso',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })

                    this.$store.state.produto.updated = !this.$store.state.produto.updated;

                } catch (error) {
                    console.log('Error ao eliminar produto: ',error);
                    this.$swal.fire({
                        position: 'top',
                        icon: 'error',
                        title: 'Error ao eliminar produto',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })
                }
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
                            axios.delete(`${BASE_URL}/produto/eliminar/${id}/?key=${KEY}`,this.formData)
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
                            console.log('Error ao eliminar produto: ',error);
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
            console.log(this.base);
        },
    }
</script>


<style scoped>

    .btn-container{
        background-color: transparent;
        position: absolute;
        bottom: 1em;
        width: 100%;
        padding: 0px 1em;
        display: flex;
        justify-content: center;
        gap: .5em;
    }
    .btn-container button{
        width: 100%;
        transition: .5s;
        background-color: #111;
        border-radius: .3em;
        
        padding: .1em .5em;
        
    }
    .btn-container button:hover{
        background-color: #000;
        transform: scale(1.02);
    }

    .card{
        position: relative;
        width: 20em;
        height: fit-content;
        background-color: #fff;
        border-radius: .3em;
        cursor: pointer;
    }
    .card:hover{
        box-shadow: 0px 0px .2em .2em #0003;
        transform: scale(1.008);
    }
    
    .img-container{
        width: 100%;
        height: 10em;
        background-color: #123;
        border-radius: .3em .3em 0px 0px;
        
    }
    
    picture{
        /* display: flex;
        justify-content: center;
        align-items: center; */
        /* padding: .5em; */
    }
    .img-container img{
        /* width: 15em; */
        width: 100%;
        max-height: 10em;
        object-fit: fill;
        object-position: center;
        /* border-radius: .3em .3em 0px 0px; */
    }

   
    .card footer{
        height: 10em;
        padding: .2em;
        text-align: center;
        background-color: #fff;
        border-radius: 0px 0px .3em .3em;
    }
    .card footer p{
        padding: .2em;
        height: 3em;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .card footer h3{
        padding-bottom: .2em;
    }

</style>