# klaverjas/admin.py

from django.contrib import admin

from .models import Match, Game, GamePlayer, GameStatus, Leg

admin.site.register(Match)
admin.site.register(Game)
admin.site.register(GamePlayer)
admin.site.register(GameStatus)
admin.site.register(Leg)

