from api.views import ResponseData

class CheckKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            if 'key' not in request.GET:
                return ResponseData(None, 400, 'Key not found')

        response = self.get_response(request)

        return response