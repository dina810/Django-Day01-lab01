from django.urls import path
from .views import index
from .views import new
from .views import book
from .views import author


urlpatterns = [
    path('',index , name="home"),
    path('new',new,name="create_book"),
    path('<int:book_id>', book, name="book_info"),
    path('author/<int:author_id>',author,name="author_info")
]
