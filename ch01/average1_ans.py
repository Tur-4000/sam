numbers = []
count = 0
summ = 0

while True:
    number = input("enter a number or Enter to finish: ")
    if number:
        try:
            number = int(number)
            numbers.append(number)
            summ += number
            count += 1
        except ValueError as err:
            print(err)
            continue
    else:
        break

print(numbers)

i = 1
lowest = numbers[0]
highest = numbers[0]
while i < len(numbers):
    if lowest > numbers[i]:
        lowest = numbers[i]
    if highest < numbers[i]:
        highest = numbers[i]
    i += 1

print("count = " + str(count) + 
        "; sum = " + str(summ) + 
        "; lowest = " + str(lowest) + 
        "; highest = " + str(highest) +
        "; mean = " + str(summ / count))