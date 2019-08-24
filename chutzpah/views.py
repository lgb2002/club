from django.shortcuts import render

# Create your views here.

def game(request):
	return render(request, 'chutzpah/game.html')

def index(request):
	return render(request, 'chutzpah/index.html')

def index2(request):
	return render(request, 'chutzpah/index2.html')

def onetwothreed(request):
	return render(request, 'chutzpah/123d.html')

def blender(request):
	return render(request, 'chutzpah/blender.html')

def razercutter(request):
	return render(request, 'chutzpah/razercutter.html')

def robox(request):
	return render(request, 'chutzpah/robox.html')

def automaker(request):
	return render(request, 'chutzpah/automaker.html')