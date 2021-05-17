from django.urls import path

from  . import views

app_name = 'store'

urlpatterns = [
    path('', views.shoe_home, name='home'),
    path('shop/<slug:shoe_slug>/', views.shoe_detail, name='shoe_detail'),
    path('brand/<slug:brand_slug>/', views.brand_shoe, name='brand_shoe'),
    path('search/', views.shoe_search, name='shoe_search'),
]