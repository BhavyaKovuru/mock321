
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('temp/', views.update, name= "temp"),
    path('temp1/', views.update1, name= "temp1"),
    path('temp2/', views.update2, name= "temp2"),
    path('temp3/', views.update3, name= "temp3"),
    path('lowTech/', views.index2, name="index2"),
    path('highTech/', views.index, name="index")
]
