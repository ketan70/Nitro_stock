from email import message
from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import render ,redirect
from django.contrib import messages
from matplotlib.style import context
from validate_email import validate_email
from django.urls import reverse
from django.contrib.auth.models import User



# Create your views here.


def main(request):
    return render(request ,"home/home.html")


def signUP(request):
    print("entaer")
    context = {'has_error': False,}
    if request.method == "POST":
        username = request.POST['name_s']
        email = request.POST['email_s']
        Password1 = request.POST['Password_1_s']
        Password2 = request.POST['Password_2_s']

        if len(Password1)<6:
            messages.add_message(request, messages.ERROR,
                                'Password should be at least 6 characters')
            context['has_error'] = True

        if Password1 != Password2:
            messages.add_message(request, messages.ERROR,
                                'Password mismatch')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR, 'Enater a valid address')
            context['has_error'] = True

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email is alredy taken by another one')
            context['has_error'] = True

        if context['has_error']:
            return render(request, "home/login.html")


        user = User.objects.create_user(username,email, Password1)
        user.username = username
        user.email = email
        user.password = Password1
        user.save()


        messages.add_message(request, messages.SUCCESS,
                            'Account Created, You can now Login')

    return render(request, "home/login.html")



def login(request):
    return render(request, "home/login.html")