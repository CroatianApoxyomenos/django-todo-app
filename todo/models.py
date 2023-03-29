from django.db import models
from django.urls import reverse


# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('list', args=[self.id])


class ToDoItem(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False, blank=False)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: due {self.due_date.date()}'
