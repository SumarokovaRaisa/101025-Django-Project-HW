
from django.urls import path

from testapp.views.tasks import (task_list,
                                 task_by_id,
                                 create_task,
                                 task_statistics)
from testapp.views.subtask import (SubTaskListCreateView,
                                   SubTaskDetailUpdateDeleteView,
                                   SubTaskPagination,
                                   SubTaskListView,
                                   SubTaskFilterListView)


urlpatterns = [
    path("task", task_list),
    path("<int:task_id>", task_by_id),
    path("create/", create_task),
    path("statistics/", task_statistics),

    path("subtasks/", SubTaskListCreateView.as_view(),
         name="subtask-list-create"),
    path("subtasks/<int:pk>/", SubTaskDetailUpdateDeleteView.as_view(),
         name="subtask-detail"),
    path("subtasks/list/", SubTaskListView.as_view(),
         name="subtask-list"),
    path("subtasks/filter/", SubTaskFilterListView.as_view(),
         name="subtask-filter"),
]