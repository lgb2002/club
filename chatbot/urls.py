from django.conf.urls import url
from chatbot import views

urlpatterns = [
    url(r'^keyboard/',views.keyboard),
    url(r'^message',views.answer),
]