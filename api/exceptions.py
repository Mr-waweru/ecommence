from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Custom exception handler to manage specific exceptions like IntegrityError.
    """
    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError):
        if "UNIQUE constraint failed" in str(exc):
            return Response(
                {"error": "A record with this value already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    return response
