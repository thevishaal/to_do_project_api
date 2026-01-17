from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TodoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.filter(user=request.user, is_deleted=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({"msg": "Todo Created Successfully!"}, status=status.HTTP_201_CREATED)


class TodoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_todo(self, pk, user):
        return get_object_or_404(Todo, pk=pk, user=user, is_deleted=False)
    
    def get(self, request, pk):
        todo = self.get_todo(pk, request.user)
        serializer = TodoSerializer(todo)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        todo = self.get_todo(pk, request.user)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Todo update", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        todo = self.get_todo(pk, request.user)
        todo.is_deleted = True
        todo.save()
        return Response({"msg": "Todo deleted Successfully!"}, status=status.HTTP_204_NO_CONTENT)