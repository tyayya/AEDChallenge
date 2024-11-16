from django.shortcuts import render
from django.http import JsonResponse
import os
import json

def form_view(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Validar datos
        if not name or not email:
            return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)

        # Ruta del archivo JSON
        file_path = os.path.join('data.json')

        # Leer datos existentes o inicializar lista vacía
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        # Agregar los nuevos datos
        new_data = {'name': name, 'email': email}
        data.append(new_data)

        # Guardar datos actualizados en el archivo JSON
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        return JsonResponse({'message': 'Datos guardados correctamente'})

    # Renderizar el formulario
    return render(request, 'myapp/form.html')
