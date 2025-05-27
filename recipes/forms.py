from django import forms
from .models import Recipe
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RecipeForm(forms.ModelForm):
    def clean_cook_time(self):
        data = self.cleaned_data['cook_time']
        if not data.isdigit():
            raise forms.ValidationError("Timpul de gătire trebuie să conțină doar cifre.")
        return data

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'cook_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titlul rețetei'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrediente'}),
            'cook_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30 minute'}),
        }

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Acest nume de utilizator este deja folosit.")
        return username
