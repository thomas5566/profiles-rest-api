from rest_framework import permissions

# BasePermission provides for making your own custom permissions classes
class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # SAFE_METHODS that don't require or don't make any change to the object
        # only reading an object not acyually trying to make any change to the object
        # check the method if it is in the safe method will allow the request to go through
        if request.method in permissions.SAFE_METHODS:
            return True

        # if using update or delete method
        return obj.id == request.user.id
