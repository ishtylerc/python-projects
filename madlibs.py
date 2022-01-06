# #String concatenation (akak how to put strings together)
# #"subscribe to ____"

# youtuber = "Ishtyler E." #makaing a variable for the madlib

# #Creating a few ways to do this...
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input("Adjective:")
verb1 = input("Verb:")
verb2 = input("Verb:")
famous_person = input("Famous person:")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay Hydrated and {verb2} like you are {famous_person}!"

print(madlib)