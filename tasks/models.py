from django.db import models

# User model represents the users in the system who can be assigned tasks.
class User(models.Model):
    # 'id' is an auto-incrementing primary key field added by default in Django.
    name = models.CharField(max_length=255)  # Name of the user (e.g., "Harsh G").
    email = models.EmailField(unique=True)   # Email address, must be unique for each user.
    mobile = models.CharField(max_length=15) # Mobile number (e.g., "+1234567890").

    # String representation of the model (makes the admin panel easier to use).
    def __str__(self):
        return self.name


# Task model represents tasks created and assigned to users.
class Task(models.Model):
    # 'id' is the primary key field that uniquely identifies each task.
    name = models.CharField(max_length=255)        # Name of the task (e.g., "Complete Report").
    description = models.TextField()              # Detailed description of the task.
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the task was created.
    task_type = models.CharField(max_length=100, blank=True)  # Type/category of the task (optional).
    completed_at = models.DateTimeField(null=True, blank=True)  # When the task was completed (optional).
    status = models.CharField(max_length=50, default="Pending")  # Status of the task (e.g., "Pending", "Completed").
    
    # Many-to-Many relationship: A task can be assigned to multiple users, and a user can have multiple tasks.
    assigned_users = models.ManyToManyField(User, related_name='tasks', blank=True)

    # String representation for admin panel or debugging.
    def __str__(self):
        return self.name
