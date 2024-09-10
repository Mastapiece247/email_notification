from django.db import models

# Create your models here.


class Notification(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=260)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.email} - {self.subject}"
