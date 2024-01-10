from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .views import tasteseeker_search

urlpatterns = [

    # Sets the url path to the landing page
    path('Index/', views.Index, name='Index'),
    # Sets the url path to the registration page
    path('register', views.register, name="register"),
    # Sets the url path to the login page
    path('login', views.login, name="login"),
    # Sets the url path to the landing page after the user clicks on logout
    path('logout', views.logout, name="logout"),
    # Sets the url path to the admin page
    path('admin/', admin.site.urls),
    # Sets the url path to the Seeker homepage
    path('seeker_home/', views.seeker_home, name="seeker_home"),
    # Sets the url path to the page to create a drink rating
    path('seeker_createentry/', views.seeker_createentry, name="seeker_createentry"),
    # Sets the url path to the drink list page tasteseeker_drink_list.html
    path('seeker_drink_list/', views.seeker_drink_list, name='seeker_drink_list'),
    # Sets the url path to the delete entry page tasteseeker_deleteentry.html
    path('<int:pk>/seeker_deleteentry/', views.seeker_deleteentry, name='seeker_deleteentry'),
    # Sets the url path to the edit an entry page edit_drink_details.html
    path('<int:pk>/edit_drink_details/', views.edit_drink_details, name='edit_drink_details'),
    # Sets the url path to the details of one entry via a link when the user clicks the drink name
    path('<int:pk>/tasteseeker_search/', views.tasteseeker_search, name='tasteseeker_search'),
    # Sets the url path to the About Us page 
    path('AboutUs/', views.AboutUs, name='AboutUs'),

    


]
urlpatterns += staticfiles_urlpatterns()