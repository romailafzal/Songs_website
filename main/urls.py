from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.autth.urls')),
    path('song/', include('apps.song.urls')),
]
