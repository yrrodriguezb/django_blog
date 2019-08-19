from django.contrib import admin
from .models import Autor, Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre', 'fecha_creacion', 'estado',)


class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombres', 'apellidos', 'email', 'estado',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )

admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)