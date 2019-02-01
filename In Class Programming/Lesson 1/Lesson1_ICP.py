# 1:

# Differences between Python 2 and Python 3 include:
# - In python 2, print is a statement, where in python 3, it is a function
# - In python 2, integer division returned an integer. In python 3 it returns a float.
# - In python 2, strings default to ASCII, where in python 3 they default to Unicode.


# 2:

num_1 = int(input("Please enter a 3 digit number: "))
reversed_num_1 = num_1 // 100 + (num_1 // 10 % 10) * 10 + num_1 % 10 * 100
print("Your number reversed is ", reversed_num_1)

num_2 = int(input("Please enter a random number: "))
num_3 = int(input("Please enter another random number: "))

print(num_2, " + ", num_3, " = ", num_2 + num_3)
print(num_2, " - ", num_3, " = ", num_2 - num_3)
print(num_2, " * ", num_3, " = ", num_2 * num_3)
print(num_2, " / ", num_3, " = ", num_2 / num_3)
print(num_2, " // ", num_3, " = ", num_2 // num_3)
print(num_2, " % ", num_3, " = ", num_2 % num_3)


# 3:

sentence = input("Please enter a sentence: ")
words = 1
letters = 0
digits = 0
previous = " "

for c in sentence:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c == ' ':
        if previous != " ":
            words += 1
    previous = c

print("In your sentence there are:")
print(" -", words, " words.")
print(" -", letters, "letters.")
print(" -", digits, "digits.")