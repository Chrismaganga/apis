from operator import is_
from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer

from rest_framework .response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



