from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda r: redirect('/tasteseeker/', permanent=False)),  # add this line
    path('tasteseeker/', include(('tasteseeker.urls', 'tasteseeker'), namespace='tasteseeker')),
    path('admin/', admin.site.urls),
]