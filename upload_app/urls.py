from django.urls import include, path
from .views import *

urlpatterns = [
    path('resize_picture/', PictureCreate.as_view()),
    path('', home_page),
]
