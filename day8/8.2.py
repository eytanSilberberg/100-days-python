
# Write your code below this line 👇
import math


def prime_checker(number):
    if number == 1 or number == 2 or number == 3:
        print("It's a prime number.")
        return

    squr = math.ceil(math.sqrt(number))
    for i in range(2, squr):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    return


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
