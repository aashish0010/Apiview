from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Home
from .serializers import HomeSerializers
from rest_framework import status


# Create your views here.
# @api_view(['GET'])
# def home(request):
#     return Response({'msg': 'Hello World'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            hom = Home.objects.get(id=id)
            serializer = HomeSerializers(hom)
            return Response(serializer.data)

        hom = Home.objects.all()
        serializers = HomeSerializers(hom, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        data = request.data
        serializer = HomeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        hom = Home.objects.get(pk=id)
        serializer = HomeSerializers(hom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        id = pk
        hom = Home.objects.get(pk=id)
        serializer = HomeSerializers(hom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        hom = Home.objects.get(pk=id)
        hom.delete()
        return Response({'msg': 'Data Deleted'})
