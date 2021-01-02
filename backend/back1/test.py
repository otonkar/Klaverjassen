##### Test dabase queries

from klaverjas.models import Match, Game, GamePlayer, Leg, Slag
from my_auth.models import User

matches = Match.objects.all()
users = User.objects.all()


## Test

player = GamePlayer.objects.get(gameID=14, player=3)


## Count the number of times a user has been 'nat'
legs = Leg.objects.filter(succeeded=False)
gp = GamePlayer.objects.select_related('player').all()

l = list()
for leg in legs:
  result = gp.get(gameID=leg.gameID,position=leg.player_aangenomen)
  print(leg.gameID.gameID, leg.leg, leg.legID, result.player.username)
  l.append(result.player.username)

### Count per name
from collections import Counter
result = Counter(l)

## sort the count result bij value
result1 = sorted(result.items(), key=lambda x: -x[1])    
print(result1)

for item in result1:
  print(item[0], item[1])


## Get overview of all matches and games for a player.
gp = GamePlayer.objects.select_related('gameID__matchID').filter(player__username='ole')
for item in gp:
  print(item.position, item.player.username, item.gameID.matchID.matchID, item.gameID.gameID, item.gameID.gameStatus.gameStatus )

# Filter op uitgespeeld
gp = GamePlayer.objects.select_related('gameID__matchID').filter(player__username='ole').filter(gameID__gameStatus__gameStatus='uitgespeeld')
for item in gp:
  print(item.player.username, item.gameID.matchID.matchID, item.gameID.gameID, item.gameID.gameStatus.gameStatus )