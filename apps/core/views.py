# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordResetView, 
    PasswordResetConfirmView,
    PasswordResetDoneView
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import FormView, RedirectView, CreateView
from .forms import CreateUserForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/auth/login.html"
    success_url = reverse_lazy("blog:home")
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next', None)

        if not url:
            url = super(LoginView, self).get_success_url()
        
        return url


class LogoutView(RedirectView):
    pattern_name = 'core:login'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class PasswdChangeView(PasswordChangeView):
    template_name = "core/auth/password_change.html"
    success_url = reverse_lazy("password_change")

    def get_success_url(self):
        self.success_url = str(self.success_url + "?success")
        return super(PasswdChangeView, self).get_success_url()


class PasswdResetView(PasswordResetView):
    template_name = "core/auth/password_reset.html"
    success_url = reverse_lazy('password_reset')

    def get_success_url(self):
        self.success_url = str(self.success_url + "?success")
        return super(PasswdResetView, self).get_success_url()


class PasswdResetConfirmView(PasswordResetConfirmView):
    template_name = "core/auth/password_reset_confirm.html"
    success_url = reverse_lazy('password_reset_complete')


class PasswdResetDoneView(PasswordResetDoneView):
    template_name = "core/auth/password_reset_complete.html"


class UserCreateView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "core/auth/register.html" 
    success_url = reverse_lazy('core:login')


def _404(request, exception):
    context = { 'code': 404, 'message': 'Página No Encontrada' }
    return render(request, "core/http/error.html", context)


def _500(request):
    context = { 'code': 500, 'message': 'Error Interno de Servidor' }
    return render(request, 'core/http/error.html', context)