from django.urls import path
from .views import HomeView
from django.http import HttpResponse

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('api/', lambda x : HttpResponse('Hola desde la api'), name='api')
] 
