from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('delete/<int:pk>/',views.delete_book, name='delete_book'),
    path('add/', views.add_book , name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('search/', views.search_books, name='search_books'), 
    path('filter/', views.filter_books, name='filter_books'), 
    path('delete_filtered/', views.delete_filtered_books, name='delete_filtered_books'),
]