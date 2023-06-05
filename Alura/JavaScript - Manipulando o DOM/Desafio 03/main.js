const lista = document.querySelector("ul");
const botaoMostrar = document.querySelector("button");
const botaoEsconder = document.createElement("button");

botaoEsconder.textContent = "Esconder cores";
document.body.appendChild(botaoEsconder);

botaoMostrar.addEventListener("click", () => {
  lista.style.display = "block";
});

botaoEsconder.addEventListener("click", () => {
  lista.style.display = "none";
});