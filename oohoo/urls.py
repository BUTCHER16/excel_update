# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_excel, name='upload_excel'),
    path('success/', views.success_view, name='success'),
    # Add other URL patterns as needed
]
