from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    HIGH = 'high'
    LOW = 'low'
    MEDIUM = 'medium'
    PRIORITY_CHOICES = [
        (HIGH, 'high'),
        (MEDIUM, 'medium'),
        (LOW, 'low'),
    ]
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)

    def __str__(self):
        return self.title


