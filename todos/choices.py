from django.db import models

class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    COMPLETED = 'COMPLETED', 'Completed'
    ARCHIVED = 'ARCHIVED', 'Archived'


class PriorityChoices(models.TextChoices):
    LOW = 'LOW', 'Low'
    MEDIUM = 'MEDIUM', 'Medium'
    HIGH = 'HIGH', 'High'