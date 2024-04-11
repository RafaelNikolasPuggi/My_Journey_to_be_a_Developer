import {
  RouteRecordRaw,
  createRouter,
  createWebHashHistory,
} from "vue-router";

import Tarefas from "@/views/ViewTarefas.vue";
import ViewFormulario from "@/views/Projetos/ViewFormulario.vue";
import ListaProjetos from "@/views/Projetos/ListaProjetos.vue";
import ViewProjetos from "@/views/ViewProjetos.vue";

const rotas: RouteRecordRaw[] = [
  {
    path: "/",
    name: "ViewTarefas",
    component: Tarefas,
  },

  {
    path: '/ViewProjetos',
    component: ViewProjetos,
    children: [
      {
        path: "",
        name: "ListaProjetos",
        component: ListaProjetos,
      },
      {
        path: "novo",
        name: "Novo projeto",
        component: ViewFormulario,
      },
      {
        path: ":id",
        name: "Editar projeto",
        component: ViewFormulario,
        props: true
      }
    ]
  }
  
];

const roteador = createRouter({
  history: createWebHashHistory(),
  routes: rotas,
});

export default roteador;
