# Day 5 - Strings Manipulation and Formatting
![Default_A_young_smart_genius_sitting_with_pc_on_the_desk_codin_0 (3)](https://github.com/jrshittu/30-days-of-Python/assets/110542235/b2b8bb16-6ccd-4502-bcfe-7bd48a3d3c6e)


## Introduction
Strings in Python are a sequence of characters, enclosed in either single quotes (`'...'`) or double quotes (`"..."`). They can contain letters, numbers, special characters, and spaces. Strings are immutable, meaning that once you create a string, you cannot change its content. Here's an example of a string in Python:
```python
my_string = "Hello, World!"
```
String formatting is a way to create strings by inserting variables into placeholders within the string. One of the most popular ways to format strings in Python is using f-strings, which were introduced in Python 3.6. F-strings are prefixed with the letter `f` or `F` and allow you to embed expressions inside curly braces `{}`. Here's an example:
```python
name = "Alice"
age = 25
message = f"{name} is {age} years old."
print(message)
```
In this example, the variables `name` and `age` are inserted into the string `message` using the curly braces `{}`. The resulting string is `"Alice is 25 years old."`.

F-strings offer several advantages over other string formatting methods, such as being more concise and easier to read. They also support more advanced formatting options, such as expression evaluation and string formatting specifiers. Here's an example:
```python
pi = 3.14159
radius = 5
area = pi * radius ** 2
formatted_area = f"The area of a circle with radius {radius} is {area:.2f}."
print(formatted_area)
```
In this example, the expression `pi * radius ** 2` is evaluated and inserted into the string `formatted_area`. The `:.2f` specifier is used to format the floating-point number `area` with two decimal places. The resulting string is `"The area of a circle with radius 5 is 78.54."`.

## Python String methods.
Strings in Python are objects that come with a set of built-in methods for performing common operations on them. These methods allow you to manipulate strings in various ways, such as searching for substrings, modifying case, removing whitespace, and more.

Here are some of the most commonly used string methods in Python:

* `upper()`: Converts all the characters in a string to uppercase.
* `lower()`: Converts all the characters in a string to lowercase.
* `title()`: Converts the first character of each word in a string to uppercase, and the rest of the characters to lowercase.
* `strip()`: Removes leading and trailing whitespace from a string.
* `lstrip()`: Removes leading whitespace from a string.
* `rstrip()`: Removes trailing whitespace from a string.
* `replace(old, new)`: Replaces all occurrences of the `old` substring with the `new` substring in a string.
* `split(sep)`: Splits a string into a list of substrings based on the specified separator `sep`.
* `find(sub)`: Returns the index of the first occurrence of the `sub` substring in a string, or `-1` if not found.
* `startswith(prefix)`: Returns `True` if a string starts with the specified `prefix`, and `False` otherwise.
* `endswith(suffix)`: Returns `True` if a string ends with the specified `suffix`, and `False` otherwise.

### Examples
```python
text = "   Hello, World!   "
print(text.upper()) # "   HELLO, WORLD!   "
print(text.lower()) # "   hello, world!   "
print(text.strip()) # "Hello, World!"
print(text.replace("World", "Python")) # "   Hello, Python!   "
print(text.split(" ")) # ['', '', 'Hello,', 'World!', '', '']
print(text.find("World")) # 13
print(text.startswith("Hello")) # False
print(text.endswith("World!")) # True
```
In this example, we're using various string methods to manipulate the `text` string. The `upper()` and `lower()` methods are used to change the case of the string, while the `strip()` method is used to remove leading and trailing whitespace. The `replace()` method is used to replace a substring, while the `split()` method is used to split the string into a list of substrings. The `find()`, `startswith()`, and `endswith()` methods are used to search for substrings within the string.

### Exercises
Now let's explore how to slice, dice, search, and replace text with ease using strip(), split(), join(), lower(), upper(), replace(), and find().

## Exercise One: Palindrome Checker <a name="pr1"></a>
**Problem:** Implement a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards). Use string methods to remove whitespace and punctuation, and compare the modified string with its reverse.

