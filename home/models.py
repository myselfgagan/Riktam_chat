from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_in = models.ForeignKey('auth.Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.text