# Generated by Django 4.0.1 on 2022-01-25 12:44

from django.db import migrations, models
import upload_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0005_alter_picture_height_alter_picture_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(storage=upload_app.models.OverwriteStorage, upload_to='images/'),
        ),
    ]
