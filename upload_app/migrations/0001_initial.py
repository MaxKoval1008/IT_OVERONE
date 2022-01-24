# Generated by Django 4.0.1 on 2022-01-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
                ('width', models.CharField(max_length=4)),
                ('height', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
    ]
