async function listaVideos() {
    const conexao = await fetch ("http://localhost:3000/profile");
    const conexaoConvertida = conexao.json();
    console.log(conexaoConvertida);
}

listaVideos();