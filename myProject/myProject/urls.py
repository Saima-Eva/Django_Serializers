
from django.contrib import admin
from django.urls import path

from myProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myStudent/<str:myid>', views.myStudent, name='myStudent'),
    path('myStudent_List', views.myStudent_List, name='myStudent_List'),

]
