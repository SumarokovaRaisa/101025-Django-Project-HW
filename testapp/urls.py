
from django.urls import path

# from testapp.views.tasks import (task_list,
#                                  task_by_id,
#                                  create_task,
#                                  task_statistics)
from testapp.views.tasks import (TaskListCreateView,
                                TaskDetailUpdateDeleteView)

from testapp.views.subtask import (SubTaskFilterListView,
                                   # SubTaskListCreateView,
#                                    SubTaskDetailUpdateDeleteView,
#                                    SubTaskPagination,
#                                    SubTaskListView,
                                    SubTasksListCreateAPIView,
                                    SubTasksRetrieveUpdateDestroyAPIView
                                )


urlpatterns = [
#     path("task", task_list),
#     path("<int:task_id>", task_by_id),
#     path("create/", create_task),
#     path("statistics/", task_statistics),
#
#     path("subtasks/", SubTaskListCreateView.as_view(),
#          name="subtask-list-create"),
#     path("subtasks/<int:pk>/", SubTaskDetailUpdateDeleteView.as_view(),
#          name="subtask-detail"),
#     path("subtasks/list/", SubTaskListView.as_view(),
#          name="subtask-list"),
    path("subtasks/filter/", SubTaskFilterListView.as_view(),
         name="subtask-filter"),
    path("tasks/", TaskListCreateView.as_view(),
         name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailUpdateDeleteView.as_view(),
         name="task-detail-update-delete"),
    path("subtasks/", SubTasksListCreateAPIView.as_view(),
         name="subtask-list-create"),
    path("subtasks/<int:pk>/", SubTasksRetrieveUpdateDestroyAPIView.as_view(),
         name="subtask-detail-update-delete"),
]