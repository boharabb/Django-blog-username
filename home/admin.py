from django.contrib import admin
from home.models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("name","isbn", "price")