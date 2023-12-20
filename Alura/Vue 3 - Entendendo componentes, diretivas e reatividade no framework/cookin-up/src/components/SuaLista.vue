<template>
    <section>
            <span class="subtitulo-lg sua-lista-texto">
                Sua lista:
            </span>

            <ul v-if="ingredientes.length" class="ingredientes-sua-lista">
                <li v-for="ingrediente in ingredientes" :key="ingrediente">
                    <Tag :texto="ingrediente" :ativa="true"/>
                </li>
            </ul>

            <p v-else class="paragrafo lista-vazia">
                <img src="../assets/images/icones/lista-vazia.svg" alt="Ícone de pesquisa">
                Sua lista está vazia, selecione ingredientes para iniciar.
            </p>
        </section>
</template>