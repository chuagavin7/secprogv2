from django import forms
from users.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    shippingAdd = forms.CharField(max_length=1024, required=True, help_text='Required.')
    billingAdd = forms.CharField(max_length=1024, required=True, help_text='Required.')
    contact_num = forms.CharField(max_length=20, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'shippingAdd', 'billingAdd', 'contact_num', 'password1', 'password2', 'email', )

                