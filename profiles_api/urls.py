from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# ViewSet
router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("", include(router.urls)),  # Pass router.register  => router.urls
]
