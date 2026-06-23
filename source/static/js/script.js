// Seleciona os elementos do HTML
const inputFoto = document.getElementById("foto-usuario");
const previewFoto = document.getElementById("preview-foto");

// Quando o usuário escolher uma imagem
inputFoto.addEventListener("change", function () {

    const arquivo = this.files[0];

    // Verifica se selecionou algum arquivo
    if (!arquivo) {
        return;
    }

    // Verifica se é uma imagem
    if (!arquivo.type.startsWith("image/")) {
        alert("Selecione apenas imagens.");
        return;
    }

    // Cria leitor de arquivo
    const leitor = new FileReader();

    leitor.onload = function (evento) {

        // Atualiza a foto na tela
        previewFoto.src = evento.target.result;

    };

    leitor.readAsDataURL(arquivo);

});