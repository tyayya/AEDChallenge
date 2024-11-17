from flask import Flask, request, render_template, redirect, url_for, send_file
import json
import pathlib
from participant import save_participant
import os

current_directory = os.getcwd()

app = Flask(__name__,template_folder=current_directory,static_folder=os.path.join(current_directory, 'static'))

# Ruta al JSON de participantes
DATA_PATH = os.path.join(current_directory, "data", "datathon_participants.json")

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/datos.html")
def datos():
    return render_template("datos.html")


@app.route("/submit", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Captura los datos enviados por el formulario
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "age": int(request.form["age"]),
            "year_of_study": request.form["year_of_study"],
            "shirt_size": request.form["shirt_size"],
            "university": request.form["university"],
            "dietary_restrictions": request.form["dietary_restrictions"],
            "interests": [interest.strip() for interest in request.form["interests"].split(",")],
            "preferred_role": request.form["preferred_role"],
            "experience_level": request.form["experience_level"],
            "hackathons_done": int(request.form["hackathons_done"]),
            "objective": request.form["objective"],
            "introduction": request.form["introduction"],
            "technical_project": request.form.get("technical_project", ""),
            "future_excitement": request.form.get("future_excitement", ""),
            "fun_fact": request.form.get("fun_fact", ""),
            "preferred_languages": [
                language.strip() for language in request.form["preferred_languages"].split(",")
            ],
            "friend_registration": [],  # Puedes ajustar esto según tus necesidades
            "preferred_team_size": int(request.form["preferred_team_size"]),       
            "availability": {
                slot.strip(): True for slot in request.form["availability"].split(",")
            },  # Simula disponibilidad en todos los horarios
            "programming_skills": {
                skill.strip(): 1 for skill in request.form["programming_skills"].split(",")
            },  # Simula habilidades con nivel básico
            "interest_in_challenges": [
                challenge.strip() for challenge in request.form["interest_in_challenges"].split(",")
            ],
        }

        # Guarda el participante en el JSON
        save_participant(data, path=DATA_PATH)

        # Redirige a la página para buscar equipo
        return redirect(url_for("equipos"))
    
    # Si es un GET, solo renderiza el formulario
    return render_template("datos.html")




# Ruta que renderiza buscar_equipo.html
@app.route("/equipos")
def equipos():
    return render_template("equipos.html")

@app.route('/perfiles.json')
def serve_perfiles():
    return send_file('perfiles.json')

if __name__ == "__main__":
    # Asegúrate de que el archivo JSON existe
    if not pathlib.Path(DATA_PATH).exists():
        with open(DATA_PATH, "w") as f:
            json.dump([], f)
    app.run(debug=True)