from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import Book

def index(request):
    return render(request, 'myapp/index.html')

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
