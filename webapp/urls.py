from django.contrib import admin
from django.urls import path, include
from user import views as user_view
# from django.contrib.auth import views as auth
# from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    ##### user related path##########################
    path('', include('user.urls')),




]