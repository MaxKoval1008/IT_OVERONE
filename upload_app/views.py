from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PictureForm
from .models import Picture
from django.core.files.storage import FileSystemStorage


def home_page(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, 'home_page.html')


class PictureCreate(CreateView):
    model = Picture
    form_class = PictureForm
    extra_context = {'picture': Picture.objects.all()}
    template_name = 'picture_create.html'
    success_url = '/picture/'
