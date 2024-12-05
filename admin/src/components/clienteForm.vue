<template lang="">
    <section class="form-container">
                <header>
                    <Icon @click="closePop" icon="carbon:close-filled" class="close-icon" />
                </header>
                <h2 style="text-align: center;color: #111;">{{ $props.propsData.title }}</h2>
                <form @submit.prevent>
                    <input v-model="nameField" type="text" name="" id="nome" placeholder="Nome...">
                    <input v-model="emailField" type="text" name="" id="email" placeholder="Email...">
                    <input v-model="phoneField" type="number" name="" id="password" placeholder="Telefones...">
                    <input v-model="addressField" type="text" name="" id="password" placeholder="Endereço...">
                    
                    <button @click="submitForm(propsData.action)" type="button">{{ propsData.action ?? '---' }} </button>
                </form>
            </section>
</template>

<script>
    import axios from 'axios';
    import { BASE_URL, KEY } from '@/config';
    export default {
        name: 'FuncionarioForm',
        components: {
            
        },
        data() {
            return {
                nameField: this.propsData.data.nome ?? '',
                emailField: this.propsData.data.email ?? '',
                phoneField: this.propsData.data.telefone ?? '',
                addressField: this.propsData.data.endereco ?? '',
                userField: this.propsData.data.user ?? '',
            }
        },
        methods:{
            closePop(){
                this.$store.state.popUp.show = false
            },
            async RegisterCliente(){
                console.log(this.formData);
                try {
                    axios.post(`${BASE_URL}/cliente/registrar/?key=${KEY}`,this.formData)
                    .catch(err =>{
                        this.$swal.fire({
                            position: 'top',
                            icon: 'warning',
                            title: 'Campo obrigatorio imcompleto',
                            showConfirmButton: false,
                            timer: 5000,
                            toast: true
                        })
                    })
                    return true
                } catch (error) {
                    return false
                }
            },

            async UpdateCliente(id){
                // console.log('url',`${BASE_URL}/cliente/${id}/atualizar/?key=${KEY}`); return
                try {
                    // return true
                    axios.put(`${BASE_URL}/cliente/${id}/atualizar/?key=${KEY}`,this.formData)
                    // console.log('Testeeee'); return true
                    .catch(err =>{
                        this.$swal.fire({
                            position: 'top',
                            icon: 'warning',
                            title: 'Campo obrigatorio imcompleto',
                            showConfirmButton: false,
                            timer: 5000,
                            toast: true
                        })
                    })
                    return true
                } catch (error) {
                    console.log('Error: ',error);
                    return false
                }
            },

            async submitForm(action=null){
                if (action === 'editar'){
                    if (await this.UpdateCliente(this.propsData.data.id) == true ){
                        
                        this.$store.state.emiter = !this.$store.state.emiter
                        this.$swal.fire({
                            position: 'top',
                            icon: 'success',
                            title: 'Editado com sucesso',
                            showConfirmButton: false,
                            timer: 2000,
                            toast: true
                        })
                        console.log('Formdata: ',this.formData);
                    }else{
                        this.$swal({
                            title: 'Error!',
                            text: 'Falha ao fazer edição',
                            icon: 'error',
                            confirmButtonText: 'OK',
                            timer: 3000,
                            showCancelButton: false,
                            cancelButtonText: 'Cancelar',
                            reverseButtons: false
                        })
                    
                    }
                }else{
                    if(await this.RegisterCliente() == true ){
                        // console.log('Testeeee');return

                        this.$store.state.emiter = !this.$store.state.emiter
                        this.$swal.fire({
                            position: 'top',
                            icon: 'success',
                            title: 'Registrado com sucesso',
                            showConfirmButton: false,
                            timer: 1500,
                            toast: true
                        })
                    }else{
                        this.$swal({
                            title: 'Error!',
                            text: 'Falha ao fazer registro',
                            icon: 'error',
                            confirmButtonText: 'OK',
                            timer: 3000,
                            showCancelButton: false,
                            cancelButtonText: 'Cancelar',
                            reverseButtons: false
                        })
                    }                    
                }
            },


        },
        props:{
            propsData: Object
        },

        computed:{
            formData(){
                return {
                    nome: this.nameField,
                    email: this.emailField,
                    telefone: this.phoneField,
                    endereco: this.addressField
                }
            }
        },

        created(){
            console.log(this.propsData);
            // if (!this.propsData.data.nome && this.propsData.action === 'editar'){
            //     this.$swal({
            //         title: 'Alerta!',
            //         text: 'Funcionario sem dados!',
            //         icon: 'warning',
            //         confirmButtonText: 'OK',
            //         timer: 3000,
            //         showCancelButton: false,
            //         cancelButtonText: 'Cancelar',
            //         reverseButtons: false
            //     })
            // }
        },
        errorCaptured(err, vm, info) {
            this.$swal({
            title: 'Erro!',
            text: 'Ocorreu um erro ao renderizar a view: ' + err.toString(),
            icon: 'error',
            confirmButtonText: 'OK',
            });
            return false; // isso impede que o erro seja propagado para componentes ancestrais
        },


    };
</script>

<style scoped>


    section.popup-container{
        background-color: #0008;
        backdrop-filter: blur(2px);
        color: #fff9;

        position: absolute;
        top: 0;
        left: 0;
        height: 100vh;
        width: 100vw;
    }

     header{
        display: flex;
        justify-content: center;
        padding: 1em;
    }
    
    .pop-main-contet{
        padding: 1em;
        display: flex;
        justify-content: center;
    }
    
     .form-container{
        background-color: #0000ff;
        width: 30em;
        padding-bottom: 3em;
        border-radius: .5em;
        box-shadow: 0px 0px .5em .3em #0003;
    }
     .form-container header{
        display: flex;
        justify-content: end;
        /* background-color: red; */
        padding-bottom: 0px;
        padding-top: 1em;
        padding-right: 1em;
    }

     form{
        padding: 1em;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 1em;
    }
     form input, form button,  form select{
        padding: .3em;
        border: none;
        border-radius: .5em;
        outline: none;
        box-shadow: 0px 0px .2em .2em #0003;
        font-size: 13pt;
    }

     form input{
        padding-left: .8em;

    }

     form button{
        margin-top: 0.5em;
         background-color: #111;
         padding: .5em;
         color: #fff9;
         font-weight: bold;
         
         text-transform: capitalize;
        }
        form button:hover{
            background-color: #000;
            color: #fff;
        }

</style>
 