from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 'bye'
    return render(request, "about.html", {'gretting': 'hello', 'gretting1': a})


def home(request):
    return HttpResponse("This is home page.")
