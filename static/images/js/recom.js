// Lista simulada de candidatos ordenados por compatibilidad

async function loadCandidates() {
    try {
        const response = await fetch('perfiles.json');
        const perfilesData = await response.json();
        
        const candidates = perfilesData.map(perfil => ({
            name: perfil[0],
            age: perfil[1],
            intro: perfil[2]
        }));

        return candidates;
    } catch (error) {
        console.error('Error loading candidates:', error);
        return [];
    }
}

// Initialize cards when document loads
document.addEventListener('DOMContentLoaded', async () => {
    const candidates = await loadCandidates();
    const container = document.querySelector('.recommendation-container');
    
    candidates.forEach((candidate, index) => {
        const card = createCard(candidate, index);
        container.appendChild(card);
    });
});

function createCard(candidate, index) {
    const card = document.createElement('div');
    card.className = 'recommendation-card';
    card.setAttribute('data-index', index);

    card.innerHTML = `
        <h2>${candidate.name || 'Unknown'}</h2>
        <p class="age"><strong>Age:</strong> ${candidate.age || 'N/A'}</p>
        <button class="reject-btn">Reject</button>
        <p class="intro">${candidate.intro || 'No introduction available.'}</p>
    `;

    card.querySelector('.reject-btn').addEventListener('click', () => {
        card.remove();
    });

    return card;
}
