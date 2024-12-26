from api.views import ResponseData, ourData, extratoData
from rest_framework.views import APIView


class ReconciliacaoView(APIView):
    

    def reconciliar(self, swift, nostro):
        nostroNotMatched = []
        swiftNotMatched = []

        # return [nostro, swift]
        
        print('Chegou aqui at least...............')

        # Extract swift references
        swift_refs = {}
        for swift_item in swift:
            ref = swift_item['reference']
            if 'REF' not in ref:
                ref_num = ref.split('.')[-1]
            else:
                ref_num = ref.split(': ')[-1]
            swift_refs[ref_num] = swift_item
        
        # Extract nostro references
        nostro_refs = {}
        for nostro_item in nostro:
            ref_num = nostro_item['tipo_movimento'].split(' ')[-1]
            nostro_refs[ref_num] = nostro_item
    
        # Find unmatched items
        for ref, item in swift_refs.items():
            if ref not in nostro_refs:
                nostroNotMatched.append(item)
                
        for ref, item in nostro_refs.items():
            if ref not in swift_refs:
                swiftNotMatched.append(item)

        # print ('Nostro not matched: ', nostroNotMatched)
        # print ('Swift not matched: ', swiftNotMatched)
                        
        return nostroNotMatched, swiftNotMatched
       



    def post(self, request):

        # uri = request.build_absolute_uri()


        # return ResponseData(self.reconciliar(extratoData(request,True), ourData(request,True)), 200, 'ReconciliacaoView')

        if 'nostro' in request.GET:
            if request.GET['nostro'] == '1':
                data = {
                    'nostro': [],
                    'extrato': []
                }
                # for item in
                
                filters = request.data
                # print('Yuuuuuuuuuuuuuuurrrrrrrrr: ', filters)

                if 'data_inicio' in filters and 'data_fim' in filters:
                    # print('nostro came: ',filters['data_inicio']) 
                    for item in ourData(request, True):
                        # if item['data_mov'] >= filters['data_inicio'] and item['data_mov'] <= filters['data_fim']: 
                        if item['data_mov'] >= filters['data_inicio'] and item['data_mov'] <= filters['data_fim']: 
                            data['nostro'].append(item)
                        # if item['data_mov'] >= filters['data_inicio']: #  and item['data_mov'] <= filters['data_fim']
                            # data.append(item)

                    for item in extratoData(request, True):
                        if item['data'] >= filters['data_inicio'] and item['data'] <= filters['data_fim']:
                            data['extrato'].append(item)  
                    # return ResponseData(self.reconciliar(data['extrato'], data['nostro']), 200, 'ReconciliacaoView')
                    return ResponseData(data, 200, 'Nosso extrato encontrado')
                # return self.reconciliar(data['extrato'], data['nostro'])
                return ResponseData(data, 200, 'Extrato nostro encontrado')




                return ourData(request)
            else:
                return ResponseData([], 503, 'Extrato vostro nao disponivel ainda')

        return ResponseData({
            'uri':'/reconciliacao/'
        }, 200, 'ReconciliacaoView')
    
        