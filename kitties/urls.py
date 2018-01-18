from django.contrib import admin
from django.urls import path

from registry.views import KittyListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', KittyListView.as_view(), name='kitty-list'),
]
