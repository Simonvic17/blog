from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'rounded_list'}))
    class Meta:
        model = Post
        fields = [
            'title',
            'postText',
            'category',
            'photo',
            'date_created',
            'date_updated'
            ]
        