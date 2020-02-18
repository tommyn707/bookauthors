# other imports
from django.shortcuts import render, redirect
from books_author_app.models import *
# show all of the data from a table
def index(request):
    context = {
    	"books": books.objects.all()
    }
    return render(request, "index.html", context)


def create_books(request):
    books.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect("/")

def view(request, id):
    context ={
        "books":books.objects.get(id=id),
        # "authors":authors.objects.get(id=id)
    }
    return render(request, "view.html", context)

# def authors(request):
#     context = {
#         "authors": authors.objects.all()
#     }
#     return render(request, "author.html", context)
    
def delete_book(request, id):
    book = books.objects.get(id=id)
    book.delete()
    return redirect("/")
