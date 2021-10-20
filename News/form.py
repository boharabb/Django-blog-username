from django import forms
from django.db import models
from django.forms import fields
from django.forms import widgets
from News.models import Blog
from django.forms.widgets import Widget


class BlogForm(forms.ModelForm):
    blogdetail = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control mt-2" }))
    # blogimage = forms.FileField(widget=forms.FileField(attrs={"class": "form-control" }))
    class Meta:
        model = Blog
        fields = ("blogtitle", "blogdetail", "blogcreator", "blogimage")
        # widgets = {
        #     "blogtitle": forms.TextInput(attrs={"class": "form-control mt-2"}),
        #     "blogcreator": forms.Select(attrs={"class": "form-control mt-2"}),

        # }
