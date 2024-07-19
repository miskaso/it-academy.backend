from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('show/', showLead, name='show'),
    path('<int:pk>',
         views.DetailLead.as_view(), name='details'),
    path('create', addLead, name='add'),

]
