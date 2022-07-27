from django.shortcuts import render
from django.http import HttpResponse
from . models import Team

# Create your views here.
# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return HttpResponse("Python is a programming language")
# def contact(request):
#     return render(request,"contact.html")
# def detail(request):
#     return HttpResponse("Python is a future tech")
# def thanks(request):
#     return render(request,"thanks.html")
def operation(request):
    x=Team.objects.all()
    return render(request,"index.html",{'result':x})
# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,"Result.html",{'addition':add,'subtraction':sub,'multiplication':mult,'division':div})