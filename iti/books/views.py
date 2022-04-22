from pydoc import describe
from django.shortcuts import render , get_object_or_404
import json,os
from multiprocessing import context
from django.http import HttpResponse
from .models import Book
from .models import Author



# Create your views here.
def index(request):

    context = {
        "books": Book.objects.all()

    }
    return render(request,"books/index.html", context=context)

def book(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    context= {
        "book":book,
        "img":os.path.basename(book.img.__str__())
    }

    
    return render(request,"books/book.html", context=context)

def author(request,author_id):
    books=Book.objects.filter(author=author_id).all()
    context= {
        "author":books[0].author,
        "books":books
    
    }
    return render(request,"books/author.html", context=context)
    
def any(request):
    return HttpResponse("Any") 
    

def new(request):
    return render(request, books/book_create.html)