from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """ Test api view """

    def get(self, request, format=None):
        """ Returns a list of APIView """
        an_apiview=[
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over the app logic',
        'Is mapped mnually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
