<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .model import Post
from .forms import PostForm

# Create your views here.

=======
from django.shortcuts import render, redirect, get, get_list_or_404
from .models import Post
from .forms import PostForm 

# Create your views here.
>>>>>>> e5ff280 (creacion del formulario)
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
<<<<<<< HEAD
            post.autor = request.user
            post.save()
            return redirect('lista_publicaciones')
        else:
            form = PostForm()
        return render(request, 'post/post_formulario.html', {'form': form})
    
def lista_publicaciones(request):
    publicaciones = Post.object.all()
    return render(request,'post/crear_post.html', {'post':publicaciones})

def detalles_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk) 
    return render(request, 'post/detalles_post.html', {'post': publicacion})

def editar_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.metod =="POST":
        form = PostForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
        else:
            form = PostForm(instance=publicacion)
        return render(request, 'post/crear_post.html', {'form':form})

def eliminar_post(request, pk):
    publicacion = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        publicacion.delete()
        return redirect(request, 'post/eliminar_post.html', {'post' : publicacion})        
=======
            post.autor



>>>>>>> e5ff280 (creacion del formulario)
