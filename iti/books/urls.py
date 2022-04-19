from django.urls import path
from .views import index,get_single_books
urlpatterns = [
    path('',index),
    # path('<int:books_id>',get_single_books),
    path('<int:id>',get_single_books),

]