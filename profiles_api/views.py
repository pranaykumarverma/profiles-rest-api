from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of API View Features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similiar to a Traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a Hello Message with our name """
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle update of data """
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """ Handle update of PATCH """
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """ Handle DELETE of data """
        return Response({"method": "DELETE"})
