from django.urls import path
from home.views import homeviews, add_book, edit_book, delete_book

app_name = "home"
urlpatterns = [
    path("home", homeviews, name="home"),
    path("add_book", add_book, name="addbook"),
    path("edit_book/<int:book_id>", edit_book, name="editbook"),
    path("delete_book/<int:book_id>", delete_book, name="deletebook"),
]
