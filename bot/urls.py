from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
	path('login/', views.userLogin, name='login'),
	path('register/', views.register, name='register'),
	path('logout/', views.userLogout, name='logout'),
	path('profile/', views.profile, name='profile'),




]