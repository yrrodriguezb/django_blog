from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


ERROR_MESSAGE_USER = { 
    'required': 'El usuario es requerido.',
    'unique': 'El usuario ya esta registrado.',
    'invalid': 'El nombre de usuario es incorrecto.'    
}

ERROR_MESSAGE_PASSWORD = { 
    'required': 'La contraseña es requerida.' 
}

ERROR_MESSAGE_EMAIL = {
    'invalid': 'Ingrese un correo valido.'
}  


class AuthenticationUserForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=20, error_messages = ERROR_MESSAGE_USER)
    email = forms.CharField(error_messages= ERROR_MESSAGE_EMAIL)

    class Meta:
        model = User

        fields = (
           'username',
           'email',
           'password1',
           'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('El email ya se encuentra registrado.')
        return email
