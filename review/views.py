from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'review/test.html')