**Solution:**
1. Import the `string` module: The first step is to import the `string` module, which provides a set of string constants and functions for manipulating strings.
```python
import string
```
2. Define a function to check if a word is a palindrome: The next step is to define a function called `check_palindrome` that takes a string `word` as input and returns `True` if the string is a palindrome, and `False` otherwise.
```python
def check_palindrome(word):
```
3. Convert the string to lowercase: The first step inside the function is to convert the input string to lowercase using the `lower()` string method. This ensures that the palindrome check is case-insensitive.
```python
    word = word.lower()
```
4. Remove punctuation: The next step is to remove any punctuation characters from the string using the `translate()` string method and the `string.punctuation` constant. The `translate()` method takes a translation table as input, which maps each character in the string to a replacement character. In this case, we're using the `maketrans()` function to create a translation table that maps each punctuation character to an empty string, effectively removing them from the string.
```python
    word = word.translate(str.maketrans("", "", string.punctuation))
```
5. Remove whitespace: The next step is to remove any whitespace characters from the string using the `replace()` string method. This ensures that the palindrome check is not affected by spaces or other whitespace characters.
```python
    word = word.replace(" ", "")
```
6. Check if the string is a palindrome: The final step is to check if the string is a palindrome by reversing it using slicing with a step of `-1` (`word[::-1]`) and comparing it to the original string. If the two strings are equal, then the input string is a palindrome.
```python
    return word == word[::-1]
```
7. Get user input: The next step is to get user input using the `input()` function and store it in a variable called `example`.
```python
example = input("Enter a word: ")
```
8. Call the `check_palindrome` function: The next step is to call the `check_palindrome` function with the user input as the argument and store the result in a variable called `is_palindrome`.
```python
is_palindrome = check_palindrome(example)
```
9. Print the result: The final step is to print the result using an `if` statement. If the `is_palindrome` variable is `True`, then we print "Palindrome😍", otherwise we print "Not a palindrome🤣".
```python
if is_palindrome:
    print("Palindrome😍")
else:
    print("Not a palindrome🤣")
```

**Full Code**
```python
# imports
import string

def check_palindrome(word):
    # convert the word to lowercase
    word = word.lower()
    
    # remove punctuations
    word = word.translate(str.maketrans("", "", string.punctuation))
    
    # remove whitespaces
    word = word.replace(" ", "")
    
    # Reverse the string using slicing with a step of -1
    return word == word[::-1]

exaample = input("Enter a word: ")
# check_palindrome(exaample)

if check_palindrome(exaample):
    print("Palindrome😍")
else:
    print("Not a palindrome🤣")
```
In summary, this code defines a function called `check_palindrome` that takes a string as input and returns `True` if the string is a palindrome, and `False` otherwise. It then gets user input, calls the `check_palindrome` function with the user input, and prints the result. The function uses various string methods to preprocess the input string before checking if it's a palindrome.

## Exercise 2: Password Strength Checker <a name="pr2"></a>
**Problem:** Create a program that prompts the user to enter a password and evaluates its strength. Use string methods to check for various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters.

**Solution:**
1. Import the `string` module: The first step is to import the `string` module, which provides a set of string constants and functions for manipulating strings.
```python
import string
```
2. Define a function to check if a passkey is strong: The next step is to define a function called `is_passkey_strong` that takes a string `passkey` as input and returns `True` if the passkey is strong, and `False` otherwise.
```python
def is_passkey_strong(passkey):
```
3. Check passkey length: The first step inside the function is to check if the passkey is at least 8 characters long using the `len()` function.
```python
    length = len(passkey) >= 8
```
4. Check for uppercase letters: The next step is to check if the passkey contains at least one uppercase letter using the `isupper()` string method and the `any()` function.
```python
    uppercase_check = any(key.isupper() for key in passkey)
```
5. Check for lowercase letters: The next step is to check if the passkey contains at least one lowercase letter using the `islower()` string method and the `any()` function.
```python
    lowercase_check = any(key.islower() for key in passkey)
```
6. Check for special characters: The next step is to check if the passkey contains at least one special character using the `punctuation` constant from the `string` module and the `any()` function.
```python
    special_char_check = any(key in string.punctuation for key in passkey)
```
7. Check for numbers: The next step is to check if the passkey contains at least one number using the `isdigit()` string method and the `any()` function.
```python
    number_check = any(key.isdigit() for key in passkey)
```
8. Check passkey strength: The final step is to check if the passkey meets all the criteria for a strong passkey. If it does, then the function returns `True`, otherwise it returns `False`.
```python
    if (length and uppercase_check and lowercase_check and special_char_check and number_check):
        return True
    elif (length and uppercase_check and lowercase_check and special_char_check):
        return True
    elif (length and uppercase_check and lowercase_check):
        return False
    else:
        return False
```
9. Get user input: The next step is to get user input using the `input()` function and store it in a variable called `user_key`.
```python
user_key = input("Kindly create a passkey: ")
```
10. Check passkey strength: The final step is to call the `is_passkey_strong` function with the user input as the argument and print the result using an `if` statement. If the passkey is strong, then we print "Your 🔐 is 💪", otherwise we print "Enter a strong 🔐.....", and repeat the input process until a strong passkey is entered.
```python
while True:
    user_key = input("Kindly create a passkey: ")
    if is_passkey_strong(user_key):
        print("Your 🔐 is 💪")
        break
    else:
        print("Enter a strong 🔐.....")
```

