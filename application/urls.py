from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_services/', views.show_services, name='show_services'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('show_stock_data/', views.show_stock_data, name='show_stock_data'),
]

# host + '/' -> index
# host + '/show_services/' -> show_services
