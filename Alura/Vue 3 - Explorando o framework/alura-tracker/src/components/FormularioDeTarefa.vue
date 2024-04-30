<template>
  <div class="box formulario">
    <div class="columns">
      <div
        class="column is-5"
        role="form"
        aria-label="Formulário para criação de uma nova tarefa"
      >
        <input
          type="text"
          class="input"
          placeholder="Qual tarefa você deseja iniciar?"
          v-model="descricao"
        />
      </div>

      <div class="column is-3">
        <div class="select">
          <select v-model="idProjeto">
            <option value="">Selecione o projeto</option>
            <option
              :value="projeto.id"
              v-for="projeto in projetos"
              :key="projeto.id"
            >
              {{ projeto.nome }}
            </option>
          </select>
        </div>
      </div>

      <div class="column">
        <TemporizadorFormulario @ao-temporizador-finalizar="finalizarTarefa" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import TemporizadorFormulario from "./TemporizadorFormulario.vue";
import { useStore } from "vuex";
import { key } from "@/store";
import { NOTIFICAR } from "@/store/tipo-mutacoes";
import { TipoNotificacao } from "@/interfaces/INotificacao";

export default defineComponent({
  name: "FormularioDeTarefa",
  emits: ["aoSalvarTarefa"],
  components: {
    TemporizadorFormulario,
  },

  data() {
    return {
      descricao: "",
      idProjeto: "",
    };
  },

  methods: {
    salvarTarefa(tempoEmSegundos: number): void {
      const projeto = this.projetos.find((p) => p.id == this.idProjeto);
      if(!projeto) {
        this.store.commit(NOTIFICAR, {
          titulo: 'Ops!', 
          texto: "Selecione um projeto de finalizar",
          tipo: TipoNotificacao.FALHA,
        });
        return;
      }
    },
    finalizarTarefa(tempoDecorrido: number): void {
      this.$emit("aoSalvarTarefa", {
        duracaoEmSegundos: tempoDecorrido,
        descricao: this.descricao,
        projeto: this.projetos.find((proj) => proj.id == this.idProjeto),
      });
      this.descricao = "";
    }
  },

  setup() {
    const store = useStore(key);
    return {
      projetos: computed(() => store.state.projetos),
      store
    };
  },
});
</script>

<style>
.formulario {
  background-color: var(--bg-primario);
  color: var(--texto-primario);
}
</style>
