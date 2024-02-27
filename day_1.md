# Day 1 - Variables, Data Types and Operators
This tutorial is based on variables, data types and operators

## Variables
A variable holds a value in a memory location that is needed for the execution of your program.

### Using a variable
A memory location needs to be allocated for the variable value, before it can be used by the program.

**Declaring a variable** means stating what _data type_ will be used for the value. 
**Initialising a variable** means _setting the initial value_. Python doesn’t use variable declaration, only initialisation.

**Example**
```python
name = "Alex"
print(name)
```

- **Hello Python**
  Create a script to print hello 🐍.
  
  ```python
  pi = "🐍"
  print("Hello", pi)
  ```

- **Short Intro**
  Create a program to introduce someone.

  ```python
  name = "Albert Einstein"
  age = 67
  profession = "Scientist"

  print("Hello!", name, "is", age, "years old and a", profession)
  ```


## Data Types
There are five main data types namely;
- String (text) e.g "Alex", "Sofia"
- Integer (whole numbers) e.g. 3, 4, 5
- Boolean (True or False) e.g. True, False
- Real or floating point numbers (decimal numbers) e.g. 4.5, 7.54
- Char (single string characters) e.g. "a", "z", "b"

**N.B:** Incorrect data types can cause problems during the execution of your programs.

**Question**

Predict what might happen when this code is executed.

```python
print("Enter a number")
num1 = input()
print("Enter another number")
num2 = input()
print(num1+num2)
```
**Output**
```bash
Enter a number
1
Enter another number
2
12
>>>
```
The data type for an input is always string. When you add two pieces of string together, it will concatenate (join) them. 
Instead of adding the two numbers together to make 3, it has joined the corresponding strings together to make 12 (one,two). 
This code has produced a logic error because it hasn’t executed as expected.

If you want Python to use your value as an integer, then you need to tell it that by **casting the value**. 
You do this by placing `input()` inside the `int()` function.

```python
print("Enter a number")
num1 = int(input())
print("Enter another number")
num2 = int(input())
print(num1+num2)
```

```bash
Enter a number
1
Enter another number
2
3
```

Errors can still happen during execution, even when casting has been used.
 **Question**
 
What might happen if the user enters ‘four’ when this code is executed?

**Answer**

A runtime error occurs. This is a type of error that causes the program to crash during execution.

```python
print("Enter a number")
number = int(input())
print(number)
```

```bash
Enter a number
four
Traceback (most recent call last):
  File "c:\users\pi\mu_code\fsea.py", line 2, in <module>
    number = int(input())
ValueError: invalid literal for int() with base 10: 'four'
>>>
```

You can avoid this type of error by introducing validation checks. 
Here is an example check that you can use called try and except. 

```python
print("Enter a number")
try:
    number = int(input())
except ValueError:
    print("You must enter a number")
    number = int(input())
```
To convert values to different data types, you need to know the functions that are available to you. 
Here are the most common functions that you will need to know.

```python
# convert to string
str() 
# convert to integer
int()
# convert to real
float()
```

## Using Operators in Python
Here are the list of operators in python;
- (+)	Addition
```python
5 + 5
```
`>>> 10`
  
- (-) 	Subtraction
```python
10 - 5
```
`>>> 5`
  
- (*)	Multiplication
```python
5 * 5
```
`>>> 25`
  
- / 	Real division
```python
5 / 2
```
`>>> 2.5`
  
- //	Integer division (quotient) is the operation that calculates how many whole times the divisor (3) will fit in the dividend (14).
```python
26 // 5
```
`>>> 5`
  
- **	Powers
 ```python
5 ** 2
```
`>>> 25`

- %	Modulo (MOD) is used to work out the remainder of the division.
```python
15 % 7
```
`>>> 1`

## Randomisation
**Importing the `random` Module:**

Before using randomization, you need to import the built-in `random` module:

```python
import random
```

**Generating Random Numbers:**

* **`random.random()`:** Generates a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).

```python
random_float = random.random()
print(random_float)
```

* **`random.randint(a, b)`:** Generates a random integer between `a` (inclusive) and `b` (inclusive).

```python
random_int = random.randint(1, 6)  # Simulates rolling a die
print(random_int)  # Output: Varies between 1 and 6 (inclusive)
```

**Choosing Random Elements from Sequences:**

* **`random.choice(sequence)`:** Returns a random element from the given sequence (list, tuple, string).

```python
fruits = ["apple", "banana", "orange"]
random_fruit = random.choice(fruits)
print(random_fruit)  # Output: Varies among "apple", "banana", and "orange"
```

**Shuffling Lists:**

* **`random.shuffle(list)`:** Modifies the original list by shuffling its elements randomly in place.

```python
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)
print(colors)  # Output: Order of colors varies on each run
```

**Generating Random Samples from Sequences:**

* **`random.sample(sequence, k)`:** Returns a list of `k` unique elements chosen from the sequence without replacement.

```python
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random_sample = random.sample(letters, 5)  # Choose 5 unique letters
print(random_sample)  # Output: Varies with 5 distinct letters
```

**Example Projects:**

1. **Simple Coin Game:**
   - Create a variable to get computer_choice `random.choice(coin)`.
   - Allow the user to guess whether H or T and compare it to the result.
   - Print messages based on whether the guess is correct or not.
  
```python
from random import choice

coin = ["Head", "Tail"]
player_choice = input("Enter your choice (Head/Tail): ").capitalize()

if player_choice == choice(coin):
    print("You guessed it right!")
else:
    print("Sorry, you lost!")
    print("The coin landed on", choice(coin))
```
    
2. **Simple Dice Rolling Game:**
   - Create a variable to get computer_choice `random.randint(1, 6)`.
   - Allow the user to guess a sum and compare it to the actual roll.
   - Print messages based on whether the guess is correct or not.

```python
from random import randint

computer_choice = randint(1, 6)

player_guess = int(input("Enter your choice 1-6: "))

if computer_choice == player_guess:
    print("You guessed it right!")
else:
 print("Sorry, computer choice was", computer_choice)
```
__Exercise__:Improve the program by adding error handling