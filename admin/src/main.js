import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Icon } from '@iconify/vue'
import VueApexCharts from "vue3-apexcharts"
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
// createApp(App).component('Icon',Icon).use(VueApexCharts).use(store).use(router).mount('#app')

let app = createApp(App)
app.component('Icon',Icon)
app.use(VueApexCharts)
app.use(VueSweetalert2)
app.use(store)
app.use(router)
app.mount('#app')

