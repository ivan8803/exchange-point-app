import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import 'bootstrap/dist/js/bootstrap.js'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')