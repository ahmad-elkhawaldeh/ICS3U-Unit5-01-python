# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program calculates the temperature in fahrenheit


def fahrenheit():

    # input
    celsius_string = input("Enter temperature in celsius: ")

    try:
        celsius = float(celsius_string)
        fahrenheit = (celsius * 9/5) + 32

        # output
        print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
    except Exception:
        print("This is not a number")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
