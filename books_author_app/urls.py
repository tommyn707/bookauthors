from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('create_books', views.create_books, name='create_books'),
    path('view/<int:id>', views.view, name='view'),
    # path('edit_movie/<int:id>', views.edit_movie, name='edit_movie'),
    # path('add_actor/<int:id>', views.add_actor, name='add_actor'),
    # path('actor/<int:id>', views.show_actor, name='show_actor'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
    path('authors', views.authors, name='authors'),
]