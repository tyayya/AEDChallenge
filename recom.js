// Lista simulada de candidatos ordenados por compatibilidad
const candidates = [
    { name: "María Pérez", age: 25, intro: "Desarrolladora full-stack con experiencia en proyectos innovadores." },
    { name: "Carlos Gómez", age: 28, intro: "Ingeniero en IA, experto en algoritmos de optimización." },
    { name: "Lucía Martínez", age: 23, intro: "Diseñadora UX/UI apasionada por crear experiencias intuitivas." },
    { name: "Juan Sánchez", age: 26, intro: "Especialista en ciberseguridad con conocimientos avanzados en redes." },
    { name: "Ana López", age: 27, intro: "Programadora de Python interesada en ciencia de datos." }
];

// Carga inicial de las tarjetas
function loadRecommendations() {
    const container = document.querySelector('.recommendation-container');
    container.innerHTML = ''; // Limpiar cualquier contenido previo

    // Mostrar los primeros 3 candidatos
    const visibleCandidates = candidates.slice(0, 3);
    visibleCandidates.forEach((candidate, index) => {
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
    // Eliminar al candidato de la lista
    candidates.splice(index, 1);

    // Recargar las tarjetas
    loadRecommendations();
}

// Cargar recomendaciones al iniciar la página
document.addEventListener('DOMContentLoaded', loadRecommendations);
