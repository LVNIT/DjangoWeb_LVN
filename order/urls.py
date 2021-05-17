from django.urls import path
from . import views


app_name = 'order'


urlpatterns = [
    path('add/', views.order_add, name='order_add')
]