from django.core.serializers import serialize
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from testapp.serializers.tasks import TaskSerializer
from testapp.models.models import Task

# Create your views here.
def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse("HELLO FROM MY  APP!!!!")


def user_greeting(request, user):
    return HttpResponse(f"HELLO {user}")


@api_view(["GET"])
def task_list(request):
    task = Task.objects.all()
    tasklist = TaskSerializer(task, many=Task)
    return Response(tasklist.data)


@api_view(["GET"])
def task_by_id(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task_data = TaskSerializer(task)
    return Response(
        task_data.data
    )


@api_view(["GET"])
def task_statistics(request):
    total_tasks = Task.objects.count()

    tasks_by_status = (
        Task.objects.values("status").annotate(count=Count("id"))
    )

    overdue_tasks = Task.objects.filter(
        deadline__lt=timezone.now()).count()

    return Response({
        "total_tasks": total_tasks,
        "tasks_by_status": list(tasks_by_status),
        "overdue_tasks": overdue_tasks
    })


api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

