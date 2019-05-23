# Spoj.com problem #1 - Life, the Universe, and Everything
# https://www.spoj.com/problems/TEST/
# Andkoc001, 23-05-2019

print("Give me an integer number between 1 and 99.")
number = int(input())
if number in range(100):
    while number != 42:
        print("You have entered:", number, ". Keep going.")
        number = int(input())
    else:
        print("Bingo! This is the answer!")
else:
    print("Please give me a number in range 1-99")
