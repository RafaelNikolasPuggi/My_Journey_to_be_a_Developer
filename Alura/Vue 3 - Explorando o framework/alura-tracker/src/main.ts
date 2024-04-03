import { createApp } from "vue";
import App from "./App.vue";

import "@fortawesome/fontawesome-free/css/all.css";
import roteador from "./roteador";
import { key, store } from "./store";
//npm i --save-dev @fortawesome/fontawesome-free
//https://fontawesome.com/

createApp(App)
.use(roteador)
.use(store, key)
.mount("#app");