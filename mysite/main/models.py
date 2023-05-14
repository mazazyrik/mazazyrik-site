from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
