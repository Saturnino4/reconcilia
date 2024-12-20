from api.views import ResponseData, ourData, extratoData
from rest_framework.views import APIView


class ReconciliacaoView(APIView):
    
    def post(self, request):

        # uri = request.build_absolute_uri()

        if 'nostro' in request.GET:
            if request.GET['nostro'] == '1':
                data = []
                # for item in
                
                filters = request.data
                # print('Yuuuuuuuuuuuuuuurrrrrrrrr: ', filters)

                if 'data_inicio' in filters and 'data_fim' in filters:
                    print('nostro came: ',filters['data_inicio'])
                    for item in ourData(request, True):
                        # if item['data_mov'] >= filters['data_inicio'] and item['data_mov'] <= filters['data_fim']: 
                        if item['data_mov'] >= filters['data_inicio'] and item['data_mov'] <= filters['data_fim']: 
                            data.append(item) 
                        # if item['data_mov'] >= filters['data_inicio']: #  and item['data_mov'] <= filters['data_fim']
                            # data.append(item)

                    # for item in extratoData(request, True):
                    #     if item['data_mov'] == filters['data_inicio']: 
                    #         data.append(item)    

                    return ResponseData(data, 200, 'Nosso extrato encontrado')

                return ResponseData(data, 200, 'Extrato nostro encontrado')




                return ourData(request)
            else:
                return ResponseData([], 503, 'Extrato vostro nao disponivel ainda')

        return ResponseData({
            'uri':'/reconciliacao/'
        }, 200, 'ReconciliacaoView')
    
        