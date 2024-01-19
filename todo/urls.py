from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='mylist' ),
    path('update/<str:pk>/',views.updatetask,name='updated'),
    path('delete/<str:pk>/',views.deletetask,name='deleted')
]