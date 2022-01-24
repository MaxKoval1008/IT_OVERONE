from PIL import Image
from django.db import models


class Picture(models.Model):
    file = models.ImageField(upload_to='images/')
    width = models.CharField(max_length=4)
    height = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return f'Picture №{self.id}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.file.path)

        if self.height != 0:
            output_size = (int(self.width), int(self.height))
            img.thumbnail(output_size)
            img.save(self.file.path)
        else:
            output_size = (int(self.width), int(self.width))
            img.thumbnail(output_size)
            img.save(self.file.path)
