from django.shortcuts import render
from .models import Picture
from rest_framework.generics import CreateAPIView
from .serializers import PictureSerializer


class PictureResize1(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    # def post(self, request, *args, **kwargs):
    #     file = Picture.objects.all()
    #     return render(request, 'home_page.html', {'file': file})

