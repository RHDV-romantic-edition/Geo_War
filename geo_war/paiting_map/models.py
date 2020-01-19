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

class Squard(models.Model):
    word_1 = models.CharField(max_length=100, help_text="Word 1")
    word_2 = models.CharField(max_length=100, help_text="Word 2")
    word_3 = models.CharField(max_length=100, help_text="Word 3")
    color = models.CharField(max_length=100, help_text="Color")
    time = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return '{0}.{1}.{2}:{3}'.format(self.word_1, self.word_2, self.word_3, self.color)