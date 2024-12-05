from django.shortcuts import get_object_or_404
from api.models import Permissao
from rest_framework.views import APIView
from api.serializers import PermissaoSerializer
from api.views import ResponseData
from django.http import Http404


class Permissao_Utilizador(APIView):
    def get(self,request,id):
        try:
            permiQuery = Permissao.objects.raw("""
                        SELECT p.id, p.modulo, p.autorizacao FROM utilizador u
                        JOIN utilizador_role ur ON u.id = ur.utilizador_id
                        JOIN role r ON ur.role_id = r.id
                        JOIN role_permissao rp ON r.id = rp.role_id
                        JOIN permissao p ON rp.permissao_id = p.id
                        WHERE u.id = %s
                        """ % id)
            data = []
            for item in permiQuery:
                data.append({
                    'modulo': item.modulo,
                    'autorizacao': item.autorizacao
                })
            status = 200 if len(data) > 0 else 208
            message = "Lista de permissoes"
        except Exception as e:
            data = {}
            status = 500
            message = "Falha ao buscar permissoes desse utilizador: "+str(e)
            
        return ResponseData(data,status,message)


class PermissaoViewsGet(APIView):
    def getByAnyColumn(self, request,campo,valor):
        try:
            if 'exact' in request.GET:
                querySet = Permissao.objects.filter(**{campo: valor}).exclude(status='eliminado')
            else:
                querySet = Permissao.objects.filter(**{campo + '__icontains': valor}).exclude(status='eliminado')
            rows = querySet.count()
            serializer = PermissaoSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Permissaos encontrados'
            else:
                message = 'Nenhum permissao encontrado'
                status = 208
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar permissaos: ' + str(e)

        return {'status': status, 'data': data,'message': message, 'rows': rows }


    def getAll(self, request):
        try:
            querySet = Permissao.objects.all().exclude(status='eliminado')
            rows = querySet.count()
            serializer = PermissaoSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Permissaos encontrados'
            else:
                message = 'Nenhum permissao encontrado'
                status = 208
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar permissaos: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Permissao, id=id)
                if querySet.status == 'eliminado':
                    pass
                serializer = PermissaoSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Permissao encontrado'
                else:
                    message = 'Nenhum Permissao encontrado'
                    status = 208
            except Http404:
                status = 208
                data = []
                message = 'Permissao não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Permissao: ' + str(e)
        
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
    

class PermissaoViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = PermissaoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Permissao criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar permissao: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar permissao: ' + str(e)
        
        return ResponseData(None, status, message)
    
class PermissaoViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request, id):
            try:
                querySet = get_object_or_404(Permissao, id=id)
                serializer = PermissaoSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Permissao atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar permissao: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar permissao: ' + str(e)
            
            return ResponseData(None, status, message)

class PermissaoViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request, id):
        try:
            querySet = get_object_or_404(Permissao, id=id)
            querySet.status = 'eliminado'
            querySet.save()
            status = 200
            message = 'Permissao deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar permissao: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    