
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('tasteseeker/', include('tasteseeker.urls')),
    path('admin/', admin.site.urls),
    
]
