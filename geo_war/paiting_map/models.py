from django.db import models
import uuid
# Create your models here.
class Comand(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for comand")
    name = models.CharField(max_length=100, help_text="TeamName")
    black_squard = models.ManyToManyField('Squard', blank=True, help_text="The list of Squards that belongs to this project")
    password = models.IntegerField(default=1111)

    def __str__(self):
        return self.name


class Delta(models.Model):
    coords = models.CharField(max_length=100, help_text="Coords")
    color =  models.CharField(max_length=100, help_text="color")


    def __str__(self):
        return '{0}:{1}'.format(self.coords, self.color)

class Squard(models.Model):
    coord = models.CharField(max_length=100, help_text="Word 1")
    color = models.CharField(max_length=100, help_text="Color")

    def __str__(self):
        return '{0}:{1}'.format(self.coord, self.color)
