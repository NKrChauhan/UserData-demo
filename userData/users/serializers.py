from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Userinfo

class userSerializer(ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'