from django import forms
from .models import empmodel
from django.contrib.auth.models import User

class empform(forms.ModelForm):
    class Meta:
        model = empmodel
        fields = '__all__'

class signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']