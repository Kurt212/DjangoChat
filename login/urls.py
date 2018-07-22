from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.sigin_view,),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
]