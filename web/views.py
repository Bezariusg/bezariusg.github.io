from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render (request, 'web/home.html')


def librodiario(request):
    response = requests.get('http://127.0.0.1:8000/LibroDiario').json()
    return render(request,'web/librodiario.html', {
        'response':response
    })