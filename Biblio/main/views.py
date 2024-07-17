from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *

from .forms import *
from .models import *


# Create your views here.


def setcookie(request, response):
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
        response.set_cookie('visit_count', str(visit_count))
    else:
        visit_count = 1
        response.set_cookie('visit_count', str(visit_count))
    return response


def index(req):
    img = MyModel.objects.all()
    response = render(req, 'index.html', {'img': img})
    response = setcookie(req, response)
    return response


def book(req):
    books = Book.objects.all()
    paginator = Paginator(books, 4)
    page = req.GET.get('page')
    books = paginator.get_page(page)

    resp = render(req, 'books.html', {'lbook': books})
    resp = setcookie(req, resp)
    return resp


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


def showcookie(request):
    show = request.COOKIES.get('visit_count')
    if show:
        html = "Hello!<br> Your cookie: {0}<br><br><br> <a href='http://127.0.0.1:8000/del'>Очистить кэш</a>".format(show)
    else:
        html = "Cookie 'visit_count' is not set."
    return HttpResponse(html)


def del_cookie(req):
    html = redirect('home')
    if req.COOKIES.get('visit_count'):
        html.delete_cookie('visit_count')
    return html
