from django.db import models

class Instruction(models.Model):
    id = models.CharField(max_length=200)