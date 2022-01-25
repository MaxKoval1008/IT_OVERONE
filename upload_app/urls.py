from django.urls import path
from .views import *

urlpatterns = [
    path('resize_picture/v2', PictureResize1.as_view()),
]
