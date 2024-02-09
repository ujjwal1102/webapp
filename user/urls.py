
from django.urls import path, include
# from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
         path('', views.index, name ='index'),
         path('login/',views.user_login,name='login'),
         path('register/',views.register,name='signup'),
         path('chatbot/',views.chatbot,name='chatbot'),
         path('about/',views.about,name="about"),
         path('logout/',LogoutView.as_view(),name='logout'),
]