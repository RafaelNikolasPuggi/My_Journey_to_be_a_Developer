<template>
  <BoxDeComponente>
    <div class="columns">
      <div class="column is-7">{{ tarefa.descricao || 'Tarefa sem descrição' }}</div>
      <div class="column is-3">
        {{ tarefa.projeto?.nome || 'N/D' }}
      </div>
      <div class="column">
        <CronometroFormulario :tempoEmSegundos="tarefa.duracaoEmSegundos" />
      </div>
    </div>
  </BoxDeComponente>
</template>

<script lang="ts">
import CronometroFormulario from "./CronometroFormulario.vue";
import { defineComponent, PropType } from "vue";
import ITarefa from "@/interfaces/ITarefa";
import BoxDeComponente from "./BoxDeComponente.vue";

export default defineComponent({
  name: "TarefaNoFormulario",
  components: {
    CronometroFormulario,
    BoxDeComponente
},
  props: {
    tarefa: {
      type: Object as PropType<ITarefa>,
      required: true
    }
  }
});
</script>