from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
class ToDoView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoDetailView(APIView):
    def get_object(self, id):
        try:
            ToDo.objects.filter(id)
        except ToDo.DoesNotExist:
            raise Http404