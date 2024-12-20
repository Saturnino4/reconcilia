from django.shortcuts import get_object_or_404
from api.models import Banco
from rest_framework.views import APIView
from api.serializers import BancoSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = Banco.objects.raw(f"SELECT * FROM banco WHERE {campo} like '{valor}'")
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
        return ResponseData(None, 500, 'Erro ao buscar banco')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class BancoViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = Banco.objects.all()

            if 'nostro' in request.GET:
                print(f'Nostro: {request.GET["nostro"]}')
                if request.GET['nostro'] == '1':
                    querySet = querySet.filter(isnostra=1)
                else:
                    querySet = querySet.filter(isnostra=0)

            rows = querySet.count()
            serializer = BancoSerializer(querySet, many=True)
            data = serializer.data
            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Bancos encontrados'
            else:
                message = 'Nenhum banco encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar bancos: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Banco, id=id)
                serializer = BancoSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Banco encontrado'
                else:
                    message = 'Nenhum Banco encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Banco não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Banco: ' + str(e)
        
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
    

class BancoViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def post(self, request):
        try:
            serializer = BancoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'Banco criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar banco: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar banco: ' + str(e)
        
        return ResponseData(None, status, message)
    
class BancoViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def put(self, request):
            try:
                querySet = get_object_or_404(Banco, id=request.data['id'])
                serializer = BancoSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Banco atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar banco: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar banco: ' + str(e)
            
            return ResponseData(None, status, message)

class BancoViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(Banco, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Banco deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar banco: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    