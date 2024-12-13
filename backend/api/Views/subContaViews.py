from django.shortcuts import get_object_or_404
from api.models import SubConta, Conta
from rest_framework.views import APIView
from api.serializers import SubContaSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = SubConta.objects.raw(f"SELECT * FROM subSubConta WHERE {campo} like '{valor}'")
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
        return ResponseData(None, 500, 'Erro ao buscar subSubConta')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class SubContaViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = SubConta.objects.all()
            rows = querySet.count()
            serializer = SubContaSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'SubContas encontrados'
                for item in data:
                    item['conta'] = Conta.objects.get(id=item['conta_id']).numero
            else:
                message = 'Nenhum subSubConta encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar subSubContas: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(SubConta, id=id)
                serializer = SubContaSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'SubConta encontrado'
                else:
                    message = 'Nenhum SubConta encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'SubConta não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar SubConta: ' + str(e)
        
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
    

class SubContaViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = SubContaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'SubConta criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar subSubConta: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar subSubConta: ' + str(e)
        
        return ResponseData(None, status, message)
    
class SubContaViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request):
            try:
                querySet = get_object_or_404(SubConta, id=request.data['id'])
                serializer = SubContaSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'SubConta atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar subSubConta: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar subSubConta: ' + str(e)
            
            return ResponseData(None, status, message)

class SubContaViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(SubConta, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'SubConta deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar subSubConta: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    