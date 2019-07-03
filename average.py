# Andrzej Kocielski, 2019-06-26
# Calculates average of numbers

how_many = 0
user_input = 0
sum = 0
average = 0

print("How many number: ")
numbers = int(input())

for number in range(numbers):
    print("Enter ", number+1, " number:")
    user_input = float(input())
    sum = sum + user_input

average = sum/numbers
print("Sum is ", sum)
print("Average is ", average)
