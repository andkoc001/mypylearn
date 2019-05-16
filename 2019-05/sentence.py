# Andrzej Kocielski, 15-05-2019
# What character appears most in the sentence
# =====

sentence = "This is a common interview question."
# letters = [sentence]

# Salution taken and adapted from: https://codewithmosh.com/courses/417695/lectures/6781694
char_frequency = {}  # empty Dictionary

for char in sentence:  # iterates each char through the sentence
    if char not in char_frequency:
        # if the current char appears for the first time
        char_frequency[char] = 1
    else:
        char_frequency[char] += 1  # if the current char has appeared before

# print(char_frequency) # commented out, because of ugly formatting

# sorting the result and formatting
# because Dictionary is unsortable, we will convert it do Tuple
# with the lambda function we will takes each item from the Dictionary and convert it to Tuple
# sorted iterates through all items
char_frequency_sorted = sorted(char_frequency.items(),
                               # key parameter generates a new list; lambda takes key value (kv) of each item and assigns its value
                               key=lambda kv: kv[1],
                               reverse=True)

print(char_frequency_sorted[0])
