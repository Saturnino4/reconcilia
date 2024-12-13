<template>
    <keep-alive>
    <aside class="relative shadow">
        
            <nav>
                <header class="profile">
                    <span>
                        <!-- <Icon class="icon-minimiza" icon="fluent:arrow-next-12-filled" /> -->
                        <Icon :class="{'reverse': isMinimized}" @click="setMinimized" class="icon-minimiza" icon="bxs:left-arrow" />
                    </span>
                    <h1 style="text-wrap:nowrap; font-family: 'arial'">
                        <Icon class="icon-logo" icon="bi:bank" />
                        <span v-if="!isMinimized" style="font-size: .5em;">
                            {{ ' '+empresa?.nome ?? 'empresa' }}
                            <hr style="border: .001em solid #fff5;">
                        </span> 
                        </h1>
                </header>
                <ul>
                    <li v-for="(item, index) in permissoes" :key="index">
                        <RouterLink active-class="rota-ativo" id="dash" :to="path[item.modulo]"> 
                            <span class="icon-text-container">
                                <Icon class="icon" :icon="icons[item.modulo]" /> 
                                <span v-if="!isMinimized" > {{ item.modulo }} </span>
                            </span> 
                        </RouterLink>
                        <span class="info"></span>
                    </li>
                    
                </ul>
            </nav>
            <RouterView />
        </aside>
    </keep-alive>

    <!-- <aside class="shadow">
            ...
        </aside> -->
</template>

<script>
    
    import { mapMutations, mapActions, mapGetters } from 'vuex';
    import { fakeEmpresa } from '@/services/fakeData';
    export default {
        name: 'AsideNavBar',
        data() {
            return {
                isMinimized: false,
                path:  {dashboard: '/',configuracao:'/configuracao',cliente:'/cliente',extrato: '/extrato',
                         registro_externo: '/registro_externo',recibo: '/recibo',
                         simulacao: '/simulacao',pendencia: '/pendencia',
                         analise: '/analise', tarefa: '/tarefa'
                        },
                icons: {cliente:'fluent:people-list-24-filled',dashboard: 'ion:home',configuracao: 'solar:settings-bold',
                extrato: 'fluent-mdl2:key-phrase-extraction',registro_externo: 'gravity-ui:database-arrow-right',
                simulacao: 'material-symbols:database-upload-rounded',
                pendencia: 'ic:outline-pending-actions',analise: 'carbon:analytics',
                tarefa: 'fluent:clipboard-task-list-ltr-24-filled'
            },
                permissoes: [
                    {
                    modulo:'dashboard',autorizacao: 'crud'
                    },
                    {
                        modulo:'configuracao',autorizacao: 'crud'
                    },
                    {
                        modulo:'cliente',autorizacao: 'crud'
                    },
                    {
                        modulo:'tarefa',autorizacao: 'crud'
                    },
                    {
                        modulo:'simulacao',autorizacao: 'crud'
                    },
                    {
                        modulo:'pendencia',autorizacao: 'crud'
                    },
                    {
                        modulo:'extrato',autorizacao: 'crud'
                    },
                    {
                        modulo:'registro_externo',autorizacao: 'crud'
                    },
                    {
                        modulo:'analise',autorizacao: 'crud'
                    },
                ],
                empresa: fakeEmpresa(),
            }
        },

        computed: {
            ...mapGetters(['getLoggedUser','getPermissao']),
        },

        methods: {
            // ...mapActions(['fethPermissoes']),
            ...mapMutations(['setLoggedUser']),

            setMinimized() {
                try {
                    localStorage.setItem('isMinimized', JSON.stringify(!this.isMinimized));
                    this.isMinimized = !this.isMinimized;
                } catch (error) {
                    console.log('Nao conseguiu set Minimizar!', error);
                }
            },

            getMinimized() {
                try {
                    this.isMinimized =  JSON.parse(localStorage.getItem('isMinimized'));
                    console.log('Minimizado: ', this.isMinimized);
                    
                } catch (error) {
                    console.log('Nao conseguiu obter Minimizar!', error);
                    // return false; // Valor padrão caso ocorra um erro
                }
            }

        },

        async created() {


            this.getMinimized();
            
            this.setLoggedUser()
            // await this.$store.dispatch('fethPermissoes', this.getLoggedUser.id)

            // this.permissoes = this.getPermissao


            // this.permissoes.push(
                
            // )


            // console.log('User: ', this.getLoggedUser);
            // console.log('Permissões no aside: ', this.permissoes);
            
            
        },
        
    }
</script>

<style scoped>

    .reverse{
        transform: rotate(180deg);
    }

    .rota-ativo{
        color: #fff;
        border-bottom: 1px solid red;
        transform: scale(1.09);
        /* background-color: #0003;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: .5em; */
    }


    .icon-minimiza{
        color: #fff7;
        position: absolute;
        top: 1em;
        right: .1em;
      
        font-size: 1.2em;
        border-radius: 50%;
        border: 1px;
        cursor: pointer;
    }

    hr{
        max-width: 11em;
    }

    ul li a .icon-text-container{
        display: flex;
        gap: .3em;
        align-items: end;
        height: 2em;
    }
    
    ul li a .icon-text-container > span{
        font-size: 10pt;
    }
    
    ul li a .icon-text-container .icon{
        font-size: 14pt;
    }

    h1{
       

    }
    .icon-logo{
        font-weight: bold;
    }

</style>