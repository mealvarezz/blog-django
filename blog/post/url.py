from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('create/', views.crear_post, name='crear_post'),  
    path('<int:pk>/', views.detalles_post, name='detalles_post'),
    path('<int:pk>/edit/', views.editar_post, name='editar_publicacion'),
    path('<int:pk>/delete/', views.eliminar_post, name='eliminar_post'),

    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


