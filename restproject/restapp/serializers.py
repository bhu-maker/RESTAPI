from dataclasses import fields
from .import models
from rest_framework.serializers import ModelSerializer

class corpseri(ModelSerializer):
    class Meta:
        model=models.corporates
        fields=('id','org','nature','opennings','salary','employees','ratings')