**Full Code**
```python
import string

def is_passkey_strong(passkey):
    # checks for strong passkey
    length = len(passkey) >= 8
    uppercase_check = any(key.isupper() for key in passkey)
    lowercase_check = any(key.islower() for key in passkey)
    special_char_check = any(key in string.punctuation for key in passkey)
    number_check = any(key.isdigit() for key in passkey)
    
    # check all the criteria and return the comment
    if (length and uppercase_check and lowercase_check and special_char_check and number_check):
        return True
    elif (length and uppercase_check and lowercase_check and special_char_check):
        return True
    elif (length and uppercase_check and lowercase_check):
        return False
    else:
        return False

# ask for input   

# check passkey strength
while True:
    user_key = input("Kindly create a passkey: ")
    if is_passkey_strong(user_key):
        print("Your 🔐 is 💪")
        break
    else:
        print("Enter a strong 🔐.....")
```
In summary, this code defines a function called `is_passkey_strong` that takes a string as input and returns `True` if the string is a strong passkey, and `False` otherwise. It then gets user input, calls the `is_passkey_strong` function with the user input, and prints the result. The function uses various string methods and the `any()` function to check if the passkey meets the criteria for a strong passkey. The code also uses a `while` loop to repeatedly prompt the user for input until a strong passkey is entered.

## Exercise 3: Anagram Finder<a name="pr3"></a>
**Problem:** Develop a program that takes two strings as input and determines if they are anagrams (contain the same letters but in a different order). Use string methods to remove whitespace and compare the sorted versions of the strings.

**Solution:**
1. Import the `string` module: The first step is to import the `string` module, which provides a set of string constants and functions for manipulating strings.
```python
import string
```
2. Define a function to check if two strings are anagrams: The next step is to define a function called `is_anagram` that takes two strings `str1` and `str2` as input and returns `True` if the strings are anagrams of each other, and `False` otherwise.
```python
def is_anagram(str1, str2):
```
3. Remove whitespace: The first step inside the function is to remove any whitespace characters from both strings using the `replace()` string method.
```python
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
```
4. Remove punctuation: The next step is to remove any punctuation characters from both strings using the `translate()` string method and the `string.punctuation` constant.
```python
    str1 = str1.translate(str.maketrans("", "", string.punctuation))
    str2 = str2.translate(str.maketrans("", "", string.punctuation))
```
5. Convert to lowercase: The next step is to convert both strings to lowercase using the `lower()` string method.
```python
    str1 = str1.lower()
    str2 = str2.lower()
```
6. Sort the characters: The next step is to sort the characters in both strings using the `sorted()` function, which takes an iterable as input and returns a new sorted list containing the elements of the original iterable in ascending order.
```python
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
```
7. Check if the sorted strings are equal: The final step is to check if the sorted strings are equal using the `==` operator. If they are equal, then the input strings are anagrams of each other.
```python
    return sorted_str1 == sorted_str2
```
8. Get user input: The next step is to get user input using the `input()` function and store it in variables called `input_str1` and `input_str2`.
```python
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
```
9. Call the `is_anagram` function: The final step is to call the `is_anagram` function with the user input as the arguments and print the result using an `if` statement. If the strings are anagrams, then we print "The strings are anagrams.", otherwise we print "The strings are not anagrams.".
```python
if is_anagram(input_str1, input_str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
```

**Full Code**
```python
import string

def is_anagram(str1, str2):
    # Remove whitespace from both strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Remove punctuation from both strings
    str1 = str1.translate(str.maketrans("", "", string.punctuation))
    str2 = str2.translate(str.maketrans("", "", string.punctuation))

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the characters in both strings
    # sorted takes an iterable as input
    # returns a new sorted list containing the elements of the original iterable in ascending order.
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal
    return sorted_str1 == sorted_str2

# Test the is_anagram function
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

if is_anagram(input_str1, input_str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

```
In summary, this code defines a function called `is_anagram` that takes two strings as input and returns `True` if the strings are anagrams of each other, and `False` otherwise. It then gets user input, calls the `is_anagram` function with the user input, and prints the result. The function uses various string methods to preprocess the input strings, and then sorts the characters in the strings and checks if the sorted strings are equal to determine if the input strings are anagrams.

