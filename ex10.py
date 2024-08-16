# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0

numbers = ""
for i in range(5):
    n = input("Enter:")
    numbers+=str(n)
    max = numbers
    min = numbers
    for i in range(len(numbers)):
        if numbers[i]>max:
            max = numbers[i]
        elif numbers[i]<min:
            min = numbers[i]
print("max:",max)
print("min:",min)