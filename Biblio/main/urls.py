from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='regist'),
    path('', index, name='home'),
    path('books/', book, name='books'),
    path('add/', views.add, name='add'),
    path('<int:pk>', views.Dbook.as_view(), name='info'),
    path('detail/author/<str:author>/', author, name='category'),
    path('set/', setcookie, name='cookie'),
    path('show/', showcookie, name='showcookie'),
    path('del/', del_cookie, name='del'),
]
