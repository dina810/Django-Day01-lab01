from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import json
import os.path



# def index(request):
#     return HttpResponse("<h1>hello world</h1>")

def welcome(request):
    return HttpResponse("<h1>welcome in book store</h1>")


# def welcome(request,books_id):
#     context = {
#             "id":books_id
#         }
#     return render(request,"books/welcome.html",context=context)


# books=[
#         {"id": 1, "name": "Book1", "description": "Book1 decs", "image": ""},
#         {"id": 2, "name": "Book2", "description": "Book2 decs", "image": ""},
#         {"id": 3, "name": "Book3", "description": "Book3 decs", "image": ""},
#         {"id": 4, "name": "Book4", "description": "Book4 decs", "image": ""},
#         {"id": 5, "name": "Book5", "description": "Book5 decs", "image": ""},
#         {"id": 6, "name": "Book6", "description": "Book6 decs", "image": ""}
#
#     ]

####################################################################################################################
# def index(request):
#     return render(request,"books/index.html")

def get_books():
    books = os.path.join(settings.BASE_DIR) + "/books.json"
    with open(books, 'r') as file:
        data = json.load(file)
    return data


def index(request):
    books = get_books()
    context = {
        "books" : books
    }
    return render(request, "books/index.html",context=context)


def get_single_books(request, id):
    books = get_books()
    selected_book = {}
    for book in books:
        if book["id"] == id:
            selected_book = book
    context = {"book" : selected_book}
    return render(request, "books/welcome.html",context=context)