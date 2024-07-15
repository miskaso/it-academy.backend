from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.


def index(req):
    img = MyModel.objects.all()
    return render(req, 'index.html', {'img': img})


def book(req):

    books = Book.objects.all()
    paginator = Paginator(books, 4)
    page = req.GET.get('page')
    books = paginator.get_page(page)

    return render(req, 'books.html', {'lbook': books})


@login_required
def add(req):
    if req.method == 'POST':
        form = AddBookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookForm

    return render(req, 'create.html', {'add': form})


class Dbook(DetailView):
    model = Book
    template_name = 'info.html'
    context_object_name = 'detail'


def author(req, author):
    search = Book.objects.filter(author=author)
    return render(req, 'author.html', {'search': search, 'author': author})


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = RegisterForm()

    return render(req, 'registration/register.html', {'reg': form})
