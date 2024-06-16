
# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024


year = int(input("Enter a Year"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a Leap Year")
        else:
            print("It is not a Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("It is not a Leap Year")

