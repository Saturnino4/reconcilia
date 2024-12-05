<template>
    <asideNavBar />
    <section class="right-side">
        <headerNav />
        <section class='main-content'>
            <header class="crud-title">
                <h2>Recibo</h2>
            </header>
                <div id="recibo-container">
                    <ul id="recibo">
                        <li>
                            <span> <p>item 001</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 0012</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 00132</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 0013</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 0013</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 003</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 004</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 005</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 00167</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 007</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 008</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p>item 0019</p> <span>------------------------------------------------------------</span> <b>$200</b> </span>
                            <span> <p id="total">Total</p> <span>------------------------------------------------------------</span> <b>$65949</b> </span>
                            

                        </li>
                    </ul>
                </div>
                <button @click="imprimirRecibo">Imprimir</button>
        </section>
    </section>

</template>
  
<script>
    import asideNavBar from '@/components/AsideNavBar.vue';
    import headerNav from '@/components/headerNav.vue';
    import html2pdf  from 'html2pdf.js';
    export default { 
 
        components: {   
            asideNavBar, 
            headerNav
       }, 
       data(){
           return{ 
           } 
       }, 
       methods: {  

        imprimirRecibo() {
            const element = document.getElementById('recibo-container');
            const options = {
                margin: 0.5, // Ajuste as margens conforme necessário
                filename: 'recibo.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: [130, 170], orientation: 'portrait' } // Formato personalizado para recibo
            };
            html2pdf().set(options).from(element).save();
        }

       }, 
       created(){
       } 

   }
</script>
 
<style scoped>
   .main-content{ 
    
    height: 100dvh; 
   } 

   .main-content ul{
    background-color: rgba(145, 145, 145, 0.678);
    padding: 1em;
    max-width: 20em;
   }

   button{
        padding: .5em;
        font-size: 1em;
        font-weight: bold;
        background-color: rgba(8, 89, 139, 0.858);
        color: #fffa;
        border-radius: .5em;
   }

   .main-content ul,li{
     display: flex;
     flex-direction: column;
   }

   li > span{
       display: flex;
       justify-content: space-between;
       
    }
    li > span:last-child{
        padding-top: 2em;
    }

    li > span > p{
        font-size: 1.2em;
        z-index: 2;
        text-wrap: nowrap;
        padding-right: .5em;
    }
    li p#total{
        font-weight: bold;
    }
    
    li > span > b{
        padding-left: .5em;
    }


    li > span > span{
        font-size: 1.2em;
        z-index: 1;
        text-wrap: nowrap;
        overflow: hidden;
        opacity: 0.2;
    }
    
   #recibo-container {
    padding-top: 2em;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60%;
    width: 100%;

    
}

#recibo {
    text-align: center;
    width: 100%;
    padding: 2em;
}
</style> 