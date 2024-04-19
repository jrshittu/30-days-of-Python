# Day 8: File Handling and I/O Operations

## Contents
[Introduction](#intro)

[Handling Files](#handle)

[CSV Files](#csv)

[Conclusion](#conc)


## Introduction
<a name="intro"></a>In Python, files are used to store data permanently on disk. File handling involves reading, writing, and manipulating data stored in files. In this article, we will explore how to perform file handling and I/O operations in Python.

A file is a term used to describe data that is held in storage on a computer. 
Files come in many forms, for example:
- Text files
- Image files
- Video files
- Sound files
 
## Handling Files
File handling is a term used to describe how programs work with the files that are stored in a computer. 
Having the ability to use file-handling techniques in your own programs opens up endless possibilities.

All of the programs that you have created so far have lost any data generated within them once they have been terminated.
Saving program data to an external file allows you to use that data again. 

An example of when this might be used is to keep track of the highest score for a game. 

A **text file** can be used to store the highest score and this can be accessed and modified each time the game is played. 


## Key File Handling Techniques
The key file-handling techniques that you need to be able to use are:
- Open
- Read
- Close
- Write
- Append

### Open and read a text file
In order to read the data stored in a text file, you must open it first. 

Think of it a bit like a book. You can’t read what is inside if you don’t open it first. 

Here is an instruction that will open a text file in read mode. 

```python
file = open("quick.txt","r")
```
- Creates an identifier for the file that is to be accessed.
- Calls a function that returns a file object.
- The first argument is the name of the text file to be opened. 
- The second argument is the mode that the file will be opened.

There are four modes for opening a file:
* 'r' - Read mode (default)
* 'w' - Write mode
* 'a' - Append mode
* 'r+' - Read and write mode

**Read a Text File**

To read the contents of a text file, we can use the read() method on the file object: Once a file has been opened, it can then be read. 
```python
file = open("quick.txt","r")
quicktext = file.read()
```

After we are done working with a file, it's important to close it using the close() method. This ensures that any changes made to the file are saved and the file is released from memory.
```python
file.close()
```
Reading and Writing to Files

To read data from a file, we can use the read() method. This method reads the entire contents of the file and returns it as a string.
```python
file = open('example.txt', 'r')
contents = file.read()
print(contents)
file.close()
```
To write data to a file, we can use the write() method. This method writes a string to the file.
```python
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
```
We can also use the writelines() method to write a list of strings to a file.
```python
file = open('example.txt', 'w')
lines = ['Hello, World!\n', 'This is a test.\n']
file.writelines(lines)
file.close()
```
File Errors and Exceptions

When working with files, it's important to handle errors and exceptions that may occur. For example, if we try to open a file that doesn't exist, Python will raise a FileNotFoundError. We can handle this error using a try-except block.
```python
try:
    file = open('example.txt', 'r')
    contents = file.read()
    print(contents)
    file.close()
except FileNotFoundError:
    print('File not found.')
```
Project: File Organizer

For this project, we will create a file organizer that moves files from one directory to another based on their file extension.

Step 1: Create a directory called 'files' and add some files with different file extensions to it.

Step 2: Create a dictionary that maps file extensions to their respective directories.
```python
file_extensions = {
    'txt': 'text_files',
    'jpg': 'image_files',
    'png': 'image_files',
    'pdf': 'document_files'
}
```
Step 3: Loop through the files in the 'files' directory and move them to their respective directories based on their file extension.
```python
import os
import shutil

for filename in os.listdir('files'):
    extension = filename.split('.')[-1]
    if extension in file_extensions:
        directory = file_extensions[extension]
        if not os.path.exists(directory):
            os.makedirs(directory)
        shutil.move(os.path.join('files', filename), os.path.join(directory, filename))
```
Step 4: Run the script and verify that the files have been moved to their respective directories.

## CSV Files <a name="csv"></a>
CSV stands for comma-separated values. 

CSV files can be read by a range of different spreadsheet software packages as well as Python files. 

CSV files contain data structured so that a comma separates individual items in the file, and each record is on a new line of the file.

A CSV file can be created in a text editor by changing the extension of the file to .csv

You can also create CSV files in spreadsheet software by exporting them as a .csv file. 

When you open a CSV file in spreadsheet software, the commas are used as a guide to display the data neatly in rows and columns. 

When a CSV file is opened in spreadsheet software, it is displayed in tabular format. 

A CSV file is still a text file. Each row is stored as string. 

Modern spreadsheet software will typically recognise a number and store it as that data type.

Python will not do this automatically. Any data is always read as string and will need to be casted before it is used as any other data type. 

### Reading a CSV File
To read a CSV file, we first need to open it using the `open()` function with the file name and mode 'r' for reading. Then, we create a `csv.reader()` object by passing the file object to it. The `csv.reader()` object reads the CSV file line by line and returns an iterator that yields a list of values for each row.

Here's an example of reading a CSV file:
```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```
In this example, we open the file 'example.csv' in read mode and create a `csv.reader()` object. Then, we loop through the rows in the CSV file using a for loop and print each row as a list.

By default, the `csv.reader()` object assumes that the delimiter is a comma. However, we can specify a different delimiter using the `delimiter` parameter. For example, to read a TSV (Tab Separated Values) file, we can set the delimiter to '\t':
```python
import csv

with open('example.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
```
In addition to reading the data as lists, we can also read it into a dictionary using the `csv.DictReader()` class. This is useful when we want to access the values in each row using the column names as keys. To use `csv.DictReader()`, we need to pass the file object and a list of column names as arguments. The first row of the CSV file should contain the column names.

Here's an example of reading a CSV file into a dictionary:
```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.DictReader(file, fieldnames=['Name', 'Age', 'Gender'])
    for row in reader:
        print(row)
```
In this example, we create a `csv.DictReader()` object and pass it the file object and a list of column names. Then, we loop through the rows in the CSV file and print each row as a dictionary.

### Write to CSV File
Writing to a CSV file is very similar to writing to a standard text file. 

The key thing is to remember how a CSV file is structured. 

The next thing to remember is that a CSV file is a text file. You can only write data to it that has the string data type. 

Here is a program that is attempting to write an integer to a CSV file. 

```python
file = open("numbers.csv", "w")
numbers = 3
file.write(numbers)
file.close()
```

When executed, this error message will occur. 

```
TypeError: write() argument must be str, not int
```

Any data written to a CSV file must be sent in the format that it requires:

- Data must have the string data type
- Each item should be separated by a comma
- Each new row or record should be indicated by a line space \n which stands for newline

Writing a List of Numbers to a CSV File in Python
--------------------------------------------------

In this example, we'll write a list of numbers to a CSV file using Python. Here are the steps:

### Step 1: Create a List of Numbers

First, let's create a list of numbers that we want to write to the CSV file:
```css
numbers = [3, 4, 5]
```
### Step 2: Convert the Numbers to Strings

Next, we need to convert the numbers to strings so that we can write them to the CSV file. We'll use a for loop to iterate through the list of numbers and append each string representation to a new list:
```css
str_numbers = []
for number in numbers:
    str_numbers.append(str(number))
```
### Step 3: Join the Strings into a Single String

Now that we have a list of string representations of the numbers, we need to join them into a single string separated by commas. We can use the `",".join(str_numbers)` method to do this:
```makefile
data = ",".join(str_numbers)
```
### Step 4: Open the File in Write Mode

Next, we need to open the CSV file in write mode. We'll use the `open()` function to do this:
```python
file = open("numbers.csv", "w")
```
### Step 5: Write the Data to the File

Now we can write the data to the CSV file using the `write()` method:
```scss
file.write(data)
```
### Step 6: Close the File

Finally, we need to close the file using the `close()` method:
```python
file.close()
```
And that's it! When we run this code, a new CSV file named "numbers.csv" will be created in the current directory, containing the list of numbers separated by commas.

Here's the complete code:
```css
numbers = [3, 4, 5]

str_numbers = []
for number in numbers:
    str_numbers.append(str(number))

data = ",".join(str_numbers)

file = open("numbers.csv", "w")
file.write(data)
file.close()
```

## Conclusion

In this article, we learned how to perform file handling and I/O operations in Python. We covered how to open and close files, read and write data to files, handle file errors and exceptions, and create a file organizer project. File handling is an important skill to have in Python, as it allows us to work with data stored on disk.