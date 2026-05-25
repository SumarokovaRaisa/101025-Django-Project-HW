
"""
Домашнее задание: Проект "Менеджер задач" — ORM запросы
Цель:
Освоение основных операций CRUD (Create, Read, Update, Delete) на примере заданных моделей.
Выполните запросы:
Создание записей:
Task:
title: "Prepare presentation".
description: "Prepare materials and slides for the presentation".
status: "New".
deadline: Today's date + 3 days."""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Manager.settings')

django.setup()
from testapp.models import Task, SubTask
from django.utils import timezone

# Task.objects.filter(title="Prepare presentation").delete()  для удаления лишней задачи в базе данных

new_task = Task.objects.create(title="Prepare presentation",
                              description="Prepare materials and slides for the presentation",
                              status="New",
                              deadline=timezone.now() + timezone.timedelta(days=3))

print(f"Задача создана успешно! ID: {new_task.id}")


"""SubTasks для "Prepare presentation":
title: "Gather information".
description: "Find necessary information for the presentation".
status: "New".
deadline: Today's date + 2 days.
title: "Create slides".
description: "Create presentation slides".
status: "New".
deadline: Today's date + 1 day."""

parent_task = Task.objects.get(title="Prepare presentation")

new_subtask_1 = SubTask.objects.create(title="Gather information",
                              description="Find necessary information for the presentation",
                              status="New",
                              deadline=timezone.now() + timezone.timedelta(days=2),
                              task=parent_task)

new_subtask_2 = SubTask.objects.create(title="Create slides",
                              description="Create presentation slides",
                              status="New",
                              deadline=timezone.now() + timezone.timedelta(days=1),
                              task=parent_task)

print("2 подзадачи успешно созданы!")


"""Чтение записей:
Tasks со статусом "New":
Вывести все задачи, у которых статус "New".
SubTasks с просроченным статусом "Done":
Вывести все подзадачи, у которых статус "Done", но срок выполнения истек."""

from django.db.models import Q, F

new_tasks = Task.objects.filter(status="New")

done_subtasks = SubTask.objects.filter(
    Q(status="Done")  &  Q(deadline__lt=timezone.now())
    )


print("--- Задачи со статусом 'New' ---")
for task in new_tasks:
    print(f"- {task.title} (Статус: {task.status})")

if done_subtasks:
    print("\n--- Просроченные выполненные подзадачи ---")

for subtask in done_subtasks:
    print(f"- {subtask.title} (Дедлайн был: {subtask.deadline})")
else:
    print("\n--- Просроченных подзадач нет  ---")



"""Изменение записей:
Измените статус "Prepare presentation" на "In progress".
Измените срок выполнения для "Gather information" на два дня назад.
Измените описание для "Create slides" на "Create and format presentation slides"."""

Task.objects.filter(title="Prepare presentation").update(
    status="In progress")
task = Task.objects.get(title="Prepare presentation")
print(f"\nЗадача - {task.title}, статус - {task.status}")

SubTask.objects.filter(title="Gather information").update(
    deadline=F("deadline") - timezone.timedelta(days=2))
subtask = SubTask.objects.get(title="Gather information")
formated_subtask = subtask.deadline.strftime('%Y-%m-%d')
print(f"\nПодзадача - {subtask.title}, дедлайн - {formated_subtask}")

SubTask.objects.filter(title="Create slides").update(
    description="Create and format presentation slide")
changed = SubTask.objects.get(title="Create slides")
print(f"\nПодзадача - {changed.title}, измененное описание - {changed.description}")


"""Удаление записей:
Удалите задачу "Prepare presentation" и все ее подзадачи.
"""

task_deleted = Task.objects.filter(title="Prepare presentation").delete()