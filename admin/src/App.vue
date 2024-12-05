<template>
    <main>
        <!-- <AsideNavBar /> -->
        <RouterView />
        <!-- <BarChart /> -->
    </main>
    
</template>


<script>
    import './styles/index.css'
    import './styles/frame.css'
    // import AsideNavBar from './components/AsideNavBar.vue';
// import { mapMutations, mapActions, mapGetters } from 'vuex';

    export default {
        name: 'App',
        
        components: {
            // AsideNavBar
        },

        methods: {
            


        },

        computed: {
           
        },

        created() {
            // this.fetchUser()
            // this.setLoggedUser()
        }
    }
    
</script>



<style>
    *{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    :root{
        --primary: #c4c4c4;
        --secondary: #011753;
        --secondary-2: #013253ec;
        --primary: #c4c4c4;

        --white-1: #fff;
        --white-2: #fff9;
    }
</style>
