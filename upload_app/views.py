from django.shortcuts import render
from django.views.generic import CreateView
from .models import Picture
from django.core.files.storage import FileSystemStorage
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .serializers import PictureSerializer


# class PictureResize(RetrieveAPIView):
#     queryset = Picture.objects.all()
#     serializer_class = PictureSerializer
#
#     def get(self, request, *args, **kwargs):
#         picture = Picture.objects.all()
#         if request.method == 'GET' and request.FILES:
#             file = request.FILES['myfile1']
#             fs = FileSystemStorage()
#             filename = fs.save(file.name, file)
#             file_url = fs.url(filename)
#             return render(request, 'home_page.html', {
#                 'file_url': file_url
#             })
#         return render(request, 'home_page.html')


class PictureResize1(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    # def dehydrate(self, bundle):
    #     if bundle.request.method == 'POST':
    #         bundle.data['my_custom_data'] = 'my_data'
    #
    #     return bundle

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PictureSerializer(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                img_obj = form.instance
                return render(request, 'home_page.html', {'form': form, 'img_obj': img_obj})
        else:
            form = PictureSerializer()
        return render(request, 'home_page.html', {'form': form})
