from django.urls import path
from .views import stock_data
from . import views
urlpatterns = [
    path('', views.stock_data, name='stock_data'),
]