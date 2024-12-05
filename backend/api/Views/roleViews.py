from django.shortcuts import get_object_or_404
from api.models import Role
from rest_framework.views import APIView
from api.serializers import RoleSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = Role.objects.raw(f"SELECT * FROM role WHERE {campo} like '{valor}'")
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
        return ResponseData(None, 500, 'Erro ao buscar role')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class RoleViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = Role.objects.all()
            rows = querySet.count()
            serializer = RoleSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Roles encontrados'
            else:
                message = 'Nenhum role encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar roles: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Role, id=id)
                serializer = RoleSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Role encontrado'
                else:
                    message = 'Nenhum Role encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Role não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Role: ' + str(e)
        
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
    

class RoleViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Role criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar role: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar role: ' + str(e)
        
        return ResponseData(None, status, message)
    
class RoleViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request):
            try:
                querySet = get_object_or_404(Role, id=request.data['id'])
                serializer = RoleSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Role atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar role: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar role: ' + str(e)
            
            return ResponseData(None, status, message)

class RoleViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(Role, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Role deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar role: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    