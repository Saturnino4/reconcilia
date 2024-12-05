from django.shortcuts import get_object_or_404
from api.models import Moeda
from rest_framework.views import APIView
from api.serializers import MoedaSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = Moeda.objects.raw(f"SELECT * FROM moeda WHERE {campo} like '{valor}'")
        data = []
        for item in querySet:
            data.append({
                'id': item.id,
                'nome': item.data,
                'hora': item.hora,
                'status': item.status,
            })
            rows += 1
    except:
        return ResponseData(None, 500, 'Erro ao buscar moeda')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class MoedaViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = Moeda.objects.all()
            rows = querySet.count()
            serializer = MoedaSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Moedas encontradas'
            else:
                message = 'Nenhuma moeda encontrada'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar moedas: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Moeda, id=id)
                serializer = MoedaSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Moeda encontrada'
                else:
                    message = 'Nenhuma Moeda encontrada'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Moeda não encontrada'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Moeda: ' + str(e)
        
        return {'status': status, 'data': data, 'message': message}

    def get(self, request, id=None):

        if id is not None: 
            res = self.getById(request, id)
            return ResponseData(res['data'], res['status'], res['message'])
            # return ResponseData([], 200, "teste")
        
        if id is None and 'campo' in request.GET and 'valor' in request.GET:
            res = self.getByAnyColumn(request, request.GET['campo'], request.GET['valor'])
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
    

class MoedaViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = MoedaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Moeda criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar moeda: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar moeda: ' + str(e)
        
        return ResponseData(None, status, message)
    
class MoedaViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request):
            try:
                querySet = get_object_or_404(Moeda, id=request.data['id'])
                serializer = MoedaSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Moeda atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar moeda: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar moeda: ' + str(e)
            
            return ResponseData(None, status, message)

class MoedaViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(Moeda, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Moeda deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar moeda: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    