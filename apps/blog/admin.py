from django.contrib import admin
from .models import Autor, Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre', 'fecha_creacion', 'estado',)


class AutorAdmin(admin.ModelAdmin):
    list_display_links = ('id', )
    search_fields = ('nombre',)
    list_display = ('id', 'nombres', 'apellidos', 'email', 'estado',)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )
    actions = ['activateStatePost', 'inactivateStatePost']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def activateStatePost(self, request, queryset):
        rows_updated = queryset.update(estado=True)
        if rows_updated > 0:
            self.message_user(request, "Las publicaciones se habilitaron correctamente, filas afectadas: %s" % str(rows_updated))
    activateStatePost.short_description = 'Habilitar publicaiones'

    def inactivateStatePost(self, request, queryset):
        rows_updated = queryset.update(estado=False)
        if rows_updated > 0:
            self.message_user(request, "Las publicaiones se inhabilitaron correctamente, filas afectadas: %s" % str(rows_updated))
    inactivateStatePost.short_description = 'Inhabilitar publicaiones'

admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)