from django.urls import path
from .views import NotificationView

urlpatterns = [
    path("send-notification/", NotificationView.as_view(), name="send-notification"),
]
