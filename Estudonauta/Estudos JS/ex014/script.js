function carregar() {
    var msg = document.getElementById('msg')    
    var img = document.getElementById('imagem')
    var data = new Date()
   // var hora = data.getHours()
   var hora = 14
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        // Bom dia!
        img.src = 'manha1.png'
        document.body.style.background = '#f6eade'
    } else if (hora >= 12 && hora <= 18) {
        // Boa tarde!
        img.src = 'tarde1.png'
        document.body.style.background = '#923b0d'
    } else {
        // Boa noite!
        img.src = 'noite1.png'
        document.body.style.background = '#166bca'
    }
}