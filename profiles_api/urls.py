from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# ViewSet
router = DefaultRouter()
# 'basename' : creating a view set that doesen't have query set or
# want to override the name of the query set is associated to it
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
# no need to specify a 'basename' because we have a view set a query set object
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("", include(router.urls)),  # Pass router.register  => router.urls
]
