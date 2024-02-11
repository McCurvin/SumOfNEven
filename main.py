#SumOfNEven by Royeras Mc Curvin

def evenSum(number):
    curr = 2
    _sum = 0
    i = 1
    while i <= number:
        _sum += curr
        #next even numbers
        curr += 2
        i = i + 1
    return _sum
#ask user their input
while True:
    try:
        number = int(input("Enter the first N integers you want to compute (1 - 100) \t: "))
        if 1 <= number <= 100:
            break
        elif number == 0:
            print("Invalid input")
        elif number > 100:
            print("Out of range!")
        else:
            print("Number must be between 1 to 100.")
    except ValueError:
        print("Invalid input")

print("Sum of the first", number, "even numbers is:", evenSum(number))