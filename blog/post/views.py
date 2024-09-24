from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  
            post.save()
            return redirect('lista_publicaciones')
    else:
        form = PostForm()
    return render(request, 'post/crear_post.html', {'form': form})


def lista_publicaciones(request):
    publicaciones = Post.objects.all()  
    return render(request, 'post/ver_post.html', {'posts': publicaciones})


def detalles_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk) 
    return render(request, 'post/detalles_post.html', {'post': publicacion})

@login_required
def editar_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('detalles_post', pk=publicacion.pk)
    else:
        form = PostForm(instance=publicacion)
    return render(request, 'post/crear_post.html', {'form': form})

@login_required
def eliminar_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'post/eliminar_post.html', {'post': publicacion})

def registrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registro/registrar.html', {'form': form})
