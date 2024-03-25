# Day 5 - Subroutines and Scopes

**Table of Contents**

[1. Introduction](#intro)

[2. Subroutines](#sub)

- 2.1. Parameters
- 2.2. Arguments

[3. Control Flow](#contr)

[4. Procedures and Functions](#pro)

[5. Scope](#scope)

- 5.1. Global Scope
- 5.2. Local Scope

[6. Constants](#const)

[Conclusions](#conc)

## Introduction <a name="intro"></a>
```python
def calculate(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

num1 = 10
num2 = 15

calculate(num1, num2)
```
- Explain exactly what you think will happen when this code is executed.

- Run the code and check if you are right.


## Subroutines <a name="sub"></a>
A subroutine is a sequence of instructions to perform a specific task with an **identifiable** name.

```python
def calculate(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")
```

**Subroutines** can be called upon whenever they are required. 

**def** just defines the subroutine. It is not executed unless the subroutine is called. 

**Parameters** are values passed into the subroutine. In the `calculate` function above, the parameters are `a` and `b`. 

A subroutine call has **arguments**. The values held in the **arguments** are passed to the **parameters**.  

```python
def calculate(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

num1 = 10
num2 = 5

calculate(num1, num2) # 10 + 5 = 15
```
What exactly do you think are the **arguments** passed to the **parameters**? 

## Control Flow <a name="contr"></a>
The control flow differs when a subroutine call is encountered. 

Instead of running statements one after another, the program transfers control ‘out of line’ to the subroutine, and the code in the subroutine is executed.

```python
def greet(name):
  print("Hello, " + name + "!")

print("Starting program...")
greet("Alice")
print("Ending program...")
```
In this example, the `greet` function is a subroutine that takes a single argument, `name`. When the `greet` function is called, control is transferred to the code inside the function, and the message `"Hello, Alice!"` is printed to the console. Once the function has finished executing, control is transferred back to the main program, and the message `"Ending program..."` is printed.

## Procedures and functions <a name="pro"></a>
Subroutines come in two categories:
- Procedures
- Functions

A **procedure** executes a specific set of commands when it is called. It does not return a value.
```python
def calculate(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

calculate(5, 10)
```

A **function** is used to calculate or process a value based on arguments given. It always returns a value.  
```python
def calculate(a, b):
    answer = a + b
    return answer

answer = calculate(5, 10)
```
**Note:** In Python, there is no distinction between a `function` and a `procedure`. 

It is important to note that when the `return` line is executed. The function will terminate, returning the value. 

Any code after the return is executed is ignored. 

**Project: Create a Calculator**
```python
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Would you like to +, -, / or * ? ")

if operator == "+":
  result = add(num1, num2)
  print(f"The result is {result}")
elif operator == "-":
  result = subtract(num1, num2)
  print(f"The result is {result}")
elif operator == "*":
  result = multiply(num1, num2)
  print(f"The result is {result}")
elif operator == "/":
  result = divide(num1, num2)
  print(f"The result is {result}")
else:
  print("Invalid operator")
```
**Questions:**
- What exactly do you think will happen when you run the program?
- How can you improve the program?

## Scope <a name="scope"></a>
The scope of a variable is the section of the program where the variable can be accessed and modified.

Variables can either have `global scope` or `local scope`.

`Global scope` refers to a variable that can be accessed and modified from anywhere in the program, even from inside subroutines.

`Local scope` refers to variables that can only be accessed and modified within the code block that they were declared.  

Not all programming languages handle scope in the same way.

Python has been designed to discourage the modification of global variables, you’ll find out why during this lesson. Variables are local unless otherwise declared. 

A variable declared in the main part of the program can be accessed globally by all subroutines. 
It cannot be modified unless you explicitly state that the program should modify the global variable. 

```python
def example():
    print(number)

number = 5 # global variable
example()
print(number)
```
What exactly will happen when you run this program?

```python
def example():
    number = 10 
    print(number) # outputs 10

number = 5
example()
print(number) # outputs 5
```
The intention of this subroutine is to modify the global variable number. However, it doesn’t execute as expected. 

*A new variable is declared with local scope. A global variable cannot be modified unless it is explicitly stated in the program.*

Here is a subroutine that will access and modify the `global variable`.
```python
def example():
    global number
    number = 10
    print(number) # outputs 10

number = 5
example()
print(number) # outputs 10
```

Global variables are generally seen as bad practice by programmers. This is because it can be difficult to track the value of the global variable if it is modified in other areas of the program. It is also harder to test a function in isolation if it accesses global variables. 

If you are tempted to use a global variable, it is a good idea to try and think carefully whether parameter passing would be a better approach.


## Constants <a name="const"></a>
A constant is a fixed value that doesn’t change through the execution of the program. 

`Constants` can be helpful in programming when you need to ensure that a value stays the same throughout execution. One example of this might be the value of pi. 

Not all programming languages deal with constants in the same way. 

In C for example, you need to declare a constant:

`const float pi=3.14;`

If the program is instructed to `change` the value of a `declared constant`, then it will produce an `error`.

In Python it is different. Python does not have a specific feature for declaring constants. If you wish to use a constant, then you follow a naming convention. 

*All constants are declared using capital letters.*

`PI = 3.14`

The Python language will still treat this as a variable and it will not produce an error message if the value is changed during execution.

The naming convention is used to let programmers know that this variable is to be used as a constant.

### Example
A game designer wants to ensure that all new levels begin with the background moving at the same speed.
This start speed should be the same for all new levels. 

```python
INITIAL_SPEED = 5

def level_1():
    speed = INITIAL_SPEED
    print("Go faster? Y/N")
    answer = input()
    if answer == "Y":
        speed = speed + 5

level_1()
```
At the start of each new level, the speed is set by assigning the constant `SPEED` to the variable speed. 
```python
INITIAL_SPEED = 5

def level_1():
    speed = INITIAL_SPEED
    print("Go faster? Y/N")
    answer = input()
    if answer == "Y":
        speed = speed + 5

level_1()
```
As each level gets harder, the speed will increase at different rates. The speed at the beginning of each level will always be the same.

The programmer could just assign 5 to speed at the beginning of each level. This would remove the need for the constant. 
```python
def level_1():
    speed = 5
    print("Go faster? Y/N")
    answer = input()
    if answer == "Y":
        speed = speed + 5

level_1()
```

**Question:**
What would happen if the programmer decided that the start speed should be 10 instead?

They would need to go to every part of the program that referenced the start speed and change each individual value to 10. 

By having a constant, the programmer can simply change the value once and it will change the value everywhere.
```python
INITIAL_SPEED = 5

def level_1():
    speed = INITIAL_SPEED
    print("Go faster? Y/N")
    answer = input()
    if answer == "Y":
        speed = speed + 5

level_1()
```

## Conclusion <a name="conc"></a>
In this lesson, we have learned about subroutines, their parameters and arguments, and how they affect control flow. We have also explored the difference between procedures and functions, and how to create a simple calculator program using functions. Additionally, we have discussed the concept of scope, including global and local scope, and the best practices for using global variables. Finally, we have learned about constants and their importance in programming. Understanding these concepts is crucial for writing efficient and well-structured code.