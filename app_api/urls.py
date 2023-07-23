from django.urls import path ,include
from rest_framework import routers
from .views import BookViewSet,BookViewSetGet

router = routers.DefaultRouter()
router.register(r'book',BookViewSet)
router.register(r'book_get',BookViewSetGet)


urlpatterns = [
    path('',include(router.urls)),
]
