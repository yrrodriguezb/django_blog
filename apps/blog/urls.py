from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, 
    generales, 
    programacion, 
    tecnologia, 
    tutoriales, 
    video_juegos,
    detalle_post
)

urlpatterns = [
    path('', home, name='home'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('video-juegos/', video_juegos, name='video_juegos'),
    path('post/<slug:slug>/', detalle_post, name='detalle_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


