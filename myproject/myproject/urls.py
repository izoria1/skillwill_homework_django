# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import home 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls')),
    path('animal/', include('animal.urls')),
    path('', home, name='home'),  
]
