from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(forms.Form):
    email = forms.EmailField(label="user_email", required=True)
    wachtwoord = forms.CharField(label="user_wachtwoord",widget=forms.PasswordInput,required=True)
    

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label="Gebruikersnaam",
        widget=forms.TextInput(attrs={"autofocus":True})
    )
    
    password = forms.CharField(
        label="Wachtwoord",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

