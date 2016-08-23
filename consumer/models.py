from django.db import models

class Reaction(models.Model):
    ini = models.TextField()
    ans = models.TextField()