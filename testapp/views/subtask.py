from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

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


class SubTaskPagination(PageNumberPagination):
    page_size = 5


class SubTaskListView(ListAPIView):
    queryset = SubTask.objects.all().order_by("-created_at")
    serializer_class = SubTaskSerializer
    pagination_class = SubTaskPagination


class SubTaskFilterListView(ListAPIView):
    serializer_class = SubTaskSerializer
    pagination_class = SubTaskPagination

    def get_queryset(self):
        queryset = SubTask.objects.all()

        main_task = self.request.query_params.get("main_task")
        status = self.request.query_params.get("status")


        if main_task:
            queryset = queryset.filter(task__title__icontains=main_task)

        if status:
            queryset = queryset.filter(status=status)


        return queryset.order_by("-created_at")

