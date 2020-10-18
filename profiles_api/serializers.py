from rest_framework import serializers
from rest_framework import fields

from profiles_api import models


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        # Password need to be write only so use extra_kwargs
        extra_kwargs = {
            # Add custom 'password' field
            "password": {
                # when create password set it to write only
                # only can create or update
                # can't retriece use GET won't see password object at the response
                "write_only": True,
                # custom style password only can see dot or start input
                "style": {"input_type": "password"},
            }
        }

    # overwrite the create function
    # password need to be created as a hash not the clear text
    def create(self, validated_data):
        """Create and return a new user"""
        # create and return a new user from our user profiles model manager
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user

    # if a user updates their profile, the password field is stored in cleartext, and they are unable to login.
    # This is because we need to override the default behaviour of Django REST Frameworks ModelSerializer to hash the users password when updating.
    # The default update logic for the Django REST Framework (DRF) ModelSerializer code will take whatever fields are provided (in our case: email, name, password) and pass them directly to the model.

    # This is fine for the email and name fields, however the password field requires some additional logic to hash the password before saving the update.
    # Therefore, we override the Django REST Framework's update() method to add this logic to check for the presence password in the validated_data which is passed from DRF when updating an object.
    # If the field exists, we will "pop" (which means assign the value and remove from the dictionary) the password from the validated data and set it using set_password() (which saves the password as a hash).
    # Once that's done, we use super().update() to pass the values to the existing DRF update() method, to handle updating the remaining fields.
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)
