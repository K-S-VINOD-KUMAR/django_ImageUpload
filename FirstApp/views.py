from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.forms import BooksForm
from .models import Books
# Create your views here.

def register(request):
	form = BooksForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		return HttpResponse('Uploaded')
	form = BooksForm()
	return render(request,'FirstApp/register.html',{'form':form})

def show(request):
	data=Books.objects.all()
	return render(request,'FirstApp/show.html',{'data':data})
