from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .views import tasteseeker_search

urlpatterns = [

    path('admin/', admin.site.urls),
    # Sets the url path to the home page tasteseeker_home.html
    path('tasteseeker_home/', views.tasteseekerHome, name="tasteseeker_home"),
    # Sets the url path to the entry page tasteseeker_createentry.html
    path('tasteseeker_createentry/', views.tasteseeker_createentry, name="tasteseeker_createentry"),
    # Sets the url path to the drink list page tasteseeker_drink_list.html
    path('tasteseeker_drink_list/', views.tasteseeker_drink_list, name='tasteseeker_drink_list'),
    # Sets the url path to the delete entry page tasteseeker_deleteentry.html
    path('<int:pk>/tasteseeker_deleteentry/', views.tasteseeker_deleteentry, name='tasteseeker_deleteentry'),
    # Sets the url path to the edit an entry page edit_drink_details.html
    path('<int:pk>/edit_drink_details/', views.edit_drink_details, name='edit_drink_details'),
    # Sets the url path to the details of one entry via a link when the user clicks the drink name
    path('<int:pk>/tasteseeker_search/', views.tasteseeker_search, name='tasteseeker_search'),
    # Sets the url path to the login page
    path('LogIn/', views.LogIn, name='LogIn'),


]
urlpatterns += staticfiles_urlpatterns()