## Exercise 4: Text Encryption/Decryption<a name="pr4"></a>
**Problem:** Build a program that encrypts and decrypts text using a simple substitution cipher. Implement string methods to manipulate the text, such as shifting characters, replacing characters, or reversing the string.

**Solution:**
1. Initialize the encrypted text: The first step inside the function is to initialize an empty string called `encrypted_text` that will be used to store the encrypted version of the input text.
```python
encrypted_text = ""
```
2. Iterate over the characters in the input text: The next step is to iterate over each character in the input text using a `for` loop.
```python
for char in text:
```
3. Replace characters with their 8-bit binary representation: For each character in the input text, the function replaces the character with its 8-bit binary representation using the `format()` function and the `ord()` function. The `ord()` function returns the Unicode code point of the character, and the `format()` function formats the code point as an 8-bit binary string using the '08b' format code.
```python
    binary_representation = format(ord(char), '08b')  # Get the 8-bit binary representation
```
4. Add the binary representation to the encrypted text: The binary representation of the character is then added to the `encrypted_text` string, followed by a space character.
```python
    encrypted_text += binary_representation + " "
```
5. Remove trailing whitespace: The final step is to remove any trailing whitespace from the `encrypted_text` string using the `strip()` string method.
```python
return encrypted_text.strip()  # Remove trailing whitespace
```
6. Get user input: The next step is to get user input using the `input()` function and store it in a variable called `input_text`.
```python
input_text = input("Enter the text: ")
```
7. Call the `encrypt` function: The final step is to call the `encrypt` function with the user input as the argument and store the result in a variable called `encrypted_text`. The encrypted text is then printed to the console using the `print()` function.
```python
encrypted_text = encrypt(input_text)
print("Encrypted text:", encrypted_text)
```

**Full Code**
```python
def encrypt(text):
    encrypted_text = ""
    for char in text:
        # Replace characters with their 8-bit binary representation
        # convert the Unicode code point of the character char to its 8-bit binary representation
        binary_representation = format(ord(char), '08b')  # Get the 8-bit binary representation
        encrypted_text += binary_representation + " "

    return encrypted_text.strip()  # Remove trailing whitespace


# Test the encryption and decryption functions
input_text = input("Enter the text: ")

encrypted_text = encrypt(input_text)
print("Encrypted text:", encrypted_text)

```
In summary, the `encrypt` function takes a string as input and returns a string containing the 8-bit binary representation of each character in the input string, separated by space characters. The function uses the `format()` function to convert the Unicode code point of each character to its 8-bit binary representation, and then concatenates the binary representations into a single string. The function also removes any trailing whitespace from the encrypted text before returning it. The code then gets user input, calls the `encrypt` function with the user input, and prints the encrypted text to the console.

## Exercise 5: URL Parser<a name="pr5"></a>
**Problem:** Create a program that parses a URL and extracts specific components like the protocol, domain, path, and query parameters. Utilize string methods to extract and manipulate different parts of the URL.

**Solution:**
1. Remove the protocol prefix: The first step inside the function is to remove the protocol prefix (if present) from the input URL using the `startswith()` string method and string slicing.
```python
if url.startswith("http://"):
    url = url[len("http://"):]
elif url.startswith("https://"):
    url = url[len("https://"):]
```
2. Split the URL into domain and path/query parts: The next step is to split the input URL into domain and path/query parts using the `split()` string method. The `split()` method splits the input string into a list of substrings based on a specified separator. In this case, the separator is the first occurrence of the '/' character.
```python
parts = url.split("/", 1)
domain = parts[0]
path_query = parts[1] if len(parts) > 1 else ""
```
3. Split the path/query part into path and query parameters: The path/query part of the URL is then split into path and query parameters using the `split()` string method. The separator is the first occurrence of the '?' character.
```python
parts = path_query.split("?", 1)
path = parts[0]
query = parts[1] if len(parts) > 1 else ""
```
4. Return a dictionary containing the parsed URL parts: The final step is to return a dictionary containing the parsed URL parts, including the domain, path, and query parameters.
```python
return {
    "domain": domain,
    "path": path,
    "query": query
}
```
5. Get user input: The next step is to get user input using the `input()` function and store it in a variable called `input_url`.
```python
input_url = input("Enter the URL: ")
```
6. Call the `parse_url` function: The final step is to call the `parse_url` function with the user input as the argument and store the result in a variable called `parsed_url`. The parsed URL is then printed to the console using the `print()` function.
```python
parsed_url = parse_url(input_url)
print("Parsed URL:", parsed_url)
```

