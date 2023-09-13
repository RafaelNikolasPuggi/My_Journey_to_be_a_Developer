const elemento = document.querySelector("body");
const inputCheck = document.querySelector('#modo-noturno');

inputCheck.addEventListener("click", () => {
    const modo = inputCheck.checked ? 'dark' : 'light';
    elemento.setAttribute('data-bs-theme', modo)
})


// document.querySelector("#btn").addEventListener("click", () => {
// document.body.classList.toggle("dark-mode")
// })