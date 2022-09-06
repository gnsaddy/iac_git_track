from django.http import JsonResponse

# success response


def success_response(message, data=None):
    return JsonResponse({
        'status': 'success',
        'message': message,
        'data': data
    }, safe=False, status=200)

# error response


def error_response(message, data=None):
    return JsonResponse({
        'status': 'error',
        'message': message,
        'data': data
    }, safe=False, status=200)
