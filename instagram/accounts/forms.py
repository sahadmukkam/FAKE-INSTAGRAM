from .models import UserAccounts
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Sign_up(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields=['email','firstname','lastname']   
    
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       
       del self.fields['password2']
