from crispy_forms.helper import FormHelper
from django.db.models.base import Model
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	last_name = forms.CharField(max_length=200)
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "last_name", "password2"]