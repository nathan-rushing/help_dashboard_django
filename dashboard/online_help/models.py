# Create your models here.
from django.db import models


# class User(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)  # Consider using Django's built-in User model for better security

#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"
    
class Writers(models.Model):
    writer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.writer_name}"


class Task(models.Model):
    document = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    sub_section = models.CharField(max_length=255)
    comments = models.TextField()
    SME = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    completion = models.CharField(max_length=100, default='0%')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"Task {self.id} - {self.document}"


class TaskWriter(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writers, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('task', 'writer')

    def __str__(self):
        return f"Writer {self.writer_id} for Task {self.task_id}"


class MajorDocu(models.Model):
    projects = models.CharField(max_length=255)
    SME = models.CharField(max_length=255)
    support = models.ForeignKey(Writers, on_delete=models.CASCADE, related_name='supported_docs')
    writer = models.ForeignKey(Writers, on_delete=models.CASCADE, related_name='written_docs')

    def __str__(self):
        return f"MajorDocu {self.id} - {self.projects}"
