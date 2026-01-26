from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="Кто вы?",
        error_messages={
            'required': _("Пожалуйста, выберите вашу роль."),
        }
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

        error_messages = {
            'username': {
                'required': _('Введите имя пользователя.'),
                'unique': _('Это имя уже занято.'),
            },
            'password1': {
                'required': _('Введите пароль.'),
                'min_length': _('Пароль должен быть не менее 3 символов.'),
                'too_short': _('Введённый пароль слишком короткий. Он должен состоять из как минимум 30 символов.')
            },
            'password2': {
                'required': _('Подтвердите пароль.'),
                'min_length': _('Пароль должен быть не менее 3 символов.'),
                'match': _('Пароли не совпадают.'),
            }
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Пароли не совпадают.'))
        return password2