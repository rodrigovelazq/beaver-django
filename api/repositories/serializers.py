from rest_framework import serializers
from .models import Owners, Repositories


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = '__all__'


class RepositoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repositories
        fields = '__all__'
