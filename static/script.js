// Al trabajar con funciones asincronas - Promises - Promesas
async function enviarMensaje() {
    let input = document.getElementById("Mensaje");
    let chat = document.getElementById("chat");
    let mensaje = input.value;

    if (mensaje.trim() === "") {
        return;
    }

    // Burbuja del usuario
    chat.innerHTML += `
        <div class="mensaje usuario">
            <strong>Vos:</strong><br>
            ${mensaje}
        </div>
    `;

    const respuesta = await fetch("/consulta", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            mensaje: mensaje
        })
    });

    const datos = await respuesta.json();

    // Burbuja del bot
    chat.innerHTML += `
        <div class="mensaje bot">
            <strong>Bot:</strong><br>
            ${datos.respuesta}
        </div>
    `;

    input.value = "";
    chat.scrollTop = chat.scrollHeight;
}

function ponerTexto(texto) {
    document.getElementById("Mensaje").value = texto;
}
function limpiarChat() {
    document.getElementById("chat").innerHTML = "";
}





