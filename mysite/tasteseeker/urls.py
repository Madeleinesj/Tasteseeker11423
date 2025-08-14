# tasteseeker/urls.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'tasteseeker'

urlpatterns = [
    path('', views.Index, name='home'),
    path('index/', views.Index, name='Index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('seeker_home/', views.seeker_home, name='seeker_home'),
    path('seeker_createentry/', views.seeker_createentry, name='seeker_createentry'),
    path('seeker_drink_list/', views.seeker_drink_list, name='seeker_drink_list'),
    path('<int:pk>/seeker_deleteentry/', views.seeker_deleteentry, name='seeker_deleteentry'),
    path('<int:pk>/edit_drink_details/', views.edit_drink_details, name='edit_drink_details'),
    path('<int:pk>/tasteseeker_search/', views.tasteseeker_search, name='tasteseeker_search'),
    path('about-us/', views.AboutUs, name='AboutUs'),
]

urlpatterns += staticfiles_urlpatterns()
