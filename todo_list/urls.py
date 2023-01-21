from django.urls import path 
from . import views
# from .views import api_home

urlpatterns = [
    path('', views.creat),
    path('<int:id>', views.get_item),    

]

