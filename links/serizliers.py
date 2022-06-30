from dataclasses import fields
from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.Serializer):
    serializers.ModelSerializer

    class Meta:
        model = Link
        fields = '__all__'
