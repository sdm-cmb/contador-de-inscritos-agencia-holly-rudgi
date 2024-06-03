// Função para animar o contador de inscritos
function animateCounter(targetElement, start, end, duration) {
    let range = end - start;
    let current = start;
    let increment = end > start ? 1 : -1;
    let stepTime = Math.abs(Math.floor(duration / range));
    let timer = setInterval(function () {
        current += increment;
        targetElement.innerText = `Total ${current}`;
        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}

// Exemplo de uso: 
let totalCounter = document.getElementById('totalCounter');
animateCounter(totalCounter, 0, {total_inscritos}, 2000); // Substitua {{total_inscritos}} pelo valor atual
