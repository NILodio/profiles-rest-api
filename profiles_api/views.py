from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request , format = None):
        """Returns a list of APIView feactures"""
        an_apiview = [
            'Uses HTTP methods as fuctions (get, post, put, delete)',
            'Is similar to a tradicional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
