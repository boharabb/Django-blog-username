from os import get_terminal_size
from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from News.models import Blog
from News.form import BlogForm

# Create your views here.


def bloghome(request):
    bloghome = Blog.objects.all()
    context = {"bloghome": bloghome}
    return render(request, "bloghome.html", context)

# def blogkolist(request, user_id):
#     userblog = Blog.objects.get(blogcreator=user_id)
#     return render(request, "usrblog.html", {"userblog":userblog})


def blogdetail(request, blogid):
    fullblog = Blog.objects.filter(pk=blogid)
    context = {"fullblog": fullblog}
    return render(request, "fullblog.html", context)


def addblog(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("news:bloghome"))
    return render(request, "addblog.html", {"form": form})


def editblog(request, blogid):
    blogdetail = get_object_or_404(Blog, id=blogid)
    form = BlogForm(request.POST or None,
                            request.FILES or None,  instance=blogdetail)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("news:bloghome"))
    return render(request, "editblog.html", {"form": form})


def deleteblog(blogid):
    blogdetail = get_object_or_404(Blog, id=blogid)
    blogdetail.delete()
    return HttpResponseRedirect(reverse("news:bloghome"))
