from django.contrib import admin
from testapp.models import Task, SubTask, Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "deadline", "created_at")
    search_fields = ("title",)
    list_filter = ("status",)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("id","title", "task", "status")
    search_fields = ("title",)
    list_filter = ("status",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

