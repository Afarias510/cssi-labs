print("Welcome to Elpollotonios calculator")
def count_spaces(s):
    return s.count(" ")
    def count_vowels(s):
        numA = s.count("a")
        numE = s.count("e")
        numI = s.count("i")
        numO = s.count("o")
        numU = s.count("u")
        sumVowels = numA + numE + numI + numO + numU
    return sumVowels

    def count_total(s):
        return count_spaces(s) + count_vowels(s)

print(count_vowels("Hello there, you are breathtaking"))

countNum = count_vowels("Hello there, you are breathtaking")
print(countNum)
