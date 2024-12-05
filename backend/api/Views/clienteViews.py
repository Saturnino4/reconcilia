from django.shortcuts import get_object_or_404
from api.models import Cliente
from rest_framework.views import APIView
from api.serializers import ClienteSerializer
from api.views import ResponseData
from django.http import Http404

class ClienteViewsGet(APIView):

    def getByAnyColumn(self, request,campo,valor):
        try:
            if 'exact' in request.GET:
                querySet = Cliente.objects.filter(**{campo: valor}).exclude(status='eliminado')
            else:
                querySet = Cliente.objects.filter(**{campo + '__icontains': valor}).exclude(status='eliminado')
            rows = querySet.count()
            serializer = ClienteSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Clientes encontrados'
            else:
                message = 'Nenhum cliente encontrado'
                status = 208
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar clientes: ' + str(e)

        return {'status': status, 'data': data,'message': message, 'rows': rows }

    def getAll(self, request):
        try:
            querySet = Cliente.objects.all().exclude(status='eliminado')
            rows = querySet.count()
            serializer = ClienteSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Clientes encontrados'
            else:
                message = 'Nenhum cliente encontrado'
                status = 208
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar clientes: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Cliente, id=id)
                if querySet.status == 'eliminado':
                    pass
                serializer = ClienteSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Cliente encontrado'
                else:
                    message = 'Nenhum Cliente encontrado'
                    status = 208
            except Http404:
                status = 208
                data = []
                message = 'Cliente não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Cliente: ' + str(e)
        
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
    

class ClienteViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Cliente criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar cliente: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar cliente: ' + str(e)
        
        return ResponseData(None, status, message)
    
class ClienteViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request, id):
            try:
                querySet = get_object_or_404(Cliente, id=id)
                serializer = ClienteSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Cliente atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar cliente: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar cliente: ' + str(e)
            
            return ResponseData(None, status, message)

class ClienteViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request, id):
        try:
            querySet = get_object_or_404(Cliente, id=id)
            querySet.status = 'eliminado'
            querySet.save()
            status = 200
            message = 'Cliente deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar cliente: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    