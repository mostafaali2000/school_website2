from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.pageAnnouncement),
    path('', views.pageBus),
    path('', views.pageWhyUs),

]
