from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index2', views.index2, name='index2'),
	url(r'^123d', views.onetwothreed, name='index'),
	url(r'^automaker', views.automaker, name='index2'),
	url(r'^blender', views.blender, name='index'),
	url(r'^razercutter', views.razercutter, name='index2'),
	url(r'^robox', views.robox, name='index'),
	#url(r'^index2', views.index2, name='index2'),
	url(r'^game', views.game, name='game'),
	url(r'^rank', views.rank, name='rank'),
]