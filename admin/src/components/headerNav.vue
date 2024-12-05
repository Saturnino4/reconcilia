<template>
     <header class="shadow" id="mainHeader">
        <div class="left">
            <Icon class="icon" id="menu-icon" icon="iconamoon:menu-burger-horizontal-fill" />
        </div>
        <div class="center">
            <h1>Reconciliação de contas</h1>
        </div>
        <div class="right">
            <Icon class="icon" :icon="fullscreemIcon" @click="fullScreem" />
            <span style="position: relative;" @mouseenter="showUserOption" @mouseleave="hideUserOption">
                <Icon class="icon" icon="iconamoon:profile-circle-fill" />
                <span >{{ user?.role_name ?? 'admin' }}</span> 
                <Icon  class="icon-2" icon="iconamoon:arrow-down-2-duotone" />
                <div :style="userOption" class="user-options" @mouseleave="hideUserOption">
                    <ul>
                        <li> <RouterLink to="/">Ver perfil</RouterLink> </li>
                        <li> <RouterLink to="#" @click="logOutComfirm" >Logout</RouterLink></li>
                        <li></li>
                    </ul>
                </div>
            </span> 
            <Icon title="Notificações" class="icon icon-3" icon="iconamoon:notification-fill" />
            <Icon title="Definições" class="icon icon-3" icon="iconamoon:settings-fill" />
        </div>
    </header>   
</template>

<script>
    import { ref } from 'vue';

    export default {
        data() {
            return {
                user: {},
                userOption: "display: none;",

                fullscreemIcon: 'iconamoon:screen-full-light',
            };
        },
        methods: {
            showUserOption(){
                this.userOption = "display: flex;" 
            },
            hideUserOption(){
                this.userOption = "display: none;" 
            },
            logOutComfirm() {
                this.$swal({
                    title: 'Certeza que desejas sair?',
                    text: '',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Sim',
                    cancelButtonText: 'Cancelar',
                    reverseButtons: true
                }).then((result) => {
                    if (result.isConfirmed) {

                        try{
                            localStorage.removeItem('userData');
                            localStorage.removeItem('role');
                            this.$router.push('/login');
                        }
                        catch(e){
                            console.log(e);
                            this.$swal.fire({
                                icon: 'error',
                                title: 'Erro',
                                text: 'Erro ao sair!'
                            })
                        }

                    }
                }).catch(() => {
                    // O usuário clicou em 'Cancelar' ou fechou o alerta. Não faz nada.
                });
            },
            fullScreem() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
                this.fullscreemIcon = 'iconamoon:screen-normal-light';
            } else {
                if (document.exitFullscreen) {
                document.exitFullscreen();
                this.fullscreemIcon = 'iconamoon:screen-full-light';
                }
            }
            },
        },
        created(){
            try {
                this.user = JSON.parse(localStorage.getItem('userData'))
            } catch (error) {
                console.log(error)
            }
        }
    };
</script>

<style scoped>

    .icon-3{
        color: red;
        /* font-size: 3em; */
    }

    header {
        background-color: var(--white-1);
        padding: 1em;
        display: flex;
        justify-content: space-between;
    }
   
    /* header .left{
        background-color: #222;
    } */
    
    header .right {
        display: flex;
        gap: 1em;
    }

    header .right > span {
        display: flex;
        align-items: center;
        gap: .2em;
        cursor: pointer;
    }

    header .right span > .icon{
        margin-right: .2em;
    }
    
    header .right span > .user-options{
        position: absolute;
        width: 100%;
        background-color: #fff;
        color: #000;
        border-radius: .2em;
        top: 1.5em;
        display: flex;
        justify-content: center;
        z-index: 2;
        border: 2px solid #c2c2c2;
        border-top: none;
        /* box-shadow: 0px 0px 1px 1px #0003; */
        height: 5em;
        border-radius: 0px 0px .5em .5em;
        cursor: auto;

        background-color: var(--secondary-2);
        background-color: var(--secondary_v2);
        padding-top: .3em;
    }

    header .right span > .user-options ul{  
        padding-top: .3em;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        gap: .3em;
    }

    header .right span > .user-options ul li a{
        color: #000;
        
        color: #fff;
        
    }  
    header .right span > .user-options ul li a:hover{
        text-decoration: underline;
    }
    
    .icon{
        width: 1.5em;
        height: 1.5em;
        color: var(--secondary);
        color: var(--secondary_v2);
        cursor: pointer;
        transform: .3s;
        /* color: red; 
        filter: drop-shadow(0px 0px .5em yellow);
        */
    }
    
    .icon-3:hover{
        transform: scale(1.1);
    }

    #menu-icon{
        height: 100%;
    }

   

    div {
        height: 100%;
        display: flex;
        align-items: center;
    }

</style>
