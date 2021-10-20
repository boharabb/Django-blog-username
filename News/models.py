from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    blogtitle=models.CharField(max_length=500)
    blogdetail=RichTextField()
    blogcreator=models.ForeignKey(User, on_delete=models.CASCADE)
    blogcreated=models.DateTimeField(auto_now_add=True)
    blogimage=models.FileField(upload_to="BlogImage", null=True, blank=True)

    def __str__(self):
        return self.blogtitle
