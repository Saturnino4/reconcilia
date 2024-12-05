import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Calendar } from 'v-calendar';

const app = createApp(App);
app.use(store);
app.use(router);
app.component('Calendar', Calendar); // Certifique-se de que o nome do componente está correto
app.mount('#app');


