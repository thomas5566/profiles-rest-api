from django.http import request
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list APIView features"""
        an_apiview = [
            "Use Http methods as finctions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped manually yo URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get(
                "name"
            )  # retrive serializers.py define 'name'
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updateing an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


# create a viewset to accese the serializer though an endpoint head over to the view.py
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    # assiging the serializer class to a model serializer and queryset
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication_classes set how the user will authenticate 
    # that is the mechanism they will use 
    authentication_classes = (TokenAuthentication,)
    # the permission classes is set how the user gets permission to do certain things
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,) # added ',' is for tuple not a item
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    # adds the render classes to our obtain auth token view
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
