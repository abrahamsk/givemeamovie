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
         'Gymkata':'Main character Cabot must combine his gymnastics skills of the west with fighting secrets of the east and form GYMKATA!',
         'Mortal Kombat: Annihilation':'The world was created in six days, so too shall it be destroyed and on the seventh day mankind will rest... in peace.'
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

# movies we've already subjected ourselves to
archive = {'A Talking Cat!?!':'"The Room" of anthropomorphic animal movies featuring Eric Roberts.  From the AV Club: A Talking Cat?!? is really an exercise in pushing the boundaries of constructive editing far beyond their breaking point.',
         'Wild Wild West':'Will Smith fights a giant spider in a cowboy hat. Also, naked ladies',
         'Punisher: War Zone':'Just watch this: https://youtu.be/YF28ceFJJ3A',
         'Piranha 3DD':'Maddy (Danielle Panabaker), a marine biology student, returns home for the summer to the waterpark she co-owns. She finds to her horror that the other co-owner, her step-father Chet, plans to add an adult-themed section to the waterpark with "water-certified strippers", and re-open it as "Big Wet".  Need I say more?',
         'Gymkata':'Main character Cabot must combine his gymnastics skills of the west with fighting secrets of the east and form GYMKATA!'
         }








