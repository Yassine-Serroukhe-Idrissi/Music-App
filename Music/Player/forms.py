from django.forms import ModelForm
from django import forms
from .models import MusicInfo
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class MusicForm(ModelForm):
    class Meta:
        model=MusicInfo
        fields = ['music_aut', 'music_titre', 'music_image', 'music_audio']
        widgets = {
            'music_aut': forms.TextInput(attrs={'class': 'form-control'}),
            'music_titre': forms.TextInput(attrs={'class': 'form-control',}),
            'music_image': forms.FileInput(attrs={'class': 'form-control'}),
            'music_audio': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'music_aut': 'Chanteur',
            'music_titre': 'Titre',
            'music_image': 'Afffiche',
            'music_audio': 'Fichier audio'
        }
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    help_texts = {'username': None,
                  'password1': None,
                  'password2': None}

