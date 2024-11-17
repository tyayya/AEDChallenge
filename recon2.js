// Obtener datos de la API y cargarlos
async function fetchRecommendations() {
    try {
        const response = await fetch('http://127.0.0.1:5000/recommendations'); // Ruta del backend Flask
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const candidates = await response.json();
        loadRecommendations(candidates);
    } catch (error) {
        console.error('Error fetching recommendations:', error);
    }
}

// Carga inicial de las tarjetas
function loadRecommendations(candidates) {
    const container = document.querySelector('.recommendation-container');
    container.innerHTML = ''; // Limpiar cualquier contenido previo

    // Mostrar los candidatos recibidos
    candidates.forEach((candidate, index) => {
        const card = createCard(candidate, index);
        container.appendChild(card);
    });
}

// Crear una tarjeta
function createCard(candidate, index) {
    const card = document.createElement('div');
    card.className = 'recommendation-card';
    card.setAttribute('data-index', index);

    card.innerHTML = `
        <h2>${candidate.name}</h2>
        <p class="age"><strong>Edad:</strong> ${candidate.age}</p>
        <button class="reject-btn">Rechazar</button>
        <p class="intro">${candidate.intro}</p>
    `;

    // Manejar el evento de rechazo
    card.querySelector('.reject-btn').addEventListener('click', () => rejectCandidate(index));

    return card;
}

// Rechazar un candidato
function rejectCandidate(index) {
    // Eliminar al candidato de la lista (para efectos visuales)
    const container = document.querySelector('.recommendation-container');
    const cardToRemove = container.querySelector(`.recommendation-card[data-index="${index}"]`);
    if (cardToRemove) {
        cardToRemove.remove();
    }
}

// Llamar al backend al cargar la página
document.addEventListener('DOMContentLoaded', fetchRecommendations);
