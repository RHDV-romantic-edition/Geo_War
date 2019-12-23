from django.db import models

# Create your models here.
class Coordinates(models.Model):
    word_1 = models.CharField(max_length=20, help_text='word one')
    word_2 = models.CharField(max_length=20, help_text='word two')
    word_3 = models.CharField(max_length=20, help_text='word three')
    comands = models.CharField(max_length=20, help_text='comands')
