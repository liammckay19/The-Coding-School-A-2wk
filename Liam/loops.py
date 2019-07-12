i = 0
while i <= 10:
    print(i)
    i += 1

numbers = [1, 19, 20, 30, 40, 50]
sum = 0
for number in numbers:
    sum += number
print(sum)

print("")

for i in range(4):  # doesn't include 4, always starts at 0
    print(i)
 
print("\n")  # print new line

i = 0
sum = 0
numbers = [10, 50, 20, 30, 40, 50]
while not i == 5 or sum < 100:
    sum += numbers[i]
    i += 1

print(sum)