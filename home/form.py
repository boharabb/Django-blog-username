from django import forms
from django.forms import fields
from home.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("name", "isbn", "price", "book_image", "bookdetail")
