from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('/', views.homepage, name='homepage'),
    path('customerRegistration', views.customerRegistration, name='customerRegistration'),
    path('ourProducts', views.ourProducts, name='ourProducts'),
    path('ourServices', views.ourServices, name='ourServices'),
    path('stockRegistration', views.stockRegistration, name='stockRegistration'),

]
