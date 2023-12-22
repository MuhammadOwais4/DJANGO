from rest_framework.decorators import api_view
from rest_framework.response import Response

persons = [
    {
        "id": "1",
        "name": "owais"
    }
]

@api_view(["GET"])
def get_persons(request):
    return Response(persons)
