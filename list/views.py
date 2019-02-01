from django.shortcuts import render
from .models import detail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

def about1(request):
    var = detail.objects.all()
    return render(request,'base1.html',{'det':var})

def details(request,slug):
    a=detail.objects.get(slug=slug)
    return render(request, 'main.html',{'b':a})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('list:about')
    else:
        form=forms.CreateArticle()
    return render(request, 'article_create.html',{'form':form})
