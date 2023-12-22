from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app_1.serializers import PersonSerializer
from app_1.models import PersonModel

# Create your views here.

# APIView
# Generics
# Viewset - restfull guidelinces


class PersonModelViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()