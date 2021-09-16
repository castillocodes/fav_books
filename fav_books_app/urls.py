from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.show_all),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.show_one),
    path('books/<int:book_id>/update', views.update),
    path('books/<int:book_id>/delete', views.delete),
    path('favorite/<int:book_id>', views.favorite),
    path('unfavorite/<int:book_id>', views.unfavorite),
    path('logout', views.logout),
]