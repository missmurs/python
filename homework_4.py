'''
Write a program that caluculate Fibonacci series. The Fibonacci series is a series of numbers in which each number is
the sum of the two preceding numbers.The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number
 is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
'''
n = int(input())


a, b = 1, 1

print(a)
print(b)

for i in range(n - 2):
    c = a + b
    print(c)
    a, b = b, c
'''
Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3
'''
for num in range(101):
    if num % 3 == 0:
        print(num)
'''
Get a number from user input and iterate from 0 to that number.

Print 'foo' if the number is divisible by 3.
Print 'bar' if the number is divisible by 5.
Print 'foobar' if the number is divisible by both 3 and 5.
'''

n = int(input(""))

for i in range(n+1):

    if i % 3 == 0 and i % 5 == 0:
        print("foobar")
    elif i % 3 == 0:
        print("foo")
    elif i % 5 == 0:
        print("bar")
    else:
        print(i)
'''
Write a function called square() with one argument of int type and returns the value of that number raised to the second power.
'''
def square(num: int) -> int:
    return num**2
'''
Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature
in Fahrenheit. It should take a number as an argument from user input and return a number to the console.
'''
def convert_cel_to_fahr(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Цельсія: "))

fahrenheit = convert_cel_to_fahr(celsius)

print("Фаренгейта:",fahrenheit)
'''
Write a function that implement case swapping. It should return the same result as swapcase() method. Your function 
should accept one str argument and convert all lower case values to upper case and vice versa.
'''
def case_swap(s):
    swapped = ""
    for char in s:
        if char.isupper():
            swapped += char.lower()
        else:
            swapped += char.upper()
    return swapped

