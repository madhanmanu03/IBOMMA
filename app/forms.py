from django import forms
from app.views import *


class UserMF(forms.ModelForm):
    model=User
    fields=['username','email','password']
    widgets={'password':forms.passwordInput}
    help_texts={'username':''}

class ProfileMF(forms.ModelForm):
    model=Profile
    fields=['address','profile_pic']
