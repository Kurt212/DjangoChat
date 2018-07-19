from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index_view),
    path("<str:room_name>/", room_view)
]
