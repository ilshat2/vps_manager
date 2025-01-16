from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vps.urls')),  # Подключение корневого API
    path('', lambda request: HttpResponse(
        "<h1>Welcome to VPS Manager API</h1>"
        ))  # Редирект на API
]
