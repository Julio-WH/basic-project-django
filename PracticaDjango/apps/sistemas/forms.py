from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

from PracticaDjango.apps.sistemas.models import Empresa
from PracticaDjango.apps.sistemas.utils.constants import DIAL_CODE_COUNTRY_PHONE
from PracticaDjango.apps.sistemas.utils.utils import phone_regex

User = get_user_model()


class RequestDemoForm(forms.Form):

    email = forms.EmailField(
        label='Correo Electrónico', widget=forms.EmailInput(attrs={'placeholder': 'Correo Electrónico',
                                                                   'autocomplete': 'off'}))
    short_company_name = forms.CharField(label="Empresa", widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese el nombre de su Empresa', 'class': 'form-control', 'autocomplete': 'off'}))

    country_code = forms.ChoiceField(label="Código de País", choices=DIAL_CODE_COUNTRY_PHONE, initial=52, required=True,
        widget=forms.Select(attrs={"data-toggle": "select2", "class": "form-control"}))

    telefono = forms.CharField(validators=[phone_regex], label='Teléfono', max_length=14, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ingrese un numéro de teléfono', 'autocomplete': 'off',
        'class': 'form-control'}))


class CustomSignupForm(SignupForm):
    company = forms.CharField(max_length=100, label="Empresa", required=True)

    def clean_company(self):
        company = self.cleaned_data.get('company')

        if Empresa.objects.filter(nombre__iexact=company).exists():
            raise ValidationError("La empresa ya está registrada. Por favor, verifica los datos.")

        return company

    def save(self, request):
        # Llama al método de guardado original para manejar los datos básicos
        company = Empresa.objects.create(nombre=self.cleaned_data['company'])
        data = {}
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        data["company"] = company
        user = User.objects.create_user(username, email, password, **data)

        return user

    def send_confirmation(self, request, email_address, signup):
        # Sobrescribimos el método pero no hacemos nada para evitar el envío
        pass