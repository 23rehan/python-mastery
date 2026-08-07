# Today i make program of my past topics for revision purpose 

# Topics: input(), type conversion, arithmetic operators.

first_num = int(input("Enter the any number:"))

second_num = int(input("Enter the any number again:"))

print("The sum of these numbers is:",first_num + second_num)

print("The difference of these number is:",first_num - second_num)

print("The Maltiple of these numbers is:",first_num * second_num)

print("The division of these numbers is:",first_num / second_num) 

-----

# Topics: if-else

user_age = int(input("Enter your age:"))
if user_age>=18:
    print("you can vote!")
else:
    print("you can't vote!")

------

# Topics: if, elif, logical operators.


user_marks = int(input("Enter your marks:"))
if user_marks < 0 or user_marks > 100:
    print("invalid marks!try again")
elif user_marks >= 40:
    print("you'r pass!")
else:
    print(" you'r fail!")




