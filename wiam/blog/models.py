from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
