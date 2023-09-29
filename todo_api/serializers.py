from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # timestamp = serializers.DateTimeField(
    #     format="%Y-%m-%dT%H:%M:%S.%fZ"
    # )  # Customize the datetime format
    # updated = serializers.DateTimeField(
    #     format="%Y-%m-%dT%H:%M:%S.%fZ"
    # )  # Customize the datetime format

    class Meta:
        model = Todo
        fields = ["task", "completed", "user"]
