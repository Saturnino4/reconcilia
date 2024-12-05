from django.shortcuts import get_object_or_404
from api.models import Historico
from rest_framework.views import APIView
from api.serializers import HistoricoSerializer
from api.views import ResponseData, ResponseError
from django.http import Http404

class HistoricoViewsGet(APIView):

    def getByAnyColumn(self, request,campo,valor):
        try:
            if 'exact' in request.GET:
                querySet = Historico.objects.filter(**{campo: valor})
            else:
                querySet = Historico.objects.filter(**{campo + '__icontains': valor})
            rows = querySet.count()
            serializer = HistoricoSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Historicos encontrados'
            else:
                message = 'Nenhum produto encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar produtos: ' + str(e)

        return {'status': status, 'data': data,'message': message, 'rows': rows }

    def getAll(self, request):
        try:
            querySet = Historico.objects.all()
            rows = querySet.count()
            serializer = HistoricoSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Historicos encontrados'
            else:
                message = 'Nenhum historico encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar historicos: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Historico, id=id)
                serializer = HistoricoSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Historico encontrado'
                else:
                    message = 'Nenhum Historico encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Historico não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Historico: ' + str(e)
        
        return {'status': status, 'data': data, 'message': message}

    def get(self, request):
        if 'id' in request.GET:
            res = self.getById(request, request.GET['id'])
            return ResponseData(res['data'], res['status'], res['message'])
        else:
            res = self.getAll(request)
            return ResponseData(res['data'], res['status'], res['message'])
        
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    

class HistoricoViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = HistoricoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Historico criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar historico: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar historico: ' + str(e)
        
        return ResponseData(None, status, message)
    
class HistoricoViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request, id):
            try:
                querySet = get_object_or_404(Historico, id=id)
                serializer = HistoricoSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Historico atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar historico: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar historico: ' + str(e)
            
            return ResponseData(None, status, message)

class HistoricoViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(Historico, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Historico deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar historico: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    