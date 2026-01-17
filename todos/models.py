from django.db import models
from account.models import User
from .choices import StatusChoices, PriorityChoices

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    priority = models.CharField(max_length=10, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM)
    due_date = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title