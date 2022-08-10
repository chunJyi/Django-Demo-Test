from django.urls import path,include

from . import views

urlpatterns= [

    path('', views.home,name='home'),
    path('create', views.create,name='create'),
    path('createCustomer', views.createCustomer,name='createCustomer'),
    path('promotionSale', views.promotionSale,name='promotionSale'),
    path('item<str:i>', views.item,name='item'),



]
