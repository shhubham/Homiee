from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse('about')

def homepage(request):
    #return HttpResponse('This is homepage')
    return render(request,'base1.html')
