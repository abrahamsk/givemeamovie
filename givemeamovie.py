import random, sys, argparse

movies = {'The Room':'Things spiral out of control in a banker\'s life.\nYou\'re Tearing Me Apart, Lisa!!!',
         'Machete':'Danny Trejo kicks ass.',
         'Be Cool':'Mobster-turned-movie/music producer has run ins with the Russian mob. Hijinks ensure.',
         'Iron Sky':'Moon nazis.', 
         'Mad Max Beyond Thunderdome':'Mad Max\'s adventure continues with gladiator fights and Tina Turner.\nWHO RUN BARTERTOWN?!',
         'Battlefield Earth':'Based on a book by L Ron Hubbard (yes, that L Ron Hubbard).\nDescribed by its star, Travolta, as "The Schindler\'s List of science fiction."\nIt\'s a clusterfuck.',
         'Troll 2':'Vegetarian globlins (no trolls), grandpa\'s ghost, and an ill-fated family trip.', 
         'Masters of the Universe':'Skeletor find the Cosmic Key. He-Man must save the day again!',
         'The Witches':'Boy turns mouse and fights witchez!',
         'Gymkata':'Main character Cabot must combine his gymnastics skills of the west with fighting secrets of the east and form GYMKATA!'
         }

peanut_gallery = ['Excellent choice.', 'Oh dear.', 'Grab a drink or three.', 
                'Very good, sir.', 'You\'re in for a treat.']

# command line args, because why not
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", help="list all movies",
                    action="store_true")
args = parser.parse_args()
if args.all:
    print "----------"
    for k,v in movies.iteritems():
        print k
    print "----------"

# tell me what to watch
choice = (random.choice(movies.keys()))
result = "You're watching... "+choice+"!\n"
synopsis = "Here's the \"plot\": "+movies.get(choice)
commentary = "\n"+(random.choice(peanut_gallery))+"\n"
sys.stdout.write(result+synopsis+commentary)









