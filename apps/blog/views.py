from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

def home(request):
    posts = Post.objects.filter(estado=True)
    context = {
      'posts': posts
    }
    return render(request, 'blog/index.html', context)

def generales(request):
    posts = Post.objects.filter(
      estado=True,
      categoria__nombre=Categoria.objects.get(nombre='General')
    )
    context = {
      'posts': posts
    }
    return render(request, 'blog/generales.html', context)

def programacion(request):
    posts = Post.objects.filter(
      estado=True,
      categoria__nombre=Categoria.objects.get(nombre='Programación')
    )
    context = {
      'posts': posts
    }
    return render(request, 'blog/programacion.html', context)

def tutoriales(request):
    posts = Post.objects.filter(
      estado=True,
      categoria__nombre=Categoria.objects.get(nombre='Tutoriales')
    )
    context = {
      'posts': posts
    }
    return render(request, 'blog/tutoriales.html', context)

def tecnologia(request):
    posts = Post.objects.filter(
      estado=True,
      categoria__nombre=Categoria.objects.get(nombre='Tecnología')
    )
    context = {
      'posts': posts
    }
    return render(request, 'blog/tecnologia.html', context)

def video_juegos(request):
    posts = Post.objects.filter(
      estado=True,
      categoria__nombre=Categoria.objects.get(nombre='Video Juegos')
    )
    context = {
      'posts': posts
    }
    return render(request, 'blog/video_juegos.html', context)

def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = { 'post': post }
    return render(request, 'blog/detalle_post.html', context)