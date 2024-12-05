from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Swift
from api.serializers import SwiftSerializer
from api.views import ResponseData




class SwiftView(APIView):

    
#*** Calculos ***

    # def set



#**** SwiftView  ****

    def getById(self, pk):
        try:
            swift = Swift.objects.get(pk=pk)
            serializer = SwiftSerializer(swift)
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Swift retornada com sucesso')
        except Swift.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Swift não encontrada')

    def get(self, request, id=None):

        if 'id' is not None:
            return self.getById(id)

        swifts = Swift.objects.all()
        serializer = SwiftSerializer(swifts, many=True)
        return ResponseData(serializer.data,status.HTTP_200_OK, 'Swifts retornadas com sucesso')

    def post(self, request):
        serializer = SwiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_201_CREATED, 'Swift criada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao criar swift')
    
    def put(self, request, pk):
        swift = Swift.objects.get(pk=pk)
        serializer = SwiftSerializer(swift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Swift atualizada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao atualizar swift')
    
    def delete(self, request, pk):
        try:
            swift = Swift.objects.get(pk=pk)
            swift.status = 'deleted'
            swift.save()
            return ResponseData(None, status.HTTP_204_NO_CONTENT, 'Swift deletada com sucesso')
        except Swift.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Swift não encontrada')

    