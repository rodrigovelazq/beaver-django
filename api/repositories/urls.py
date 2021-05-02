from django.urls import path, include
from .views import RepositoriesView, OwnersView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('repositories', RepositoriesView)
router.register('owners', OwnersView)

urlpatterns = [
    path('', include(router.urls)),
]
