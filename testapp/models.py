from django.db import models

class Category(models.Model):
     name = models.CharField(max_length=50, unique=True)

     def __str__(self):
          return self.name


# Create your models here.
class Task(models.Model):
     title = models.CharField(max_length=30)
     description = models.TextField()
     categories = models.ManyToManyField(Category, blank=True)

     STATUS_CHOICES = (
          ("New", "New"),
          ("In progress", "In progress"),
          ("Pending", "Pending"),
          ("Blocked", "Blocked"),
          ("Done", "Done"),
     )
     status = models.CharField(STATUS_CHOICES, default='New')
     deadline = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title


class SubTask(models.Model):
     title = models.CharField(max_length=30)
     description = models.TextField()
     task = models.ForeignKey(Task, on_delete=models.CASCADE)
     STATUS_CHOICES = (
          ("New", "New"),
          ("In progress", "In progress"),
          ("Pending", "Pending"),
          ("Blocked", "Blocked"),
          ("Done", "Done"),
     )
     status = models.CharField(STATUS_CHOICES,
                             default='New')
     deadline = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.title

