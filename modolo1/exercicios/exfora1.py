#Create a Python program that identifies all numbers between 100 and 300 (inclusive)
# that are divisible by 7 but not multiples of 5. 
# The identified numbers should be displayed in a single line, separated by commas.

result = []

for number in range(100, 301):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

print(', '.join(result))        