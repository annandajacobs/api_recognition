from django.urls import path
from .views import register_faces, recognize_faces, reconhecimento_home

urlpatterns = [
    path('', reconhecimento_home, name='reconhecimento_home'),
    path('register_faces/', register_faces, name='register_faces'),
    path('recognize_faces/', recognize_faces, name='recognize_faces'),
]
