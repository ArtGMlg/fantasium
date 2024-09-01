import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import { store } from './store'
import './assets/index.css'
import 'primeicons/primeicons.css'

createApp(App).use(store).use(router).use(Antd)
  .mount('#app')
