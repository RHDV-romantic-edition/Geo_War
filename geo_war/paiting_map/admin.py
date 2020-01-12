from django.contrib import admin
from .models import Comand, Scoreboard, Squard



@admin.register(Comand)
class ComandAdmin(admin.ModelAdmin):
    pass
@admin.register(Scoreboard)
class ScoreboardAdmin(admin.ModelAdmin):
    list_filter = ('score', 'team')

@admin.register(Squard)
class SquardAdmin(admin.ModelAdmin):
    list_display = ('word_1','word_2' ,'word_3')
    #fields = [('word_1','word_2','word_3'),'team', 'time']
