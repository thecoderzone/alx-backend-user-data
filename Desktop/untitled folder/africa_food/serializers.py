from rest_framework import serializers


class Foodserializer(serializers.Serializer):
    """serializes a name field for testing out api"""

    name = serializers.CharField(max_length=100)
