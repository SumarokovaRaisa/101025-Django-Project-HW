from django.contrib import admin

from testapp.models.models import Task, SubTask, Category


# Задание 1:
# Добавить настройку инлайн форм для админ класса задач. При создании задачи
# должна появиться возможность создавать сразу и подзадачу.

class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "deadline", "created_at", "short_title" )
    search_fields = ("title",)
    list_filter = ("status",)
    inlines = [SubTaskInline]

#     Задание 2:
# Названия задач могут быть длинными и ухудшать читаемость в Админ панели,
# поэтому требуется выводить в списке задач укороченный вариант – первые 10 символов
# с добавлением «...», если название длиннее, при этом при выборе задачи для создания
# подзадачи должно отображаться полное название. Необходимо реализовать такую возможность.

    @admin.display(description="Название")
    def short_title(self, obj):
        if len(obj.title) > 10:
            return f"{obj.title[:10]}..."
        return obj.title

# Задание 3:
# Реализовать свой action для Подзадач, который поможет выводить выбранные в Админ
# панели объекты в статус Done


@admin.action(description="Отметить выбранные подзадачи как 'Done' ")
def make_subtask_done(modeladmin, request, queryset):
    queryset.update(status="Done")


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("id","title", "task", "status")
    search_fields = ("title",)
    list_filter = ("status",)
    actions = [make_subtask_done]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

