from rest_framework import serializers

from .models import Publish


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'
