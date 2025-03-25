from rest_framework import serializers # type: ignore
from .models import Task, User

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specifies the User model being serialized
        fields = '__all__'  # Serializes all fields of the User model

# Serializer for the Task model
class TaskSerializer(serializers.ModelSerializer):
    # Adding assigned_users field explicitly to handle many-to-many relationships
    assigned_users = serializers.PrimaryKeyRelatedField(
        many=True,  # Indicates that this is a many-to-many field
        queryset=User.objects.all(),  # Allows selection of existing users
        required=False  # Makes this field optional during task creation
    )

    class Meta:
        model = Task  # Specifies the Task model being serialized
        fields = '__all__'  # Serializes all fields of the Task model
