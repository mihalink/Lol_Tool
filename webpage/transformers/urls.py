from django.urls import path
from . import views

app_name = 'transformers'

urlpatterns = [
    path('', views.main, name='main'),
    path('singleview/', views.singleview, name='Single View'),
]
