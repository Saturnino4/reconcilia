from django.shortcuts import get_object_or_404
from api.models import Utilizador, Role
from rest_framework.views import APIView
from api.serializers import UtilizadorSerializer, RoleSerializer
from api.views import ResponseData
from django.http import Http404


class LoginViews(APIView):
    def post(self,request):
        # trying += 1
        username = request.data['username']
        password = request.data['password']

        try:
            querySet = Utilizador.objects.get(username=username,password=password)
            
            user = UtilizadorSerializer(querySet).data
            
            # if user['status'] is 'eliminado':
            #     pass            
            
            try:
                roleQuery = Role.objects.get(id=user['role_id'])
                role = RoleSerializer(roleQuery).data
            except Exception as e:
                role = []
                print(f'Utilizador sem role.... {e}')

            return ResponseData({'user':user,'role':role},200,'success login')
        except Exception as e:
            return ResponseData({'user':{},'role':[]},400,f'Fail to login: {e}')

     

class UtilizadorViewsGet(APIView):

    def getFreeUtilizador(self,request):
        try:
            if 'utilizador_id' in request.GET:
                id = request.GET['utilizador_id']
                querySet = Utilizador.objects.raw("""
                    SELECT  utilizador.* FROM utilizador 
                    LEFT JOIN funcionario ON utilizador.id = funcionario.utilizador_id
                    WHERE funcionario.utilizador_id IS NULL OR utilizador.id = %s and utilizador.status != 'eliminado'
                """, [id])
            else:    
                # querySet = Utilizador.objects.raw("""
                #     select DISTINCT utilizador.* from utilizador inner join funcionario
                #     where utilizador.id != funcionario.utilizador_id 
                # """)
               querySet = Utilizador.objects.raw("""
                    SELECT  utilizador.* FROM utilizador 
                    LEFT JOIN funcionario ON utilizador.id = funcionario.utilizador_id
                    WHERE funcionario.utilizador_id IS NULL and utilizador.status != 'eliminado'
                """)

            serializer = UtilizadorSerializer(querySet, many=True)
            data = serializer.data
            if len(data) > 0:
                status = 200
                message = 'Utilizadores encontrados'
            else:
                message = 'Nenhum utilizador encontrado'
                status = 200

        except Exception as e:
            status = 500
            data = []
            message = f'Erro ao buscar utilizadores livres: {str(e)}'
        return {'status': status, 'data': data, 'message': message}

    def getByAnyColumn(self, request,campo,valor):
        try:
            if 'exact' in request.GET:
                querySet = Utilizador.objects.filter(**{campo: valor}).exclude(status='eliminado')
            else:
                querySet = Utilizador.objects.filter(**{campo + '__icontains': valor}).exclude(status='eliminado')
            rows = querySet.count()
            serializer = UtilizadorSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Utilizadores encontrados'
            else:
                message = 'Nenhum utilizador encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar utilizadores: ' + str(e)

        return {'status': status, 'data': data,'message': message, 'rows': rows }

    def getAll(self, request):
        try:
            querySet = Utilizador.objects.all().exclude(status='eliminado')
            rows = querySet.count()
            serializer = UtilizadorSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Utilizadores encontrados'
            else:
                message = 'Nenhum utilizador encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar utilizadores: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Utilizador, id=id)
                if querySet.status == 'eliminado':
                    pass
                serializer = UtilizadorSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Utilizador encontrado'
                else:
                    message = 'Nenhum utilizador encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Utilizador não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar utilizador: ' + str(e)
        
        return {'status': status, 'data': data, 'message': message}

    def get(self, request, id=None):


        if id is not None: 
            res = self.getById(request, id)
            return ResponseData(res['data'], res['status'], res['message'])
            # return ResponseData([], 200, "teste")
        
        if id is None and 'campo' in request.GET and 'valor' in request.GET:
            res = self.getByAnyColumn(request, request.GET['campo'], request.GET['valor'])
            return ResponseData(res['data'], res['status'], res['message'])
        if id is None and 'free' in request.GET:
            if request.GET['free'] == 'true':
                # return ResponseData(None, 200, 'teste')
                res = self.getFreeUtilizador(request=request)
                return ResponseData(res['data'], res['status'], res['message'])
            else:
                pass
        else:
            res = self.getAll(request)
            return ResponseData(res['data'], res['status'], res['message'])

        
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    

class UtilizadorViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = UtilizadorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Utilizador criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar utilizador: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar utilizador: ' + str(e)
        
        return ResponseData(None, status, message)
    
class UtilizadorViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request, id):
            try:
                querySet = get_object_or_404(Utilizador, id=id)
                serializer = UtilizadorSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Utilizador atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar utilizador: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar utilizador: ' + str(e)
            
            return ResponseData(None, status, message)

class UtilizadorViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request, id):
        try:
            querySet = get_object_or_404(Utilizador, id=id)

            querySet.status = 'eliminado'
            querySet.save()
            status = 200
            message = 'Utilizador deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar utilizador: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    