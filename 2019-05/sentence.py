# Andrzej Kocielski, 15-05-2019
# What character appears most in the sentence
# Adapted from: https://codewithmosh.com/courses/417695/lectures/6781694
# =====

sentence = "This is a common interview task."
# letters = [sentence]

char_frequency = {}  # empty dictionary

for char in sentence:  # iterates each char through the sentence
    if char not in char_frequency:
        # if the current char appears for the first time
        char_frequency[char] = 1
    else:
        char_frequency[char] += 1  # if the current char has appeared before

print(char_frequency)
