from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),

    path('', views.index, name='index'),
]