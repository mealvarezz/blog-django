from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'), 
    path('create/', views.crear_publicacion, name='crear_publicacion'), 
    path('<int:pk>/', views.detalles_post, name='detalles_post'),  
    path('<int:pk>/edit/', views.editar_publicacion, name='editar_publicacion'), 
    path('<int:pk>/delete/', views.eliminar_post, name='eliminar_post'), 
]