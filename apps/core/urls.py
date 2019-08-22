from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    UserCreateView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserCreateView.as_view(), name='signup'),
]


