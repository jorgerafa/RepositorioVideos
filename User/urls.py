from django.urls import path
from User import views

urlpatterns = [
    path('', views.base, name='home' ),
    path('signin/', views.sign_in, name='sign_in' ),
]