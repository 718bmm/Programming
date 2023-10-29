from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    deadline = models.DateTimeField()
