from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.


class NotificationView(APIView):
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()
            send_mail(
                notification.subject,
                notification.message,
                "your_email@gmail.com",
                [notification.email],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
