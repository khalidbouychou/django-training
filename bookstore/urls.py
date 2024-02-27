
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('books/',views.books),
    # path('customer/',views.customer),
    path('customer/<str:pk>',views.customer),
    path('profile/',views.profile)
]
