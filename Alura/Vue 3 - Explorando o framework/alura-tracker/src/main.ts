import { createApp } from "vue";
import App from "./App.vue";

import "@fortawesome/fontawesome-free/css/all.css";
import roteador from "./roteador";
//npm i --save-dev @fortawesome/fontawesome-free
//https://fontawesome.com/

createApp(App).use(roteador).mount("#app");
