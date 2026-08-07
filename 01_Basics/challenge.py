# Today i make program of my past topics for revision purpose 

# NAME: SMALL Calculator

# Topics: input(), type conversion, arithmetic operators.

first_num = int(input("Enter the any number:"))

second_num = int(input("Enter the any number again:"))

print("The sum of these numbers is:",first_num + second_num)

print("The difference of these number is:",first_num - second_num)

print("The Maltiple of these numbers is:",first_num * second_num)

print("The division of these numbers is:",first_num / second_num) 

-----
# NAME:SMALL Voting SYSTEM

# Topics: if-else

user_age = int(input("Enter your age:"))
if user_age>=18:
    print("you can vote!")
else:
    print("you can't vote!")

------
# NAME: PASS & FAIL 

# Topics: if, elif, logical operators.


user_marks = int(input("Enter your marks:"))
if user_marks < 0 or user_marks > 100:
    print("invalid marks!try again")
elif user_marks >= 40:
    print("you'r pass!")
else:
    print(" you'r fail!")

------
# NAME: While Loop

# topic; while loop

num = 1
while num <= 20:
    print(num)
    num = num + 1

------
# NAME: SMALL ATM

# topic:nasted if
user_card = int(input("Enter your card number"))

if user_card == 1234:
    user_pin = int(input("Enter your pin!"))

    if user_pin == 4321:
        print("login successfully")
    else:
        print("Wrong PIN")
else:
    print("Wrong Card number")

-----




