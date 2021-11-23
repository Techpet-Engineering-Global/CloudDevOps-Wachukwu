from getpass import getuser as me
import sys

print("""\nHello, {}!\nI'm glad you decided to run my code on the Fibonacci sequence\n""".format(me()))


try:
    number = input("Enter the number of sequence you want to generate: ")
    n = int(number)
    if n < 1:
        number = input("Please enter a value greater than or equal to one: ")
        n = int(number)
except ValueError:
    number = input("Please enter an integer value: ")
    n = int(number)

print("\n{0},your requested Fibonacci sequence with {1} terms is:".format(me(), n))

fib = [];


def fibonacci(fib_number):
    a = 0
    b = 1

    if fib_number == 1:
        # print(a)
        fib.append(a)
    elif fib_number >= 2:
        # print(a)
        # print(b)
        fib.append(a)
        fib.append(b)

        for value in range(2, fib_number, 1):
            c = a + b
            a = b
            b = c
            fib.append(c)
            # print(c)


fibonacci(n)
print(fib)

print("\n{},we have three operations that might be of interest to you. If you wish to engage in any of them,"
      "\nPlease input the integer value according to what you wish to perform or reply \"no\" if you're not interested"
      "\n1 Obtain the value of the nth term in the sequence"
      "\n2 Series of the sequence"
      "\n3 The value prior to a selected value".format(me()))


def jara():
    try:
        request = input("\nPlease enter your response: ")      if request == "no":
            print("\nThank you {}. \nRemain Blessed!".format(me()))
            sys.exit()
        required = int(request)

    except ValueError:
        request = input("Please enter an integer value: ")
        required = int(request)

    if required == 1:
        nth = int(input("Enter your the nth term:"))
        return_request1 = fib[nth - 1]
        print("The required term value is {}".format(return_request1))
        print("\nThank you {}. \nRemain Blessed!".format(me()))
    elif required == 2:
        return_request2 = sum(fib)
        print("The series of your sequence is {}".format(return_request2))
        print("\nThank you {}. \nRemain Blessed!".format(me()))
    elif required == 3:
        prior = int(input("Enter your the aftermath value:"))

        checker = 0
        for value in range(len(fib)):
            if fib[value] >= prior:
                checker = value
                break

        return_request3 = fib[checker - 1]
        print("The prior value to the selected is {}".format(return_request3))
        print("\nThank you {}. \nRemain Blessed!".format(me()))

    else:
        print("The value you entered is not valid, please retry")

