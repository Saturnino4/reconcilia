from rest_framework.views import APIView
from rest_framework import status
from api.models import Pendencia, Extrato
from api.serializers import PendenciaSerializer, ExtratoSerializer
from api.views import ResponseData




class PendenciaView(APIView):

#*** Calculos ***

    def getPendenciaNossa(self, request):

        try:
            querySet = Extrato.objects.raw("""

                SELECT extracto.data_

            """)
        
        except Exception as e:
            return ResponseData(None, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Erro ao buscar pendencias: ' + str(e))





#**** PendenciaView  ****

    def getById(self, pk):
        try:
            pendencia = Pendencia.objects.get(pk=pk)
            serializer = PendenciaSerializer(pendencia)
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Pendencia retornada com sucesso')
        except Pendencia.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Pendencia não encontrada')

    def get(self, request, id=None):

        if 'type' in request.GET:
            if request.GET['type'] == 'nossa':
                return self.getPendenciaNossa(request)
            
            else:
                return ResponseData(None, status.HTTP_400_BAD_REQUEST, 'Tipo de pendencia inválido')
        else:
            return ResponseData(None, status.HTTP_400_BAD_REQUEST, 'Tipo de pendencia não informado')

        if 'id' is not None:
            return self.getById(id)

        pendencias = Pendencia.objects.all()
        serializer = PendenciaSerializer(pendencias, many=True)
        return ResponseData(serializer.data,status.HTTP_200_OK, 'Pendencias retornadas com sucesso')

    def post(self, request):
        serializer = PendenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_201_CREATED, 'Pendencia criada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao criar pendencia')
    
    def put(self, request, pk):
        pendencia = Pendencia.objects.get(pk=pk)
        serializer = PendenciaSerializer(pendencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseData(serializer.data, status.HTTP_200_OK, 'Pendencia atualizada com sucesso')
        return ResponseData(serializer.errors, status.HTTP_400_BAD_REQUEST, 'Erro ao atualizar pendencia')
    
    def delete(self, request, pk):
        try:
            pendencia = Pendencia.objects.get(pk=pk)
            pendencia.status = 'deleted'
            pendencia.save()
            return ResponseData(None, status.HTTP_204_NO_CONTENT, 'Pendencia deletada com sucesso')
        except Pendencia.DoesNotExist:
            return ResponseData(None, status.HTTP_404_NOT_FOUND, 'Pendencia não encontrada')

    