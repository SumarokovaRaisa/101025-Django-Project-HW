from django.utils import timezone
from rest_framework import serializers
from testapp.models.models import Task, SubTask
from testapp.serializers.subtask import SubTaskSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "deadline"]


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = "__all__"


    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Дата выполнения не может быть в прошлом."
            )
        return value





class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
