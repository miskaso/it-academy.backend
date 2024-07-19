from django.shortcuts import render, redirect
from django.views.generic import *

from .forms import GoLead
from .models import *


# Create your views here.


def home(req):
    content = Leed.objects.all()
    return render(req, 'index.html', {'content': content})


def showLead(req):
    content = Leed.objects.all()
    return render(req, 'leeds.html', {'content': content})


class DetailLead(DetailView):
    model = Leed
    template_name = 'leed.html'
    context_object_name = 'detail'


def addLead(req):
    if req.method == 'POST':
        form = GoLead(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoLead()
    return render(req, 'add.html', {'form': form})
