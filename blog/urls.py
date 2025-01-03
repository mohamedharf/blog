#import models
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('tags/<slug:tag_slug>', views.get_tags, name='get_tags'),
    path('coment', views.save_comment, name='save_comment'),
    path('coment-delet', views.delet , name='coment-delet'),
]