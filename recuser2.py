from flask import Flask, jsonify
from simplify import load_participants
from algoritme_graf import crear_grafo, conexiones_amigos, conexiones_preferencias
from recomendaciones import recommend

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    participants = load_participants()
    id_usuari = participants[-1].id
    G = crear_grafo(participants)

    ids_recomendados = recommend(id_usuari, G)

    perfiles = []
    for recomendado in ids_recomendados:
        for participant in participants:
            if participant.id == recomendado:
                perfiles.append({
                    "name": participant.name,
                    "age": participant.age,
                    "intro": participant.introduction
                })

    return jsonify(perfiles)

if __name__ == '__main__':
    app.run(debug=True)
