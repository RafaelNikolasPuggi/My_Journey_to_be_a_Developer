// Texto como uma única string
const emails = ``

// Quebrando a string em linhas
const texto = emails.trim().split('\n');

// Convertendo o objeto em uma string JSON
const jsonString = JSON.stringify(texto, null, 2);

console.log(jsonString);
