from django.contrib import admin
from .models import Comand, Squard, Delta



@admin.register(Comand)
class ComandAdmin(admin.ModelAdmin):
    pass

@admin.register(Squard)
class SquardAdmin(admin.ModelAdmin):
    pass


@admin.register(Delta)
class DeltaAdmin(admin.ModelAdmin):
    pass
