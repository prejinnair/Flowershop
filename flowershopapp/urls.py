from . import views
from django.urls import path
app_name='flowershopapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('allcollection/', views.allflowers, name='allflowers'),
    path('<int:f_id>/',views.f_details, name='f_details'),
    path('credential', views.credential, name='credential'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),


]