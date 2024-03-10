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
- **Questions:**
1. What will happen when you run the code?
2. How can you improve the program?

## Iterations🔂
Iteration statements, such as the `for` and `while` loops, allow you to execute a block of code repeatedly until a certain condition is met. For example, you can use a `for` loop to iterate over a list of items and perform some operation on each item, or use a `while` loop to repeatedly ask the user for input until they enter a valid value.

**`for` Loop**






**☕ Enjoyed this article? Support my work with a coffee: [https://www.buymeacoffee.com/cqvuesleq](https://www.buymeacoffee.com/cqvuesleq)**

**Also open for technical writing and frontend dev roles!**
