while Loop

Definition:

A while loop tab tak repeat hota hai jab tak uski condition True rahe.or jab false hojye gi to loop stop hojye ga.

Syntax:
while condition:
    # code
Important Rules!
Condition True honi chahiye tab loop chalega.
Condition False hote hi loop stop ho jata hai.
Loop ke andar variable ko update karna zaroori hai.

Example:

count = count + 1

Agar update nahi karoge to infinite loop ban sakta hai.
#####
## Functions

A function is a reusable block of code that performs a specific task.

### 1. Defining a Function

We use the `def` keyword to create a function.

Exp:
def welcome():
    print("Welcome to Python!")
 welcome()   

------

Parameter:

A parameter is a variable written inside the function's parentheses. It represents a value that the function expects.

def welcome(name):
    print("Hello", name)

Here, name is a parameter.

 Argument:

An argument is the actual value we give to a function when calling it.

welcome("Rehan")

Here, "Rehan" is an argument.

----- 

Parameter vs Argument
Parameter → variable in the function definition.
Argument → actual value passed when calling the function.

Example:

def welcome(name):      # name = parameter
    print("Hello", name)

welcome("Rehan")        # "Rehan" = argument


-----
