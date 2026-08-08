# Atm balance 


user_balacne = int(input("Enter your balance: "))
if user_balacne>=1000:
    print("Transection Allowed")
else:
    print("Insufficent Balance")


#######

# atm checker small program
card_num = int(input("Enter your card number"))
if card_num == "1234":
    print("")
user_pin = int(input("Enter your pin"))
if user_pin== "4321":
    print("Login Successful")
else:
    print("Invalid Card")

#now students result program:
# This program check which student is pass or which student fail.

user_marks = int(input("Enter your marks: "))
if user_marks <= 0 or user_marks > 100:
    print("This is invalid marks")
elif   user_marks >= 40:
    print("pass")
else:
    print("Fail")
-------
# Today challenge!
#topic:type convertion.

user_name = input("Enter your name:")
user_age = int(input("Enter your current age:"))
dream_job = input("Enter your dream job:")

print("Hello", user_name)
print("your dream is to become an:", dream_job)
print("you are currently:", user_age)
print("After 10 years,you will be", user_age+10)
print("Keep learning and never stop coding!")

------
topic:if elif else
# now i write the program in which  i take the passward from user.

user_password = input("Enter the password")
if user_password == "python123":
    print("login Successful")
else:
    print("Wrong password")

-------
topic:function
# it's simple function program

user_name = input("Enter your name:")
user_age = int(input("Enter your age:"))
def introduction(user_name,user_age):
    print("your name is:",user_name)
    print("your age is:",user_age)
introduction(user_name,user_age)

-------



