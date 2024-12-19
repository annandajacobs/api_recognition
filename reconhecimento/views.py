# recognition/views.py
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .utils_add_faces import capture_faces_for_person
from .utils_principal import capture_and_identify_faces

def register_faces(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if not name:
            return JsonResponse({'error': 'Name is required'}, status=400)
        capture_faces_for_person(name)
        return JsonResponse({'message': f'Faces registered for {name}.'})
    return render(request, 'reconhecimento/recognize_faces.html')

def recognize_faces(request):
    if request.method == 'POST':
        capture_and_identify_faces()  # Lógica para iniciar a câmera
        return JsonResponse({'message': 'Face recognition completed.'})
    return render(request, 'reconhecimento/recognize_faces.html')

def reconhecimento_home(request):
    return HttpResponse("Bem-vindo à página de reconhecimento!")
