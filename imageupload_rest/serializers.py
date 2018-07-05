from rest_framework import serializers
from imageupload.models import UploadImage

class UploadImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'image')