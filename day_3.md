# Day 3 - Selection, Conditions and Iterations
![Default_A_young_genius_sitting_with_pc_in_his_palm_coding_with_1 (2)](https://github.com/jrshittu/30-days-of-Python/assets/110542235/660ad787-da02-494a-b432-a260818fed36)

## Selection 🌵
Selection statements, such as the `if` statement, allow you to execute different blocks of code based on certain conditions. For example, you can use an `if` statement to check `if` a number is positive, negative, or zero, and execute different code depending on the result.

You will need an `if` or an `if`, `else:`
when there is more than one possible path for your program to follow. For example:

```python
print("What’s your name?")
user = input()
if user == "Elizabeth":
  print("Good morning Your Majesty")
else:
  print("Hello", user)
```

The condition will check if the value of user is equal to the string "Elizabeth". 

The expression user == "Elizabeth" will evaluate to either True or False.

This is the if block, i.e. the code that will be executed if the condition is True. 

This is the else block, i.e. the code that will be executed if the condition is False. 

Only one of these blocks will be executed, depending on the value of the condition. 

### Relational operators in Python (comparisons)

`==`   equal to

`!=`	not equal to

`<`		less than

`<=`	less than or equal to

`>`		greater than

`>=`		greater than or equal to

**Examples:**

`a == 1`		Does a equal 1? 

`b != c`		Are b and c different?

`d < 3`		Is d less than 3?

`d <= 3 `		Is d at most 3?

`d > 10`		Is d greater than 10?

`d >= 10`		Is d at least 10?

**Projects:**

- Lucky Number:
```python
lucky = 13
print("Guess my number:")
guess = int(input())
if guess == lucky:
  print("Amazing, you guessed it")
else:
  print("Sorry, it’s not", guess)
  print("My lucky number is", lucky)
print("Nice playing with you")
```
**Questions:**

- What will happen when you run the above program?

- How can you improve the program?
- Create a dice game.

## Conditions 🌿
Conditions are expressions that evaluate to `True` or `False`, and are used in selection statements to determine which block of code should be executed. For example, the condition `x > 0` evaluates to `True` if `x` is greater than zero, and `False` otherwise.

**Example:**
- Check if a number is positive, negative, or zero:
```python
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

In this example, the condition `x > 0` checks if `x` is greater than zero. If this condition is `True`, the code inside the `if` block is executed, and the message "x is positive" is printed. If the condition is `False`, the code inside the `elif` block is checked. In this case, the condition `x < 0` checks if `x` is less than zero. If this condition is `True`, the message "x is negative" is printed. If neither condition is `True`, the code inside the `else` block is executed, and the message "x is zero" is printed.

**Project:**

- Chatterbot

```python
name = input("What is your name?").lower() 

if name == "anakin":
  print("How do you do Anakin!")
else:
  print(f"Nice name, {name}")
print(f"So {name}, is it hot or cold where you are today?")

weather = input().upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")
print("Do you like the colour blue?")

likes_blue = input().capitalize()
if likes_blue == "Yes":
  print("I like blue too")
print("Have a good day! Bye!")
```
**Questions:**
1. What will happen when you run the code?
2. How can you improve the program?

## Iterations🔂
Iteration statements, such as the `for` and `while` loops, allow you to execute a block of code repeatedly until a certain condition is met. For example, you can use a `for` loop to iterate over a list of items and perform some operation on each item, or use a `while` loop to repeatedly ask the user for input until they enter a valid value.


**`while` Loop**

You will need a while statement:
When your program needs to repeat actions, while a condition is satisfied.

```python
# Get the user's input and store it in the variable "name"
name = input("What’s your name?")

# Use a while loop to repeatedly ask the user for their name until they enter the correct name
while name != "Hedy":
  # Print a message providing feedback to the user
  print("Try again Hedy")

  # Get the user's input again and update the value of "name"
  name = input()

# Print a personalized greeting to the user
print(f"Hello, {name}")
```

**Questions:**

1. What will happen when you run the program?
2. How can you improve the program?


**Project:**

**Parson's Puzzle:** A Parson's Puzzle is designed so that you can move the code around until it provides a logical solution to the problem given.  

Your job is to rearrange the lines of code so that the program will:

●	Ask for a word to guess

●	Check if the word is not equal to Raspberry

●	Continue to check if the word is not equal to Raspberry

●	When the word is equal to Raspberry, it should display: 
“Well done, the word was Raspberry!”

```python
print(f"Well done, the word was {word}!")
print("Try again...")
print("Guess the word")
word = input() 
word = input()
while word != "Raspberry":
```

**`for` Loop**
```python
for x in range(5):
    print(x)
```
*What will the output be when this code is executed?*

A for loop is another tool to control the flow of execution in your programs. 

A while loop can do everything that a for loop can do. 
However, it is more convenient to use a for loop for iterating through sequences. 

When you use a for loop you are saying:
“For every element in this sequence, do this.”

```python
for this sequence:
    do this
```

For loops can be used for many types of sequence, for example:
- Letters in a word

- Items in a list

- Numbers in a range

**For Example:**

```python
for x in range(5):
    print(x)
```
`range()` is the sequence that you are going to iterate through.

`range()` is a built-in function just like `input()`. 
It generates a sequence of numbers.

```python
for x in range(start, end, step):
    print(x)
```

When you call the range function, you can pass it up to three values: 
- The start number
- The end number
- The step

If you only pass one value, then the function will use it as the last number and the sequence will start at 0. 

```python
for x in range(5):
    print(x)
```

When you call the range function, it will generate a sequence of numbers:
0, 1, 2, 3, 4 

**Note:** The end number is not included in the generated sequence, because it is used as the stop point. 

x is the variable that is used to iterate through this sequence.  
0, 1, 2, 3, 4 

**Project:**
- Times table Generator
```python
times_table = 5
answer = 0
print(f"Here is the {times_table} times table")
for x in range(1,11):
    answer = x * times_table
    print(f"{x} times {times_table} is {answer}")
```
**Questions:**
1. Take a look at the code above. Read it carefully and try to make a prediction about the output of this program when it is executed.
2. In the first iteration, what is the value of x?
3. Line 4 has the code range(1,11).
4. Change the values to range(2,22).
5. What is the second line that is output for display?
6. What is the final line that is output for display?
7. Change the values passed in range so that the times table generator will output the 5 times table from 1 to 12. 
8. Introduce an input() to the program to allow the user to enter the times table that they wish to create. 


**☕ Enjoyed this article? Support my work with a coffee: [https://www.buymeacoffee.com/cqvuesleq](https://www.buymeacoffee.com/cqvuesleq)**

**Also open for technical writing and frontend dev roles!**
