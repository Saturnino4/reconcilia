from django.shortcuts import get_object_or_404
from api.models import Conta, SubConta, Banco
from rest_framework.views import APIView
from api.serializers import ContaSerializer, SubContaSerializer
from api.views import ResponseData
from django.http import Http404



def getByAnyColumn(request,campo,valor):
    rows = 0
    try:
        querySet = Conta.objects.raw(f"SELECT * FROM conta WHERE {campo} like '{valor}'")
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
        return ResponseData(None, 500, 'Erro ao buscar conta')

    return ResponseData(data, 200, "Daods retornados com sucesso")
   


class ContaViewsGet(APIView):


    def getAll(self, request):

        # if 'dia' in request.GET and 'mes' in request.GET and 'ano' in request.GET:

        try:
            querySet = Conta.objects.all()

            if 'banco_id' in request.GET:
                querySet = querySet.filter(banco_id=request.GET['banco_id'])

            if 'nostro' in request.GET:
                querySet = querySet.filter(isnostra=request.GET['nostro'])

                if 'banco_id' in request.GET:
                    querySet = querySet.filter(banco_id=request.GET['banco_id'])
                # if request.GET['nostro'] == '1':
                #     querySet = querySet.filter(isnostra=1)
                # else:
                #     querySet = querySet.filter(isnostra=0)

                if 'nocorrspondente' in request.GET:
                    contasWithOutCorrespondenteQuery = Conta.objects.raw("""
                        SELECT * FROM conta WHERE id NOT IN (
                            SELECT conta_id FROM nostro_vostro WHERE subconta_id NOT IN (
                                SELECT id FROM subconta WHERE nome = 'correspondente'
                            )
                        )
                    """)

                    querySet = querySet.filter(id__in=[item.id for item in contasWithOutCorrespondenteQuery])


           
            rows = querySet.count()
            serializer = ContaSerializer(querySet, many=True)
            data = serializer.data



            
            # data['perfil_nome'] = PerfilSerializer
            if len(data) > 0:
                status = 200
                message = 'Contas encontrados'
            else:
                message = 'Nenhum conta encontrado'
                status = 404
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar contas: ' + str(e)
            
        return {'status': status, 'data': data,'message': message, 'rows': rows if 'rows' in locals() else 0 }
            

    def getById(self, request, id):
        
        try:
            try:
                querySet = get_object_or_404(Conta, id=id)
                serializer = ContaSerializer(querySet)
                data = serializer.data

                if len(data) > 0:
                    status = 200
                    message = 'Conta encontrado'
                else:
                    message = 'Nenhum Conta encontrado'
                    status = 404
            except Http404:
                status = 404
                data = []
                message = 'Conta não encontrado'
        except Exception as e:
            status = 500
            data = []
            message = 'Erro ao buscar Conta: ' + str(e)
        
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
    

class ContaViewsPost(APIView):

    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def delete(self, request):
        return ResponseData(None, 405, 'Method not allowed')
        
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def registrarSubConta(self, data):
        try:
            serializer = SubContaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                status = 201
                message = 'SubConta criado com sucesso'
            else:
                status = 400
                message = 'Erro ao criar SubConta: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar SubConta: ' + str(e)

        return {'status': status, 'message': message}

        
    def post(self, request):
        try:

            if request.data['isnostra'] == 1:
                subconta_nome = request.data['subconta_nome']
                del request.data['subconta_nome']
                if 'conta_id' in request.GET:
                    subcontaData = {
                        'conta_id': request.GET['conta_id'],
                        'nome': subconta_nome
                    }
                    if self.registrarSubConta(subcontaData)['status'] == 201:
                        status = 201
                        message = 'SubConta criado com sucesso'
                    else:
                        status = 201
                        message = 'Houve um erro ao criar a SubConta'
                else:        
                    serializer = ContaSerializer(data=request.data)
                    if serializer.is_valid():
                        conta = serializer.save()
                        subcontaData = {
                            'conta_id': conta.id,
                            'nome': subconta_nome
                        }
                        if self.registrarSubConta(subcontaData)['status'] == 201:
                            status = 201
                            message = 'Conta e SubConta criados com sucesso'
                        else:
                            status = 201
                            message = 'Conta criado com sucesso, mas houve um erro ao criar a SubConta'
                            
                    else:
                        status = 400
                        message = 'Erro ao criar conta: ' + str(serializer.errors)
            else:
                if 'subconta_nome' in request.data:
                    del request.data['subconta_nome']
                serializer = ContaSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 201
                    message = 'Conta criado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao criar conta: ' + str(serializer.errors)
        except Exception as e:
            status = 500
            message = 'Erro ao criar conta: ' + str(e)
        
        return ResponseData(None, status, message)
    
class ContaViewsPut(APIView):
        
        def get(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def delete(self, request):
            return ResponseData(None, 405, 'Method not allowed')
            
        def post(self, request):
            return ResponseData(None, 405, 'Method not allowed')
        
        def editarSubConta(self, data):
            try:
                querySet = get_object_or_404(SubConta, conta_id=data['conta_id'])
                serializer = SubContaSerializer(querySet, data=data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'SubConta atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar SubConta: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar SubConta: ' + str(e)

            return {'status': status, 'message': message}
            
        def put(self, request):
            try:
                querySet = get_object_or_404(Conta, id=request.data['id'])
                serializer = ContaSerializer(querySet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    status = 200
                    message = 'Conta atualizado com sucesso'
                else:
                    status = 400
                    message = 'Erro ao atualizar conta: ' + str(serializer.errors)
            except Exception as e:
                status = 500
                message = 'Erro ao atualizar conta: ' + str(e)
            
            return ResponseData(None, status, message)

class ContaViewsDelete(APIView):
    def get(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def post(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    def put(self, request):
        return ResponseData(None, 405, 'Method not allowed')
    
    def delete(self, request):
        try:
            querySet = get_object_or_404(Conta, id=request.data['id'])
            querySet.delete()
            status = 200
            message = 'Conta deletado com sucesso'
        except Exception as e:
            status = 500
            message = 'Erro ao deletar conta: ' + str(e)
        
        return ResponseData(None, status, message)
    


        
    