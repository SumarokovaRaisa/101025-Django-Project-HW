from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from testapp.models.models import SubTask
from testapp.serializers.subtask import SubTaskSerializer


class SubTaskListCreateView(APIView):

    def get(self, request):
        subtasks = SubTask.objects.all()
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubTaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class SubTaskDetailUpdateDeleteView(APIView):

    def get_object(self, pk):
        return get_object_or_404(SubTask, pk=pk)


    def get(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)


    def put(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskSerializer(
            subtask,
            data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        subtask.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )