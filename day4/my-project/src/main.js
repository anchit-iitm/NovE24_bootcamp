import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
// createApp(App).use(router).use(store).use(something).mount('#app')
