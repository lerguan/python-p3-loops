#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while 1<=num<=10:
        print(num)
        num -= 1
        if num == 0:
            print("Happy New Year!") 

def square_integers(int_list):
    # code goes here!
    square_integers = [num**2 for num in int_list]
    return square_integers

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num%3 ==0 and num%5 == 0:
            print("FizzBuzz")
        elif num%3 == 0 and num%5 != 0:
            print("Fizz")
        elif num%3 != 0 and num%5 == 0:
            print("Buzz")
        else:
            print(num)
