from django.db import models
import uuid 
# Create your models here.
class Comand(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for comand")
    name = models.CharField(max_length=100, help_text="TeamName")
    black_squard = models.ManyToManyField('Squard', blank=True, help_text="The list of Squards that belongs to this project")
    Place = models.OneToOneField('Scoreboard', blank=True, on_delete=models.SET_NULL, null=True, help_text="The team place in Scoreboard")


    def __str__(self):
        return self.name

class Squard(models.Model):
    
    word_1 = models.CharField(max_length=100, help_text="Word 1")
    word_2 = models.CharField(max_length=100, help_text="Word 2")
    word_3 = models.CharField(max_length=100, help_text="Word 3")
    team = models.OneToOneField(Comand, on_delete=models.SET_NULL, null=True, help_text="The team which last paint this zone")
    time = models.DateTimeField(auto_now=True,null=True, blank=True)

    def __str__(self):
        return 'word 1 = {0} , word 2 = {1}, word 3 = {2}, command = {3}'.format(self.word_1, self.word_2, self.word_3, self.team.name)
        

class Scoreboard(models.Model):
    team = models.OneToOneField(Comand, on_delete=models.SET_NULL, null=True, help_text="The teams")
    score = models.IntegerField(default=0)
    def __str__(self):
        return "Score = {0} , comand - {1}".format(self.score, self.team.name)

        
