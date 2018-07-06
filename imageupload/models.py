import uuid
from django.db import models


#penamaan file unique image dengan UUID4
def scramble_uploaded_image_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class UploadImage(models.Model):
    image = models.ImageField("Upload Image", upload_to=scramble_uploaded_image_filename) #stores the images
