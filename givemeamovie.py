import random, sys
movies = ['Wild Wild West', 'The Room', 'Machete', 'Be Cool', 'Iron Sky', 'Mad Max Beyond Thunderdome']
text = "You're watching... "+(random.choice(movies))+"!\n"
sys.stdout.write(text)