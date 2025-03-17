
# Check the number is positive of negative

# number = int(input("Enter a number"))

# if number>0:
#         print("the number is positive")
# elif number<0:
#         print("the number is negative")
# else:print("number is zero")


# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

# age = float(input("Enter your age"))
# if age <13:
#     print("Your are Minor")
# elif age >=13 and age <= 40:
#     print("Your are adult")
# else:
#     print("you are Elder")

# 3. Write a program that checks if a given year is a leap year.

year = float(input("Enter A year to find either it is a leap year or not"))

if year % 4 == 0 and year %100 != 0 or year % 400==0:
    print("this is a leap year")
else:
    print("this is not a leap year")
    