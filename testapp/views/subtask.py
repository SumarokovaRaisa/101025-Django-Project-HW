from rest_framework.generics import get_object_or_404
from rest_framework.generics import (ListAPIView,
                                    ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from testapp.models.models import SubTask
from testapp.serializers.subtask import SubTaskSerializer


# class SubTaskListCreateView(APIView):
#
#     def get(self, request):
#         subtasks = SubTask.objects.all()
#         serializer = SubTaskSerializer(subtasks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SubTaskSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

# class SubTaskDetailUpdateDeleteView(APIView):
#
#     def get_object(self, pk):
#         return get_object_or_404(SubTask, pk=pk)
#
#
#     def get(self, request, pk):
#         subtask = self.get_object(pk)
#         serializer = SubTaskSerializer(subtask)
#         return Response(serializer.data)
#
#
#     def put(self, request, pk):
#         subtask = self.get_object(pk)
#         serializer = SubTaskSerializer(
#             subtask,
#             data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
#
#     def delete(self, request, pk):
#         subtask = self.get_object(pk)
#         subtask.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )


class SubTaskPagination(PageNumberPagination):
    page_size = 5


# class SubTaskListView(ListAPIView):
#     queryset = SubTask.objects.all().order_by("-created_at")
#     serializer_class = SubTaskSerializer
#     pagination_class = SubTaskPagination


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

# Задание 2: Замена представлений для подзадач (SubTasks) на Generic Views
# Шаги для выполнения:
# Замените классы представлений для подзадач на Generic Views:
# Используйте ListCreateAPIView для создания и получения списка подзадач.
# Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления подзадач.
# Реализуйте фильтрацию, поиск и сортировку:
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.

class SubTasksListCreateAPIView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]

    filterset_fields = ["status", "deadline"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at"]
    ordering = ["created_at"]


class SubTasksRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer