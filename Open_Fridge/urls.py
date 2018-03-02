from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import include
from . import views
from . import forms


urlpatterns = [
  path('', views.index, name='index'),
  path('index/', views.index, name='index'),
  path('database/', views.database, name = 'database'),
  path('results/', views.results, name='results'),
  path('accountPage/', views.accountPage, name ='accountPage'),
  #path('login/', views.indexAP, name='login_view'),
  #path('logout/', views.index, name='index'),
  path('register_page/', views.register_page, name = 'register_page'),
  path('recipe_register/', views.recipe_register, name = 'recipe_register'),
  url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
  url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
]
