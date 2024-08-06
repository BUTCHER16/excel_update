# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.upload_excel, name='upload_excel'),
    path('success/', views.success_view, name='success'),
    path('login/',views.login, name='login'),
    # Add other URL patterns as needed
]
