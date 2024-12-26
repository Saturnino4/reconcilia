from rest_framework.views import APIView
from rest_framework import status
from api.models import Nostro_vostro, Extrato
from api.serializers import Nostro_vostroSerializer, ExtratoSerializer
from api.views import ResponseData




class Nostro_vostroView(APIView):

#*** Calculos ***

    def getNostro_vostroNossa(self, request):

        try:
            querySet = Extrato.objects.raw("""

                SELECT extracto.data_

            """)
        
        except Exception as e:
            return ResponseData(None, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Erro ao buscar nostro_vostros: ' + str(e))





#**** Nostro_vostroView  ****  

    def getById(self, pk):
        try:
            nostro_vostro = Nostro_vostro.objects.get(pk=pk)
            serializer = Nostro_vostroSerializer(nostro_vostro)
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Nostro_vostro retornada com sucesso')
        except Nostro_vostro.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Nostro_vostro não encontrada')

    def get(self, request, id=None):

        if 'type' in request.GET:
            if request.GET['type'] == 'nossa':
                return self.getNostro_vostroNossa(request)
            
            else:
                return ResponseData(None, status.HTTP_400_BAD_REQUEST, 'Tipo de nostro_vostro inválido')
        else:
            return ResponseData(None, status.HTTP_400_BAD_REQUEST, 'Tipo de nostro_vostro não informado')

        if 'id' is not None:
            return self.getById(id)

        nostro_vostros = Nostro_vostro.objects.all()
        serializer = Nostro_vostroSerializer(nostro_vostros, many=True)
        return ResponseData(serializer.data,status.HTTP_200_OK, 'Nostro_vostros retornadas com sucesso')

    def post(self, request):
        serializer = Nostro_vostroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_201_CREATED, 'Nostro_vostro criada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao criar nostro_vostro')
    
    def put(self, request, pk):
        nostro_vostro = Nostro_vostro.objects.get(pk=pk)
        serializer = Nostro_vostroSerializer(nostro_vostro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Nostro_vostro atualizada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao atualizar nostro_vostro')
    
    def delete(self, request, pk):
        try:
            nostro_vostro = Nostro_vostro.objects.get(pk=pk)
            nostro_vostro.status = 'deleted'
            nostro_vostro.save()
            return ResponseData(None, status.HTTP_204_NO_CONTENT, 'Nostro_vostro deletada com sucesso')
        except Nostro_vostro.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Nostro_vostro não encontrada')

    