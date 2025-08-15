from .models import URL
from rest_framework import serializers


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'long_url', 'short_key', 'created_at', 'updated_at']
        read_only_fields = ['id', 'short_key', 'created_at', 'updated_at']
