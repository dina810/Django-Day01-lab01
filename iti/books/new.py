from django.shortcuts import render
from django.http import HttpResponse

Create your views here.
def index(request):
    return render(request,"books/index.html")

import json
import os.path

from django.conf import settings
from django.shortcuts import render



# Create your views here.

def get_books():
    books = os.path.join(settings.BASE_DIR) + "/books.json"
    with open(books, 'r') as file:
        data = json.load(file)
    return data


def index(request):
    books=get_books()
    context={
        "books":books
    }
    return render(request, "books/index.html",context=context)


def get_single_books(request, id):
    books=get_books()
    selected_book={}
    for book in books:
        if book["id"] == id:
            selected_book=book
    context={"book":selected_book}
    return render(request, "books/book-details.html",context=context)