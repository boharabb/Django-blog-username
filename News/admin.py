from django.contrib import admin
from News.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blogtitle", "blogcreated", "blogdetail")
