from django.urls import path
from .views import CreateTaskAPIView, AssignTaskAPIView, UserTasksAPIView

# URL patterns for the task management API
urlpatterns = [
    # 1. URL for creating a new task
    # This maps to the CreateTaskAPIView and handles POST requests to create a task.
    path('tasks/create/', CreateTaskAPIView.as_view(), name='create-task'),

    # 2. URL for assigning a task to users
    # This maps to the AssignTaskAPIView and handles POST requests for assigning a task to one or multiple users.
    # The <int:task_id> in the URL captures the task ID as a parameter and passes it to the view.
    path('tasks/assign/<int:task_id>/', AssignTaskAPIView.as_view(), name='assign-task'),

    # 3. URL for retrieving tasks assigned to a specific user
    # This maps to the UserTasksAPIView and handles GET requests for fetching tasks for a particular user.
    # The <int:user_id> in the URL captures the user ID as a parameter and passes it to the view.
    path('tasks/user/<int:user_id>/', UserTasksAPIView.as_view(), name='user-tasks'),
]
