from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
	return HttpResponse('Hello, Welcome Akhila to your world!!!!')
