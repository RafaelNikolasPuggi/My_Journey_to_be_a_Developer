<template>
  <FormularioDeTarefa @aoSalvarTarefa="salvarTarefa" />
  <div class="lista">
    <BoxDeComponente v-if="listaEstaVazia">
      Você não esta muito produtivo hoje.
    </BoxDeComponente>
    <TarefaNoFormulario
      v-for="(tarefa, index) in tarefas"
      :key="index"
      :tarefa="tarefa"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FormularioDeTarefa from "../components/FormularioDeTarefa.vue";
import TarefaNoFormulario from "../components/TarefaNoFormulario.vue";
import ITarefa from "../interfaces/ITarefa";
import BoxDeComponente from "../components/BoxDeComponente.vue";

export default defineComponent({
  name: "App",
  components: {
    FormularioDeTarefa,
    TarefaNoFormulario,
    BoxDeComponente,
  },

  data() {
    return {
      tarefas: [] as ITarefa[],
    };
  },

  computed: {
    listaEstaVazia(): boolean {
      return this.tarefas.length === 0;
    },
  },

  methods: {
    salvarTarefa(tarefa: ITarefa) {
      this.tarefas.push(tarefa);
    },
  },
});
</script>
