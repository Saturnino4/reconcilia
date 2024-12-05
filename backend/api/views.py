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


