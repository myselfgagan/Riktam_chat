from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html', redirect_authenticated_user=True), name='login'),
    path('app/', views.app, name='app'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),    
    path('chat/<str:room_name>/', views.room, name='room'),
]