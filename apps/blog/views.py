from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Post, Categoria


class PostBaseListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    

    def get_queryset(self):
        search = self.request.GET.get('q', None)
        if search:
            return Post.objects.filter(
                (Q(titulo__icontains=search) | Q(descripcion__icontains=search))
                & Q(estado=True)
            )
        return Post.objects.filter(estado=True)

    def get_posts_by_category(self, category_name):
        search = self.request.GET.get('q', None)
        categoria = self.__get_category_by_name(category_name)

        if search:
            return Post.objects.filter(
                (Q(titulo__icontains=search) | Q(descripcion__icontains=search))
                & Q(estado=True) & Q(categoria=categoria)
            )

        return Post.objects.filter(estado=True, categoria=categoria).order_by('categoria')

    def __get_category_by_name(self, name):
        return get_object_or_404(Categoria, nombre=name)


class PostsListView(PostBaseListView):
    template_name = 'blog/index.html'
      

class GeneralesListView(PostBaseListView):
    template_name = 'blog/generales.html'

    def get_queryset(self):
        return self.get_posts_by_category('General')
    

class ProgramacionListView(PostBaseListView):
    template_name = 'blog/programacion.html'

    def get_queryset(self):
        return self.get_posts_by_category('Programación')


class TutorialesListView(PostBaseListView):
    template_name = 'blog/tutoriales.html'

    def get_queryset(self):
        return self.get_posts_by_category('Tutoriales')


class TecnologiaListView(PostBaseListView):
    template_name = 'blog/tecnologia.html'

    def get_queryset(self):
        return self.get_posts_by_category('Tecnología')


class VideoJuegosListView(PostBaseListView):
    template_name = 'blog/video_juegos.html'

    def get_queryset(self):
        return self.get_posts_by_category('Video Juegos')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detalle_post.html'