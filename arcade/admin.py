from arcade.models import Game
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(Game, GameAdmin)