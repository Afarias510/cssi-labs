print ("Welcome to Elpollotonios Pluralizer")
num1 = int(raw_input("please enter a number: "))
word1 = raw_input("Please enter a word: ")
if num1 ==  0 or num1 > 1 or num1 < 1:
    print(str(num1)+" " + word1 +"s")
else:
    print(str(num1)+" "+ word1)