**Full Code**
```python
def parse_url(url):
    # Remove the protocol prefix if present
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    # Split the URL into domain and path/query parts
    parts = url.split("/", 1)
    domain = parts[0]
    path_query = parts[1] if len(parts) > 1 else ""

    # Split the path/query part into path and query parameters
    parts = path_query.split("?", 1)
    path = parts[0]
    query = parts[1] if len(parts) > 1 else ""

    return {
        "domain": domain,
        "path": path,
        "query": query
    }

# Test the URL parser
input_url = input("Enter the URL: ")

parsed_url = parse_url(input_url)
print("Parsed URL:", parsed_url)

```
In summary, the `parse_url` function takes a string as input and returns a dictionary containing the parsed URL parts, including the domain, path, and query parameters. The function first removes the protocol prefix (if present) from the input URL, and then splits the URL into domain and path/query parts using the `split()` string method. The path/query part is then split into path and query parameters using the `split()` string method. The function returns a dictionary containing the parsed URL parts. The code then gets user input, calls the `parse_url` function with the user input, and prints the parsed URL to the console.


## Exercise 6: Sentence Capitalizer<a name="pr6"></a>
**Problem:** Write a program that takes a paragraph as input and capitalizes the first letter of each sentence. Use string methods to split the paragraph into sentences, capitalize the first letter of each sentence, and join them back together.

**Solution:**
1. Split the paragraph into sentences: The first step inside the function is to split the input paragraph into sentences using the `split()` string method. The separator is the '. ' substring, which represents the end of a sentence followed by a space.
```python
sentences = paragraph.split(". ")
```
2. Capitalize each sentence: The next step is to capitalize the first letter of each sentence using the `capitalize()` string method. This is done using a list comprehension that applies the `capitalize()` method to each sentence in the `sentences` list.
```python
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
```
3. Join the capitalized sentences into a paragraph: The capitalized sentences are then joined back together into a single paragraph using the `join()` string method. The separator is the '. ' substring, which represents the end of a sentence followed by a space.
```python
capitalized_paragraph = ". ".join(capitalized_sentences)
```
4. Return the capitalized paragraph: The final step is to return the capitalized paragraph as a string.
```python
return capitalized_paragraph
```
5. Get user input: The next step is to get user input using the `input()` function and store it in a variable called `input_paragraph`.
```python
input_paragraph = input("Enter the paragraph: ")
```
6. Call the `capitalize_sentences` function: The final step is to call the `capitalize_sentences` function with the user input as the argument and store the result in a variable called `capitalized_paragraph`. The capitalized paragraph is then printed to the console using the `print()` function.
```python
capitalized_paragraph = capitalize_sentences(input_paragraph)
print("Capitalized Paragraph:")
print(capitalized_paragraph)
```

**Full Code**
```python
def capitalize_sentences(paragraph):
    sentences = paragraph.split(". ")
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    capitalized_paragraph = ". ".join(capitalized_sentences)
    return capitalized_paragraph

# Test the program
input_paragraph = input("Enter the paragraph: ")

capitalized_paragraph = capitalize_sentences(input_paragraph)
print("Capitalized Paragraph:")
print(capitalized_paragraph)
```
In summary, the `capitalize_sentences` function takes a string as input and returns a new string with the first letter of each sentence capitalized. The function first splits the input string into sentences using the `split()` string method, and then applies the `capitalize()` string method to each sentence using a list comprehension. The capitalized sentences are then joined back together into a single string using the `join()` string method. The code then gets user input, calls the `capitalize_sentences` function with the user input, and prints the capitalized paragraph to the console.

## Conclusions <a name="summ"></a>
In conclusion, this article has provided an introduction to some of the most commonly used string methods in Python. We have seen how to use these methods to manipulate strings in various ways, such as removing whitespace, punctuation, and special characters, checking for anagrams, encrypting and decrypting text, parsing URLs, and capitalizing sentences. These string methods are powerful tools that can help you perform complex operations on strings with just a few lines of code. By mastering these methods, you can improve your productivity and write more efficient and effective code. Whether you are a beginner or an experienced programmer, understanding how to work with strings is an essential skill that will serve you well in your programming journey.
