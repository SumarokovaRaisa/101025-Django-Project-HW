from django.db import models
from django.utils import timezone

class NonDeletedCategoryManager(models.Manager):

     def get_queryset(self):
          return super().get_queryset().filter(is_deleted=False)

class Category(models.Model):
     name = models.CharField(max_length=50, unique=True, verbose_name="Category")

     is_deleted = models.BooleanField(default=False, verbose_name="Deleted")
     deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Date of deletion")

     objects = NonDeletedCategoryManager()
     all_objects = models.Manager()


     def __str__(self):
          return self.name


     class Meta:
          db_table = "task_manager_category"
          verbose_name = "Category"

     def delete(self, *args, **kwargs):
          self.is_deleted = True
          self.deleted_at = timezone.now()
          self.save()



class Task(models.Model):
     title = models.CharField(max_length=30, unique=True)
     description = models.TextField()
     categories = models.ManyToManyField(Category, blank=True)

     STATUS_CHOICES = (
          ("New", "New"),
          ("In progress", "In progress"),
          ("Pending", "Pending"),
          ("Blocked", "Blocked"),
          ("Done", "Done"),
     )
     status = models.CharField(max_length=20,
                               choices=STATUS_CHOICES,
                               default='New')
     deadline = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title


     class Meta:
          db_table = "task_manager_task"
          verbose_name = "Task"
          ordering = ["-created_at"]



class SubTask(models.Model):
     title = models.CharField(max_length=30, unique=True)
     description = models.TextField()
     task = models.ForeignKey(Task, on_delete=models.CASCADE)
     related_name = "subtasks"
     STATUS_CHOICES = (
          ("New", "New"),
          ("In progress", "In progress"),
          ("Pending", "Pending"),
          ("Blocked", "Blocked"),
          ("Done", "Done"),
     )
     status = models.CharField(max_length=20,
                               choices=STATUS_CHOICES,
                               default='New')
     deadline = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title


     class Meta:
          db_table = "task_manager_subtask"
          ordering = ["-created_at"]
          verbose_name = "SubTask"

