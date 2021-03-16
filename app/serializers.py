from rest_framework import serializers
from .models import Home


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['username', 'email', 'password', 'phone']