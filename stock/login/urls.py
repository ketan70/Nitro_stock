from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='main'),
    path('signUP',views.signUP, name='signUP'),
    path('login',views.login, name='login'),
]
