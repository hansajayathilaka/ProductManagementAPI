from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        data = {
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'status': 'error',
            'message': str(exc),
        }
        response = Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        data = {
            'status_code': response.status_code,
            'status': 'error',
            'message': str(response.data['detail']),
        }
        response = Response(data, status=response.status_code)
    return response
