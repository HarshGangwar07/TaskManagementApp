from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import Task, User
from .serializers import TaskSerializer

# 1. API to create a task
class CreateTaskAPIView(APIView):
    #This view handles the creation of new tasks.
    #A POST request to this view allows the client to create a task
    #with at least a name and description, and optionally, other fields.
    
    def post(self, request):
        # Deserialize the request data and validate it
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return validation errors if the input data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. API to assign a task to one or multiple users
class AssignTaskAPIView(APIView):
    # This view enables assigning a task to one or more users.
    # A POST request to this view requires the task_id as a URL parameter
    # and a list of user_ids in the request body to assign the task to these users.
    
    def post(self, request, task_id):
        try:
            # Get the task object by its ID
            task = Task.objects.get(id=task_id)
            # Retrieve the list of user IDs from the request
            user_ids = request.data.get('user_ids')
            if not user_ids:
                # Return an error if no user_ids are provided in the request
                return Response({'error': 'No user_ids provided'}, status=status.HTTP_400_BAD_REQUEST)
            # Assign the task to the provided users by setting the relationship
            task.assigned_users.set(user_ids)
            task.save()
            return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            # Return an error if the task with the given ID does not exist
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


# 3. API to get tasks with their details for a specific user
class UserTasksAPIView(APIView):
    #This view retrieves all tasks assigned to a specific user.
    #A GET request to this view requires the user_id as a URL parameter.
    #It returns a list of tasks assigned to the user in JSON format.

    def get(self, request, user_id):
        # Filter tasks where the user (by user_id) is in the assigned_users relationship
        tasks = Task.objects.filter(assigned_users__id=user_id)
        # Serialize the tasks to convert them into JSON format
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
