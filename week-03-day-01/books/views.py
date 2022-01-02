from django.shortcuts import render

from books.models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()  # All the book objects of Book model

    # # author__name gives the name of the author of the book
    # # __iexact = Case-insensitive exact match
    # books = Book.objects.filter(author__name__iexact="john doe")

    context_dict = {"books": books}

    return render(request, "books/index.html", context=context_dict)
