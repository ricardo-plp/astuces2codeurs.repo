from django import forms

from blog.models import Comment
from django.forms import TextInput, Textarea


class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Comment
        fields = ['username','email','body']