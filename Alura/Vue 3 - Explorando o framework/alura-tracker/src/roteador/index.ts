import {
  RouteRecordRaw,
  Router,
  createRouter,
  createWebHashHistory,
} from "vue-router";

import Tarefas from "@/views/ParteTarefas.vue";
import Projetos from "@/views/ParteProjetos.vue";

const rotas: RouteRecordRaw[] = [
  {
    path: "/",
    name: "ParteTarefas",
    component: Tarefas,
  },
  {
    path: "/projetos",
    name: "ParteProjetos",
    component: Projetos,
  },
];

const roteador = createRouter({
  history: createWebHashHistory(),
  routes: rotas,
});

export default roteador;
