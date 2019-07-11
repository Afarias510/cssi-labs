print("Welcome to Elpollotonios Fuctions Cardio")
# This is the triangle Challenge
num1 = int(raw_input("Give me side 1 length: "))
num2 = int(raw_input("Give me side 2 length: "))
num3 = int(raw_input("Give me side 3 length: "))

def is_triangle(s1, s2, s3):
    sum1 = s1 + s2
    sum2 = s2 + s3
    sum3 = s1 + s3
    if sum1 > s3 and sum2 > s1 and sum3 > s2:
        print("You have a triangle")
        return True
    else:
        print("You do not have a triangle")
        return False

print(is_triangle(num1, num2, num3))
# This is the longest word Challenge
word1 = raw_input("Give me a word: ")
word2 = raw_input("Give me another word: ")
word3 = raw_input("Give me another word: ")

def longest_word(w1,w2,w3):
    if len(w1)> len(w2) and len(w1)> len(w3):
        print("This is your largest word")
        return w1
    elif len(w2)> len(w1) and len(w2)> len(w3):
        print("This is your largest word")
        return w2
    elif len(w3)> len(w2) and len(w3)> len(w1):
        print("This is your largest word")
        return w3
    else:
        print("They all have equal length")

print(longest_word(word1,word2,word3))
# This is the sum to number Challenge
num1 = int(raw_input("Enter a number: "))
def sum_to_n(num):
    sum = 1+ 2+ 3 + num
    return sum
print(sum_to_n(num1))



# This is the reverse string Challenge

word = str(raw_input("Give me a Word "))

def my_function(x):
  return x[::-1]

print("This is your word backwards "+my_function(word))


# This is the Dice Challenge
import random
game_start = raw_input("Would you like to roll the dice? ")

def dice_roll():
    print("Your number is: " + str(random.randint(1,6)))
    global play_again
    play_again = raw_input("Would you like to play again? ")

if game_start == "yes":
    dice_roll()
    while play_again == "yes":
        dice_roll()
elif game_start == "no":
    print("Game Over ")
else:
    print("Input not recognized ")
