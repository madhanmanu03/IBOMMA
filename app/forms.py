from django import forms
from app.models import *


class UserMF(forms.ModelForm):
    model=User
    fields=['username','email','password']
    widgets={'password':forms.PasswordInput}
    help_texts={'username':''}

class ProfileMF(forms.ModelForm):
    model=Profile
    fields=['address','profile_pic']
