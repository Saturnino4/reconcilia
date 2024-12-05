<template lang="">
    <section class="form-container">
                <header>
                    <Icon @click="closePop" icon="carbon:close-filled" class="close-icon" />
                </header>
                <h2 style="text-align: center;color: #fff;">{{ $props.propsData.title }}</h2>
                <form @submit.prevent>
                    <input v-model="usernameField" type="text" name="" id="username" placeholder="Nome...">
                    <input v-model="passwordField" type="password" name="" id="password" placeholder="password...">
                    <select v-model="roleField" id="">
                        <option value="">---selecione role---</option>
                        <option v-for="item in roles" :value="item.id"> {{ item.nome }} </option>
                    </select>
                    <button @click="submitForm(propsData.action)" type="button">{{ propsData.action ?? '---' }} </button>
                </form>
            </section>
</template>
 
<script>
    import axios from 'axios';
    import { BASE_URL, KEY } from '@/config';
    export default {
        components: {
            
        },
        data() {
            return {
                usernameField: this.propsData.data.username ?? '',
                passwordField: this.propsData.data.password ?? '',
                statusField: this.propsData.data.role ?? '',
                roleField: this.propsData.data.role_id ?? '',

                roles: [],
            }
        },
        methods:{
            closePop(){
                this.$store.state.popUp.show = false
            },

            async getRoles (){
                try {
                    axios.get(`${BASE_URL}/role/?key=${KEY}`)
                    .then(res => {
                        this.roles = res.data.data
                        // console.log('Roles: ',this.roles);
                    })
                    return true
                } catch (error) {
                    console.log('Error ao carregar roles',error);
                }
            },

            async RegisterUtililzador(){
                console.log(this.formData);
                try {
                    axios.post(`${BASE_URL}/utilizador/registrar/?key=${KEY}`,this.formData)
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

            async UpdateUtilizador(id){
                // console.log('url',`${BASE_URL}/utilizador/${id}/atualizar/?key=${KEY}`); return
                try {
                    axios.put(`${BASE_URL}/utilizador/${id}/atualizar/?key=${KEY}`,this.formData)
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

            async submitForm(action=null){
                if (action === 'editar'){
                    if (await this.UpdateUtilizador(this.propsData.data.id) == true ){
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
                    if(await this.RegisterUtililzador() == true ){
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
            }

        },
        props:{
            propsData: Object
        },

        created(){
            // console.log(this.propsData);
            this.getRoles()
        },
        computed: {
            formData() {
                return {
                    username: this.usernameField === "" ? null : this.usernameField,
                    password: this.passwordField === "" ? null : this.passwordField,
                    role_id: this.specialtyField === "" ? null : this.roleField,
                };
            }
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
 