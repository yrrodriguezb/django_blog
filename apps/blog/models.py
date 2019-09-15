from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


def custom_autor_upload_to(instance, filename):
    try:
        old_instance = Autor.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
    except:
        pass

    return 'autor/{0}/{1}'.format(instance.id, filename)

def custom_post_upload_to(instance, filename):
    try:
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
    except:
        pass
    return 'post/{0}/{1}'.format(instance.id, filename)

def custom_upload_to(instance, filename):
    pass


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    estado = models.BooleanField(default=True, verbose_name='Estado Activo/Inactivo')
    fecha_creacion = models.DateField(verbose_name='Fecha de Creacíon', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
      return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, verbose_name='Nombres')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos')
    facebook = models.URLField(verbose_name='Facebook', null=True, blank=True)
    twitter = models.URLField(verbose_name='Twitter', null=True, blank=True)
    instagram = models.URLField(verbose_name='Instagram', null=True, blank=True)
    web = models.URLField(verbose_name='Web', null=True, blank=True)
    imagen = models.ImageField(upload_to=custom_autor_upload_to, verbose_name='Imagen', null=True, blank=True)
    email = models.EmailField(verbose_name='Correo Electrónico')
    estado = models.BooleanField(default=True, verbose_name='Estado Activo/Inactivo')
    fecha_creacion = models.DateField(verbose_name='Fecha de Creacíon', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0} {1}'.format(self.apellidos, self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=90, verbose_name='Titulo')
    slug = models.SlugField(verbose_name='Slug', unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=110, verbose_name='descripción')
    contenido = RichTextField(default='')
    imagen = models.ImageField(upload_to=custom_post_upload_to, null=True, blank=True, verbose_name='Imagen')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True, verbose_name='Estado Activo/Inactivo')
    fecha_creacion = models.DateField(verbose_name='Fecha de Creacíon', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)


class PQR(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    email = models.EmailField(max_length=150, verbose_name='Correo Electrónico')
    asunto = models.CharField(max_length=100, verbose_name='Asunto')
    mensaje = models.TextField(max_length=1000, verbose_name='Mensaje')
    fecha_creacion = models.DateField(auto_now=True, verbose_name='Fecha de Creacíon')

    class Meta:
        verbose_name = 'Peticiones, Quejas y/o Reclamos'
        verbose_name_plural = 'Peticiones, Quejas y/o Reclamos'

    def __str__(self):
      return "%s <%s>" % (self.asunto, self.email)