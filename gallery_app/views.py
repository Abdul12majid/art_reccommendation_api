from django.shortcuts import render
from django.http import HttpResponse
from .models import Art_Work

from rest_framework.viewsets import ModelViewSet
from .serializers import Art_Work_Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
	return HttpResponse('Hello')

class ArtWorks(ModelViewSet):
	queryset = Art_Work.objects.all()
	serializer_class = Art_Work_Serializer

@api_view(['GET'])
def get_arts(request):
	arts = Art_Work.objects.all()
	serializer = Art_Work_Serializer(arts, many=True)
	return Response(serializer.data)