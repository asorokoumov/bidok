from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:number>/', views.order, name='order'),
    path('', views.in_development, name='in_development'),

]