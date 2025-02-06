from api.models import URLMapping
from rest_framework import serializers

class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['long_url', 'short_code']