from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateUpdateDeleteView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get("status")

        print("QUERY STATUS =", status)

        if status == "active/":
            return Task.objects.filter(status=False)

        elif status == "completed/":
            return Task.objects.filter(status=True)

        return Task.objects.all()