from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from testapp.models.models import Category
from testapp.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'], url_path='count-tasks')
    def count_tasks(self, request, pk=None):

        category = self.get_object()

        tasks_count = category.task_set.count()

        return Response({
            'category_id': category.id,
            'category_name': category.name,
            'tasks_count': tasks_count
        }, status=status.HTTP_200_OK)