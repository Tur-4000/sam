numbers = []
summ = 0
lowest = None
highest = None

while True:
    try:
        number = input("enter a number or Enter to finish: ")
        if not number:
            break
        number = int(number)
        numbers.append(number)
        summ += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("numbers: ", numbers)

print("count =", len(numbers), "; sum =", str(summ), 
        "; lowest =", str(lowest), "; highest =", str(highest),
        "; mean =", summ / len(numbers))