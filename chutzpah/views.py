from django.shortcuts import render
from chutzpah.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def rank(request):
	if request.method == "POST":
		name = request.POST.get('name2')
		point = request.POST.get('point2')
		rank = UserRank(user_name=name,user_point=point)
		rank.save()
	ranking = UserRank.objects.all().order_by('user_point')
	return render(request, 'chutzpah/game.html',{'ranking':ranking})

'''
try:
	name1 = request.POST.get('name1')
	try:
		name_exist = UserRank.objects.get(user_name=name1)
		return render(request, 'chutzpah/game.html',{'exist':1})
	except:
		return render(request, 'chutzpah/game.html',{'exist':0})
except:
	name = request.POST.get('name2')
	point = request.POST.get('point2')
	rank = UserRank(user_name=name,user_point=point)
	rank.save()
	ranking = UserRank.objects.all().order_by('user_point')
	return render(request, 'chutzpah/game.html',{'ranking':ranking})
	'''

def game(request):
	ranking = UserRank.objects.all().order_by('-user_point')
	return render(request, 'chutzpah/game.html',{'ranking':ranking})

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