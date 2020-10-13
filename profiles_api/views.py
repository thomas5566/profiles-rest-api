from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list APIView features"""
        an_apiview = [
            "Use Http methods as finctions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped manually yo URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

