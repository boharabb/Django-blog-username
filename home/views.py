from django.shortcuts import render, reverse, get_object_or_404
from home.models import Book
from django.http import HttpResponseRedirect
from home.form import BookForm
from userprofile.models import profile

# Create your views here.


def homeviews(request):
    book_list = Book.objects.all()
    context = {"book_list": book_list}
    return render(request, "home.html", context)


def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home:home"))
    return render(request, "addform.html", {"form": form})


def edit_book(request, book_id):
    bookedit = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None,
                    request.FILES or None, instance=bookedit)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("home:home"))
    return render(request, "editbookform.html", {"editbookform": form})


def delete_book(request, book_id):
    bookdelete = get_object_or_404(Book, id=book_id)
    bookdelete.delete()
    return HttpResponseRedirect(reverse("home:home"))
