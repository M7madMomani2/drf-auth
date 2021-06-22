from django.db.models import fields
from rest_framework import serializers
from .models import Auth

class AuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id','author')