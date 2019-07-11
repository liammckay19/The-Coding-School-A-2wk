i=0
while i<=10:
    print(i)
    i+=1

numbers = [10, 50, 20, 30, 40, 50]
sum = 0
for number in numbers:
    sum += number
print(sum)

print("")
for i in range(4):
    print(i)
print("\n")
i=0
sum = 0

while not i == 5 and sum <100:
    sum += numbers[i]
    i += 1

print(sum)
