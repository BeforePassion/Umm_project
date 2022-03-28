from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'credit/test.html')

def page(request,page):
    return redirect('/credit')
