from django.urls import path
from . import views

urlpatterns=[
    path('master',views.user_master,name='master1'),
    path('home',views.user_home,name='home1'),
    path('about',views.user_about,name='about1'),
    path('contact',views.user_contact,name='contact1'),
]