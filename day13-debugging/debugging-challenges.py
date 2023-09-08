
# EX1
number = int(input("Which number do you want to check?"))
# prev code was number % 2 = 0
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# EX2
# prev code was input("Which year do you want to check?")
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# EX3
for number in range(1, 101):
    #   prev code was if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        # prev code was if number % 3 == 0:
    elif number % 3 == 0:
        print("Fizz")
        # prev code was if number % 5 == 0:
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
