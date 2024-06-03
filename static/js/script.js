function atualizarInscritos() {
    // Para cada canal, faz uma requisição AJAX para obter os inscritos e atualiza o valor
    Object.keys(channels).forEach(function (channel_name) {
        let url = '/subscribers/' + channel_name;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                let inscritosElement = document.getElementById(channel_name);
                if (inscritosElement) {
                    inscritosElement.innerText = data.subscriber_count;
                }
            })
            .catch(error => console.error('Erro ao atualizar inscritos:', error));
    });

    // Atualiza o total de inscritos
    fetch('/')
        .then(response => response.text())
        .then(html => {
            let parser = new DOMParser();
            let doc = parser.parseFromString(html, 'text/html');
            let totalInscritosElement = doc.getElementById('totalInscritos');
            let totalInscritosValue = totalInscritosElement.innerText;
            document.getElementById('totalInscritos').innerText = totalInscritosValue;
        })
        .catch(error => console.error('Erro ao atualizar total de inscritos:', error));
}

setInterval(atualizarInscritos, 10000); // Atualiza a cada 30 segundos
