from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Post, Categoria
from .forms import EditPostForm, PQRForm


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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'core:login'
    model = Post
    context_object_name = 'post'
    form_class = EditPostForm
    template_name = 'blog/editar_post.html'

    def get_success_url(self):
        return reverse_lazy('blog:editar_post', kwargs={ 'pk': self.object.id }) + "?ok=true"


class PQRView(CreateView):
    form_class = PQRForm
    template_name = 'blog/contact.html'
    success_url = reverse_lazy('blog:PQR')

    def get_success_url(self):
        return reverse_lazy('blog:PQR') + "?ok=true"

    def form_valid(self, form):
        self.enviar_email(form)
        return super(PQRView, self).form_valid(form)

    def enviar_email(self, form):
        subject = form.cleaned_data['asunto']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['mensaje']

        try:
            send_mail(subject, message, from_email, ['django.yrrodriguezbgmail.com'])
        except:
            pass
