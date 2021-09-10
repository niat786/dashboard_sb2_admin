from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('accounts/', include('allauth.urls')),
    path('test/', views.test),
]
