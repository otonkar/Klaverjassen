# Fill the GameStatus table with the values

from klaverjas.models import GameStatus

items = [
    'niet gestart',
    'wordt gespeeld',
    'uitgespeeld',
    'afgebroken',
]

for item in items:
    GameStatus.objects.create(gameStatus = item )