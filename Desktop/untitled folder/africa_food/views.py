from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  # importing status codes (200,404,500 etc)
from . import serializers

# Create your views here.


class getfood(APIView):
    """Getting food list"""
    serializers_class = serializers.Foodserializer

    # Creating a get request to API
    def get(self, request):
        """Get response"""

        food_list = [
            'there is a list of food list', 'matoki', 'ugali', 'pilau',
            'chapati'
        ]

        return Response({'food': food_list})

    # Creating a post request to API
    def post(self, request):
        """ Creating food list"""
        serializer = serializers.Foodserializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Example of an africa food is {0}'.format(name)
            return Response({"message": message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_404_NOT_FOUND)

    # Creating a put (updating) request to API
    def put(self, request, pk=None):
        """Updating an api request"""

        return Response({"method": "put"})

    # Creating a patch (updating) request to API
    def patch(self, request, pk=None):
        """Updating an api partically request"""

        return Response({"method": "patch"})

    # Creating a delete  request to API
    def delete(self, request, pk=None):
        """deletes an api objects"""

        return Response({"method": "delete"})
