from PIL import Image
from django.db import models


class Picture(models.Model):
    file = models.ImageField(upload_to='images/')
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
