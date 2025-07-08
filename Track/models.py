from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        {'to_do', 'Зробити'},
        {'in_progres', 'В Процесі'},
        {'completed', 'Готово'}
    ]
    PRIORITY_CHOICES = [
        {'low', 'Низький'},
        {'medium', 'Середній'},
        {'high', 'Високий'}
    ]
    title = models.CharField(max_length=40)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='to_do')
    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES, default='low')
    due_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='tasks)

    def __str__(self):
        return self.title