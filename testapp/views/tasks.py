
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from testapp.serializers.tasks import TaskSerializer
from testapp.models.models import Task

# Create your views here.
def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse("HELLO FROM MY  APP!!!!")


def user_greeting(request, user):
    return HttpResponse(f"HELLO {user}")


# @api_view(["GET"])
# def task_list(request):
#     task = Task.objects.all()
#     tasklist = TaskSerializer(task, many=Task)
#     return Response(tasklist.data)
#
#
# @api_view(["GET"])
# def task_by_id(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task_data = TaskSerializer(task)
#     return Response(
#         task_data.data
#     )
#
#
# @api_view(["GET"])
# def task_statistics(request):
#     total_tasks = Task.objects.count()
#
#     tasks_by_status = (
#         Task.objects.values("status").annotate(count=Count("id"))
#     )
#
#     overdue_tasks = Task.objects.filter(
#         deadline__lt=timezone.now()).count()
#
#     return Response({
#         "total_tasks": total_tasks,
#         "tasks_by_status": list(tasks_by_status),
#         "overdue_tasks": overdue_tasks
#     })
#
#
# api_view(["POST"])
# def create_task(request):
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,
#                         status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors,
#                     status=status.HTTP_400_BAD_REQUEST)
#

class TaskListByDayView(ListAPIView):
    serializer_class = TaskSerializer


    def get_queryset(self):
        queryset = Task.objects.all()
        weekday = self.request.query_params.get("weekday")

        if weekday:
            queryset = queryset.filter(created_at__weekday=weekday)

        return queryset

# Домашнее задание: Замена функций представлений на Generic Views для задач и подзадач
# Используя Generic Views, замените существующие классы представлений
# для задач (Tasks) и подзадач (SubTasks) на соответствующие классы
# для полного CRUD (Create, Read, Update, Delete) функционала.
# Агрегирующий эндпойнт для статистики задач оставьте как есть.
# Реализуйте, фильтрацию, поиск и сортировку для этих наборов представлений.
# Задание 1: Замена представлений для задач (Tasks) на Generic Views
# Шаги для выполнения:
# Замените классы представлений для задач на Generic Views:
# Используйте ListCreateAPIView для создания и получения списка задач.
# Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления задач.
# Реализуйте фильтрацию, поиск и сортировку:
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ["status", "deadline"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at"]
    ordering = ["created_at"]


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

