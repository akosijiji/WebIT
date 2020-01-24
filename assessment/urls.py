from django.urls import path
from django.conf.urls import url, include
from django_filters.views import FilterView
from .filters import ClientFilter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/create', views.create, name='create'),
    path('client/edit/<int:id>', views.edit, name='edit'),  
    path('client/update/<int:id>', views.update),  
    path('client/delete/<int:id>', views.destroy),  
    # path('client/search/$', views.search, name='search'), 
]