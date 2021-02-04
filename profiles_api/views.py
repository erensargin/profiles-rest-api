from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    """ Test api view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView """
        an_apiview=[
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over the app logic',
        'Is mapped mnually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello massage with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partial handle update"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete objects"""
        return Response({'method':'DELETE'})
