from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .views import tasteseeker_search

urlpatterns = [

    path('admin/', admin.site.urls),
    # Sets the url path to the home page seeker_home.html
    path(r'^seeker_home/$', views.seeker_Home, name="seeker_home"),
    # Sets the url path to the entry page tasteseeker_createentry.html
    path('seeker_createentry/', views.seeker_createentry, name="seeker_createentry"),
    # Sets the url path to the drink list page tasteseeker_drink_list.html
    path('seeker_drink_list/', views.seeker_drink_list, name='seeker_drink_list'),
    # Sets the url path to the delete entry page tasteseeker_deleteentry.html
    path('<int:pk>/seeker_deleteentry/', views.seeker_deleteentry, name='seeker_deleteentry'),
    # Sets the url path to the edit an entry page edit_drink_details.html
    path('<int:pk>/edit_drink_details/', views.edit_drink_details, name='edit_drink_details'),
    # Sets the url path to the details of one entry via a link when the user clicks the drink name
    path('<int:pk>/tasteseeker_search/', views.tasteseeker_search, name='tasteseeker_search'),
    # Sets the url path to the login page
    path('LogIn/', views.LogIn, name='LogIn'),
    # Sets the url path to the first intro page/ bartender or drinker
    path('<int:pk>/tasteseekerintropick/', views.tasteseekerintropick, name='tasteseekerintropick'),
    


]
urlpatterns += staticfiles_urlpatterns()