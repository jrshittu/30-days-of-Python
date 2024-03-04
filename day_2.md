# Day 2: Lists and Dictionaries

Mastering lists and dictionaries in Python involves understanding their functionalities, properties, and common operations. Here's a comprehensive breakdown to get you started:

## Lists:

* **Definition:** An ordered collection of items enclosed in square brackets `[]`. Elements can be of any data type, including other lists and dictionaries.
* **Creation:**
```python
my_list = [1, "hello", 3.14, [True, False]]
```
* **Accessing elements:** Use zero-based indexing starting from `[0]`. Negative indices access from the end (`[-1]` is the last element).
```python
first_element = my_list[0]  # first_element will be 1
last_element = my_list[-1]  # last_element will be [True, False]
```
* **Slicing:** Extract a sublist using colon (`:`) notation. `[start:end:step]`:
  * `start` (inclusive): index of the first element to include (defaults to 0).
  * `end` (exclusive): index of the element after the last element to include (defaults to the end of the list).
  * `step`: the difference between consecutive elements to include (defaults to 1).
```python
sublist = my_list[1:3]  # sublist will be ["hello", 3.14]
```

* **Common operations:**
  * `append(element)`: Add an element to the end of the list.
  * `insert(index, element)`: Insert an element at a specific index.
  * `remove(element)`: Remove the first occurrence of an element.
  * `pop(index)`: Remove and return the element at a specific index (or the last element by default).
  * `len(list)`: Get the length of the list (number of elements).
  * `sort()`: Sort the list in ascending order (modifies the original list).
  * `reversed()`: Return a reversed iterator for the list (doesn't modify the original list).

**Exercises:**

1. Print out a list of items in reversed form
2. Find the sum of the items.
3. Find the largest of the items in a list.
4. Find the length of the list.
5. Remove the odd number from the list.

**Solutions**
1. Print out a list of items in reversed form

```python
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]

print("Original list:", original_list)
print("Reversed list:", reversed_list)
```
**Output**
```bash
Original list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
```
2. Find the sum of the items.
```python
original_list = [1, 2, 3, 4, 5]
total = sum(original_list)
print(total)
```

**Output**

`15`

3. Find the largest of the items in a list.
```python
original_list = [1, 2, 3, 4, 5]
largest = max(original_list)
print(largest)
```
**Output**

`5`

4. Find the length of the list.
```python
original_list = [1, 2, 3, 4, 5]
length = len(original_list)
print(length)
```
**Output**

`5`

5. Remove odd numbers from the list
```python
original_list = [1, 2, 3, 4, 5]

even_number = [num for num in original_list if num%2 == 0]
print(even_number)
```

**Output**

`[2, 4]`

### Dictionaries:

* **Definition:** An unordered collection of key-value pairs enclosed in curly braces `{}`. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be any data type.
* **Creation:**
```python
my_dict = {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]}
```
* **Accessing elements:** Use the key enclosed in square brackets `[]` to access the corresponding value.
```python
name = my_dict["name"]  # name will be "Alice"
```
* **Common operations:**
  * `get(key, default)`: Get the value for a key, returning `default` if the key is not found.
  * `keys()`: Return a view of all keys in the dictionary.
  * `values()`: Return a view of all values in the dictionary.
  * `items()`: Return a view of all key-value pairs as tuples.
  * `in`: Check if a key exists in the dictionary.
  * `update(dict2)`: Update the dictionary with key-value pairs from another dictionary (`dict2`).
  * `pop(key, default)`: Remove the key-value pair and return the value, or `default` if the key is not found.

  **Exercises:**
  1. Print all names, email addresses and the key-value pairs in a dict.
  2. Check if a user exist in a dict.
  3. Update the info in the dict.
 
  **Solutions:**
  1. Print all names, email addresses and the key-value pairs in a dict.
 ![carbon](https://github.com/jrshittu/30-days-of-Python/assets/110542235/d8be477d-706e-42b8-afd4-349bf23423a8)
  2. Check if a user exist in a dict
  ![carbon (1)](https://github.com/jrshittu/30-days-of-Python/assets/110542235/3eaa420e-fcec-4a71-b8d2-72bb922456d3)
  3. Update the info in the dict.
  ![carbon (2)](https://github.com/jrshittu/30-days-of-Python/assets/110542235/491cd354-2d37-4cfa-9e95-dde159e2ca54)


  ## Projects
* Simon Says: To create this program, define a list called simon_says that contains five different instructions for the user to follow. The program should then prompt the user to pick a number between 0 and 4, and store the user's input in a variable called index. The program should use the value of index to select an instruction from the simon_says list, and then print the instruction to the screen using the print function. The program should display a message that says "Simon says..." followed by the selected instruction.
* Sandwich Order: Create a program to calculate a sandwich order and print the total cost.
* Deck of Cards: Populate a list with a deck of cards.


  ## Solutions
  **Simon Says**
  ![simon-says](https://github.com/jrshittu/30-days-of-Python/assets/110542235/baa1620e-08a8-416c-9653-31ded13cd359)

  **Sandwich Order**
  
  ![sandwich](https://github.com/jrshittu/30-days-of-Python/assets/110542235/1184c7f1-2e53-4baf-9452-afc4cd69005b)
