from django.shortcuts import get_object_or_404
from api.models import Local
from rest_framework.views import APIView
from api.serializers import LocalSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = Local.objects.raw(f"SELECT * FROM local WHERE {campo} like '{valor}'")
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
        return ResponseData(None, 500, 'Erro ao buscar Local')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class LocalViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = Local.objects.all()
            rows = querySet.count()
            serializer = LocalSerializer(querySet, many=True)
            data = serializer.data

            # for item in data:
            #     del item['id']
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Locals encontradas'
            else:
                message = 'Nenhuma Local encontrada'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Locals: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Local, id=id)
                serializer = LocalSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Local encontrada'
                else:
                    message = 'Nenhuma Local encontrada'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Local não encontrada'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Local: ' + str(e)
        
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
        
    # def post(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
        
    # def delete(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
        
    # def put(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
    

class LocalViewsPost(APIView):

    # def get(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
    # def delete(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
        
    # def put(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = LocalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Local criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar Local: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar Local: ' + str(e)
        
        return ResponseData(None, status, message)
    
class LocalViewsPut(APIView):
        
        # def get(self, request):
        #     return ResponseData(None, 405, 'Method not allowed')
        
        # def delete(self, request):
        #     return ResponseData(None, 405, 'Method not allowed')
            
        # def post(self, request):
        #     return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request,id):
            try:
                querySet = get_object_or_404(Local, id=request.data['id'])
                serializer = LocalSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Local atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar Local: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar Local: ' + str(e)
            
            return ResponseData(None, status, message)

class LocalViewsDelete(APIView):
    # def get(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
    # def post(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
    # def put(self, request):
    #     return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request,id):
        try:
            querySet = get_object_or_404(Local, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Local deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar Local: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    