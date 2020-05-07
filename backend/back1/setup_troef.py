# Fill the Troef table with the values

from klaverjas.models import Troef

items = [
    'clubs',
    'hearts',
    'spades',
    'diamonds',
]

for item in items:
    Troef.objects.create(troef = item )
