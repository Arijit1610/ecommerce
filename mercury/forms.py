from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	otp = forms.CharField(label='OTP', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email address already exists.')
		return email

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
