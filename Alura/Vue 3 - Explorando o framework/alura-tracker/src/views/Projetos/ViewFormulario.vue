<template>
  <section>
    <form @submit.prevent="salvar">
      <div class="field">
        <label for="nomeDoProjeto" class="label"> Nome do Projeto </label>
        <input
          type="text"
          class="input"
          v-model="nomeDoProjeto"
          id="nomeDoProjeto"
        />
      </div>
      <div class="field">
        <button class="button" type="submit">Salvar</button>
      </div>
    </form>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useStore } from "@/store";
import { ALTERA_PROJETO, ADICIONA_PROJETO } from "@/store/tipo-mutacoes";
import { TipoNotificacao } from "@/interfaces/INotificacao";
import notificador from "@/hooks/notificador";

export default defineComponent({
  name: "ViewFormulario",

  props: {
    id: {
      type: String,
    },
  },

  //mixins: [notificacaoMixin],

  mounted() {
    if (this.id) {
      const projeto = this.store.state.projetos.find(
        (proj) => proj.id == this.id
      );
      this.nomeDoProjeto = projeto?.nome || "";
    }
  },

  data() {
    return {
      nomeDoProjeto: "",
    };
  },

  methods: {
    salvar() {
      if (this.id) {
        this.store.commit(ALTERA_PROJETO, {
          id: this.id,
          nome: this.nomeDoProjeto,
        });
      } else {
        this.store.commit(ADICIONA_PROJETO, this.nomeDoProjeto);
      }

      this.nomeDoProjeto = "";
      this.$router.push("/ViewProjetos");
      this.notificar(TipoNotificacao.SUCESSO, 'Excelente', 'O projeto foi cadastrado com sucesso!')
    },    
  },
  setup() {
    const store = useStore();
    const { notificar } = notificador();
    return {
      store,
      notificar
    };
  },
});
</script>
