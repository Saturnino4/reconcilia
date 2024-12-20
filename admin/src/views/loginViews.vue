<template>
    <section class="containerlogin" style="">
        <!-- <header>
            <h1>D'Bella Beauty</h1>
        </header> -->
        <section class="left_side">
            <span>
                <h1>Saturnino, lda</h1>
                <!-- <img src="../assets/logo.png" alt=""> -->
                <!-- <h1>D'Bella Beauty</h1> -->
            </span>
            <form>
                <h2>Autentification</h2>
                <!-- <label for="">username:</label> -->
                <input @change="validForm" v-model="usernameValue"
                :style="{border: usernameValue.length < 4 && tryLogin ? '1px solid red' : 'none'}"
                type="text" placeholder="username..." autofocus>
                <span class="pass" 
                :style="{border: passwordValue.length < 4 && tryLogin ? '1px solid red' : 'none'}"
                >
                    <!-- <Icon class="show-pass" icon="mdi:password" /> -->
                    <input 
                    
                    @change="validForm" v-model="passwordValue"  :type="inputType" class="inputPassword" placeholder="password..." style="box-shadow: none;">
                    <Icon v-if="!showPass" @click="toogleShowPassword" class="show-pass" icon="mdi:show" />
                    <Icon v-if="showPass" @click="toogleShowPassword" class="show-pass" icon="mdi:hide" />
                    
                </span>
                <span>
                    <span>
                        <input type="checkbox" name="lembrar" 
                        :style="{border: usernameValue.length < 8 && tryLogin ? '1px solid red' : 'none'}"
                        id="lembrar">
                        <label style="cursor: pointer;" for="lembrar"> Lembrar username</label>
                    </span>
                    
                </span>
                <button id="btn-login" type="button" @click="login" disabled ref="btnLogin">Entrar</button>
            </form>
        </section>
        <section class="right_side">
            <img src="" alt="">
        </section>
    </section>
</template>

<script>


    import axios from 'axios';
    import { BASE_URL, KEY } from '@/config';
    export default{
        name: 'Login',
        data(){
            return{
                usernameValue : '',
                tryLogin: false,
                trying: 0,
                passwordValue : '',
                showPass: false,
                inputType: 'password',
                user: null,
                role: null,
                fail: false,
                ip: '',
                counter: 0
            }
        },
        methods:{
            validForm(){
                
                if (this.usernameValue !== '' && this.passwordValue !== '' ) {
                    this.$refs.btnLogin.disabled = false
                }
            },

            async login(){
                let btnLogin = document.getElementById('btn-login')
                this.tryLogin = true

                if(this.trying > 3 ){
                    if(btnLogin.disabled != true)
                        btnLogin.disabled = true

                    return
                }
                this.trying ++

                // try{
                //     localStorage.setItem('tentativa', this.counter + 1)
                // }
                // catch(error){
                //     console.log(error)
                // }

                // try{
                //     this.counter = localStorage.getItem('tentativa')
                // }
                // catch(error){
                //     console.log(error)
                // }

                // if(this.counter > 5){
                //     console.log('Tentativas excedidas');
                //     return
                // }

                // if (this.usernameValue.length < 4 || this.passwordValue.length < 4 ){
                    
                //     return
                // }


// ----------------  Pegar IP ------------------------------------------------------------------------------------------------------
                axios.get('https://api.ipify.org?format=json')
                .then(response => {
                    this.ip = response.data.ip
                    console.log(response.data.ip);
                })
                .catch(error => {
                    console.error(error);
                });

// --------------------------------------------------------------------------------------------------------------------------------
                console.log('URL: ',`${BASE_URL}/login/?key=${KEY}`);
                

                try{
                    const res = await axios.post(`${BASE_URL}/login/?key=${KEY}`,{
                        username: this.usernameValue,
                        password: this.passwordValue,
                        ip: this.ip
                    })
                    // .then(response => console.log(response.data) )
                    .catch(err => { 
                        if(err.message == "Network Error"){
                            this.$swal.fire({
                                position: 'top',
                                icon: 'error',
                                title: 'Falha no servidor, tente mais tarde!',
                                showConfirmButton: false,
                                timer: 1500,
                                toast: true
                            })
                            return
                        }
                    })

                    // try{}
                    
                    this.user = res.data.data.user
                    // this.role = res.data.data.role
                    this.fail = false
                    // return
                }
                catch(err){
                    this.fail = true
                    console.log('Erro no login: ',err);
                    
                }

                
                
                if (!this.fail){
                    

                    try {
                        localStorage.setItem('userData', JSON.stringify(this.user))
                        // localStorage.setItem('role', JSON.stringify(this.role))
                    } catch (error) {
                        console.log(error)
                    }

                this.$router.push('/')
                }else{
                    this.$swal.fire({
                        position: 'top',
                        icon: 'error',
                        title: 'Falha na autentificação',
                        showConfirmButton: false,
                        timer: 1500,
                        toast: true
                    })
                }
            },
            toogleShowPassword(){
                this.showPass = !this.showPass
                if (this.inputType == 'password'){
                    this.inputType = 'text'
                }else{
                    this.inputType = 'password'
                }
            }
        },
        created(){
            // axios.get('http://127.0.0.1:8000/api/v1/utilizador/?key=123')
            // .then(res => {
            //     this.users = res.data.data
            // })

            // .catch(err => {
            //     console.log(err)
            // })

        }
                
        
    }

</script>


<style scoped>
   .pass{
       overflow: hidden;
       background-color: #fff;
       border-radius: .5em;
       display: flex;
       
    }
    .pass .show-pass{
        height: 100%;
        padding: .2em;
        font-size: 25pt;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }

   .containerlogin{
        user-select: none;
        background-color: red;
        display: flex;
        justify-content: space-between;
        /* padding-top: 5em; */
        height: 100vh;
        width: 100vw;
   } 

   .left_side{
        flex: .65;
        display: flex;
        flex-direction: column;
        align-items: center;
        /* gap: 2em; */
        /* justify-content: center; */
        /* flex: .7; */
        padding: 1em;
        padding-top: 3em;

   }

    form{
        width: 100%;
        /* background-color: #091d92f8; */
        display: flex;
        flex-direction: column;
        gap: 1em;
        padding: 2em 5em;
        border-radius: .5em;
    }
    
    form h2{
        color: #300101;
        font-size: 25pt;
        text-align: center;
    }

    form input:not(input[type="checkbox"]){
        width: 100%;
        padding: .5em;
        outline: none;
        font-size: 14pt;
    }

    form button{
        font-size: 16pt;
        padding: .4em;
        background-color: var(--secondary-2);
        background-color: var(--secondary_v2);
        color: var(--primary);
        font-weight: bold;
        transition: .5s;
    }
    
    form button:hover{
        background-color: var(--secondary);
        background-color: var(--secondary_v2-1);
        color: var(--white-1);
    }
    
    form input:not(input[type="checkbox"]), form button, .pass{
        border: none;
        border-radius: .3em;
        box-shadow: 0px 0px .1em .1em #0003;
    }

    /* form input.inputPassword{
        box-shadow: 0px 0px 10px 10px red;
    } */
    
    section.right_side{
        
        background-image: url('../assets/cover_3.png');
        background-color: var(--secondary_v2);
        background-size: cover;
        flex: .4;
        height: 100%;
    }

</style>


