# Generated by Django 2.0.7 on 2018-07-06 06:25

from django.db import migrations, models
import imageupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=imageupload.models.scramble_uploaded_image_filename, verbose_name='Upload Image'),
        ),
    ]
