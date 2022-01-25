from PIL import Image
from django.db import models
import hashlib
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


def upload_to(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    class_name = instance.__class__.__name__.lower()

    h = hashlib.md5()
    field = getattr(instance, 'file')
    for chunk in field.chunks():
        h.update(chunk)
    name = h.hexdigest()

    return os.path.join(
        class_name,
        name + ext,
    )


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Picture(models.Model):
    file = models.ImageField(storage=OverwriteStorage, upload_to=upload_to)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'Picture №{self.id}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.file.path)

        try:
            if self.height == None or self.height == 0:
                output_size = (self.width, self.width)
                img.thumbnail(output_size)
                img.save(self.file.path)
            else:
                output_size = (self.width, self.height)
                resized_img = img.resize(output_size)
                resized_img.save(self.file.path)
        except ValueError or TypeError or ZeroDivisionError:
            output_size = (self.width, self.width)
            img.thumbnail(output_size)
            img.save(self.file.path)
