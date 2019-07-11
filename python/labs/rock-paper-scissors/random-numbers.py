import random

print("Welcome to ElPolloTonios Random Playground")

# print (random.randint(1,5))

die1 = random.randint(1,6)
die2 = random.randint(1,6)

sum = die1 + die2
if die1 == die2:
    print("Doubles!!")
    print("You move %s steps " % sum)
    print("You roll again")
else:
    print("You move %s steps" % (sum))
    print("Next players turn")
