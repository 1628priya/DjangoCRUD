from rest_framework import viewsets
from .import models
from .import serializers

class InstitueViewset(viewsets.ModelViewSet):
    queryset=models.Institutes.objects.all()
    serializer_class=serializers.InstituteSerializer