from django.shortcuts import render  , redirect , get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib import messages

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html',{'books': books})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'deleted successfully')
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'add successfully')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'book_list.html', {'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'edit successfully')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def filter_books(request):
    price = request.GET.get('price')
    date = request.GET.get('date')
    books = Book.objects.all()

    if price:
        books = books.filter(price__lte=price)
    if date:
        books = books.filter(publication_date__gte=date)

    return render(request, 'book_list.html', {'books': books})

def delete_filtered_books(request):
    price = request.GET.get('price')
    date = request.GET.get('date')
    books = Book.objects.all()

    if price:
        books = books.filter(price__lte=price)
    if date:
        books = books.filter(publication_date__gte=date)

    if request.method == 'POST':
        books.delete()
        messages.success(request, 'deleted successfully')
        return redirect('book_list')

    return render(request, 'delete_filtered_books.html', {'books': books})


