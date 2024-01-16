from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from cfdi.serializers import CreateCfdiSerializer, CfdiSerializer

from cfdi.models import Cfdi

class CreateCfdiCollection(APIView):
    
    def post(self, request):
        data = request.data
        serializer = CreateCfdiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 
                'message': 'este cfdi ha sido creado correctamente',
                'data': serializer.data})
        return Response({'status': 500, 'message': 'no existe este cfdi'})

class CfdiView(APIView):
    def get(self, request):
        docs = Cfdi.objects.all()
        serializer = CfdiSerializer(docs, many=True)
        return Response({'status': 200,
            'message': 'estos son los cfdi registrados',
            'data': serializer.data})