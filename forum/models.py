from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200, null=False)
    details = models.TextField(null=False)
    have_tried = models.TextField()
    created_date = models.DateTimeField("Created on")
