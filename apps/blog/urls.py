from django.urls import path

from .views import (
    PostsListView,
    GeneralesListView,
    ProgramacionListView, 
    TutorialesListView,
    TecnologiaListView, 
    VideoJuegosListView,
    PostDetailView
)

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    path('generales/', GeneralesListView.as_view(), name='generales'),
    path('programacion/', ProgramacionListView.as_view(), name='programacion'),
    path('tecnologia/', TecnologiaListView.as_view(), name='tecnologia'),
    path('tutoriales/', TutorialesListView.as_view(), name='tutoriales'),
    path('video-juegos/', VideoJuegosListView.as_view(), name='video_juegos'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='detalle_post'),
]


