# Day 8: File Handling and I/O Operations

## Contents
[Introduction](#intro)

[Handling Files](#handle)


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

## CSV Files
CSV stands for comma-separated values. 

CSV files can be read by a range of different spreadsheet software packages as well as Python files. 

CSV files contain data structured so that a comma separates individual items in the file, and each record is on a new line of the file.

A CSV file can be created in a text editor by changing the extension of the file to .csv

You can also create CSV files in spreadsheet software by exporting them as a .csv file. 




## Conclusion

In this article, we learned how to perform file handling and I/O operations in Python. We covered how to open and close files, read and write data to files, handle file errors and exceptions, and create a file organizer project. File handling is an important skill to have in Python, as it allows us to work with data stored on disk.