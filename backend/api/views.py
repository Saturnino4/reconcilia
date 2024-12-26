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


def ourData(request,data_only=False):
    data = [
        {
            # "id": 1,
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "123456",
            "tipo_movimento": "OPR ref. 9635696002DBNJ51",
            "debito": 4560,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 2,
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "111222",
            "tipo_movimento": "TAXA APLICADA ref. 9635696004DBNJ52",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 3,
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "333444",
            "tipo_movimento": "TAXA APLICADA ref. 9635696004DBNJ45",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 4,
            "data_mov": "10/10/2024",
            "da_ccb": "123456-7",
            "documento": "556699",
            "tipo_movimento": "TAXA APLICADA ref. 131325",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 5,
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "878787",
            "tipo_movimento": "OPR ref. 131326",
            "debito": 4560,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 6,
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "656565",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 7,
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "747474",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 8,
            "data_mov": "12/10/2024",
            "da_ccb": "123457-9",
            "documento": "959595",
            "tipo_movimento": "TAXA APLICADA ref. 131326",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 9,
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "454543",
            "tipo_movimento": "OPR ref. 131354",
            "debito": 67500,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 10,
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "998889",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 11,
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "776776",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 12,
            "data_mov": "15/10/2024",
            "da_ccb": "123456-8",
            "documento": "665645",
            "tipo_movimento": "TAXA APLICADA ref. 131354",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 13,
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "546534",
            "tipo_movimento": "OPR ref. 131332",
            "debito": 12007,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 14,
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "212322",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 15,
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "90909",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 16,
            "data_mov": "16/10/2024",
            "da_ccb": "123456-0",
            "documento": "99098",
            "tipo_movimento": "TAXA APLICADA ref. 131332",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 17,
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "543211",
            "tipo_movimento": "OPR ref. 131322",
            "debito": 4323,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 18,
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "444444",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 19,
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "333333",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 20,
            "data_mov": "18/10/2024",
            "da_ccb": "123456-2",
            "documento": "666666",
            "tipo_movimento": "TAXA APLICADA ref. 131322",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 21,
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "567865",
            "tipo_movimento": "OPR ref. 131222",
            "debito": 887700,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 22,
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "222332",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 23,
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "332345",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 24,
            "data_mov": "22/10/2024",
            "da_ccb": "123456-1",
            "documento": "665547",
            "tipo_movimento": "TAXA APLICADA ref. 131222",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 25,
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "555433",
            "tipo_movimento": "OPR ref. 002211",
            "debito": 887700,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 26,
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "890633",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 27,
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "334245",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        },
        {
            # "id": 28,
            "data_mov": "28/10/2024",
            "da_ccb": "123456-1",
            "documento": "766589",
            "tipo_movimento": "TAXA APLICADA ref. 002211",
            "debito": 9,
            "credito": 0,
            "saldo_pos": 12000
        }
    ]

    if data_only:
        return data
    return ResponseData(data, 200, 'Data found', len(data))


def extratoData(request, data_only=False):
    data = [
        {
            "id": 1,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "57318825/OPE 1896356960DBNJ45 9001ORD.P.REC.9635696004DBNJ45",
            "amount": 4771.00,
            "ma": "D",
        },
        {
            "id": 2,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "ORD.P.EMI 9635696002DBNJ51 9001N.REF: 9635696002DBNJ51",
            "amount": 4771.00,
            "ma": "D",
        },
        {
            "id": 3,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "57325510/OPE 1896356960DBNJ52 9001ORD.P.REC.9635696004DBNJ52",
            "amount": 4771.00,
            "ma": "C",
        },
        {
            "id": 4,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "ORD.P.EMI. 9635696002DBNJ58 9001N.REF: 9635696002DBNJ58",
            "amount": 4771.00,
            "ma": "C",
        },
        {
            "id": 5,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "57325510/OPE 1896356960DBNJ59 9001ORD.P.REC.9635696004DBNJ59",
            "amount": 4771.00,
            "ma": "D",
        },
        {
            "id": 6,
            "data": "10/10/2024",
            "value":  241009,
            "entr": 1009,
            "F": None,
            "code": "NTRF",
            "reference": "ORD.P.EMI. 9635696002DBNJ60 9001N.REF: 9635696002DBNJ60",
            "amount": 4771.00,
            "ma": "D",
        }

    ]

    if data_only:
        return data

    return ResponseData(data, 200, 'Data found', len(data))


