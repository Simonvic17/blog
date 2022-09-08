from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UsersCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    pic = forms.FileField(widget=forms.FileInput(attrs={'class': 'rounded_list'}))
    
    class Meta:
        model = User
        fields = ["first_name", "last_name","email", 'pic']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = UserAccount
#         fields = ['pic']



class UserRegister(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = {"first_name", "last_name", 'email','password1', 'password2'}