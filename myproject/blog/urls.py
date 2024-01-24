from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contact/', views.contact, name='blog-contact'),
    path('projects/', views.projects, name='my-projects'),
    path('currencyapi/', views.currencyapi, name='currencyapi'),
    # path('upload/', views.uploadpdf, name='uploadpdf')
]