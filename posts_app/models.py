from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    attachment = models.FileField(upload_to='docs/', null=True)
    creation_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.title