from django.contrib import admin
from django.urls import path, include
from .views import home  # Make sure this import is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('reader/', include('reader.urls')),
    path('', home, name='home'),
]
