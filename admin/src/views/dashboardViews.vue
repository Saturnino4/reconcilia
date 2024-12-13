<template >

    <asideNavBar />
    <section class="right-side">
            <headerNav />
            <section class="main-content">
                 <!-- <b>USER: {{ user.username }} </b> -->
                 <div style="display: flex;flex-direction: column;">
                    <h1> {{ empresa.nome }} </h1>
                    <label for="" style="padding-right: 2em;font-family: monospace;">Trazendo soluções modernas e inovadoras para si.</label>
                 </div>
            </section>
            <!-- <popup /> -->
    </section>
    
</template>

<script>
    import asideNavBar from '@/components/AsideNavBar.vue';
    import headerNav from '@/components/headerNav.vue';
    import { fakeEmpresa } from '@/services/fakeData';
    
    export default {

        components: {
            asideNavBar,
            headerNav,
        },
        data(){
            return{
                user: {},
                empresa: {},
            }
        },

        methods:{
            getEmpresa(){
                this.empresa = fakeEmpresa()
            }
        },
        created(){

            this.getEmpresa()

            try {
                this.user = JSON.parse(localStorage.getItem('userData'))
            } catch (error) {
                console.log(error)
            }
            console.log(this.role);
        }
    };
</script>

<style scoped>


.main-content div{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50vh;
    width: 100%;
    font-size: 2em;
    font-family: 'arial';
    color: #333;
}

.main-content div h1{
    font-family: 'Dancing Script', cursive;
    font-size: 4em;
    color:  var(--secondary_v2);
    text-shadow: 2px 4px 4px #0007;
}
    

</style>
