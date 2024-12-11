from django.shortcuts import render
from django.http import JsonResponse

def checkKey(request):
    if request.method == 'GET':
        if 'key' not in request.GET:
            return ResponseData(None, 400, 'Key not found')
        else:
            if request.GET('key') != '1234':
                return ResponseData(None, 400, 'Invalid Key')
        # else
        

def notFound(request):
    data = {
                'status': 404,
                'data': None,
                'message': 'Url Invalida!'
         }
    return JsonResponse(data, status=404, safe=False )

def outOfService(request):
    data = {
                'status': 503,
                'data': None,
                'message': 'Out of service'
         }
    return JsonResponse(data, status=503, safe=False ) 

def ResponseData(data = None, status=200, message = None, rows = None):
    data = {
                'rows': rows , # if rows is not None, return rows, else return 'len(data)
                'status': status,
                'message': message,
                'data': data,
         }
    return JsonResponse(data, status=status, safe=False )

def ResponseError(message, status=500):
    data = {
            'status': status,
            'message': message,
            'data': None
            }
    return JsonResponse(data, status=status, safe=False )


def ourData(request):
    data = [
        {
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "123456",
            "tipo_movimento": "OPR ref. 131325",
            "debito": 4560,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "111222",
            "tipo_movimento": "TAXA APLICADA ref. 131325",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "333444",
            "tipo_movimento": "TAXA APLICADA ref. 131325",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "556699",
            "tipo_movimento": "TAXA APLICADA ref. 131325",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "878787",
            "tipo_movimento": "OPR ref. 131326",
            "debito": 4560,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "656565",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "747474",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "959595",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "454543",
            "tipo_movimento": "OPR ref. 131354",
            "debito": 67500,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "998889",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "776776",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "665645",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "546534",
            "tipo_movimento": "OPR ref. 131332",
            "debito": 12007,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "212322",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "90909",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "99098",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "543211",
            "tipo_movimento": "OPR ref. 131322",
            "debito": 4323,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "444444",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "333333",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "666666",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "567865",
            "tipo_movimento": "OPR ref. 131222",
            "debito": 887700,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "222332",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "332345",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "665547",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "555433",
            "tipo_movimento": "OPR ref. 002211",
            "debito": 887700,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "890633",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "334245",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "766589",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        }
    ]

    return ResponseData(data, 200, 'Data found', len(data))

