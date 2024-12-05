<template>
    <section class="popup-container">
        <header>
            <h1 style="text-align: center;color: transparent;">Pop Up</h1>
        </header>
        <section class="pop-main-contet">
            <slot>

            </slot>
        </section>
    </section>
</template>

<script>
    export default {
        data() {
            return {
                // title: this.$store.state.popUp.title
            }
        },
        components:{

        },
        methods:{
            
        }   
    }
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
        z-index: 11;
    }
    section.popup-container > header{
        display: flex;
        justify-content: center;
        padding: 1em;
    }
    
    .pop-main-contet{
        padding: 1em;
        display: flex;
        justify-content: center;
    }
    
    .pop-main-contet .form-container{
        background-color: #0000ff;
        width: 30em;
        padding-bottom: 3em;
        border-radius: .5em;
        box-shadow: 0px 0px .5em .3em #0003;
    }
    .pop-main-contet .form-container header{
        display: flex;
        justify-content: end;
        /* background-color: red; */
        padding-bottom: 0px;
        padding-top: 1em;
        padding-right: 1em;
    }

    .pop-main-contet form{
        padding: 1em;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 1em;
    }
    .pop-main-contet form input,.pop-main-contet form button, .pop-main-contet form select{
        padding: .3em;
        border: none;
        border-radius: .5em;
        outline: none;
        box-shadow: 0px 0px .2em .2em #0003;
        font-size: 13pt;
    }

    .pop-main-contet form input{
        padding-left: .8em;

    }

    .pop-main-contet form button{
        /* padding: .2em; */
        font-weight: bold;
    }

</style>