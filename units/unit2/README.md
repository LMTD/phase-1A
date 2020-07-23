# LMTD Phase One - Unit Two - Python
Understanding the Python programming language

## Introduction to Python ([from Real Python](https://realpython.com/learning-paths/python3-introduction/))
"Python is a beautiful language. It’s easy to learn and fun, and its syntax is simple yet ele- gant. Python is a popular choice for beginners, yet still powerful enough to back some of the world’s most popular products and applications from companies like NASA, Google, Mozilla, Cisco, Microsoft, and Instagram, among others. Whatever the goal, Python’s design makes the programming experience feel almost as natural as writing in English.

Check out [Real Python](https://realpython.com) to learn more about Python and web development."


### Primitives and Data Types
#### Numbers, Strings, and Booleans

##### Numbers
```
#Python has integers and floats. 
#Integers are simply whole numbers, like 314, 500, and 716. 
#Floats are fractional numbers like 3.14, 2.867, 76.88887. 

>>> type(3) <class 'int'> 
>>> type(3.14) <class 'float'> 
>>> pi = 3.14 
>>> type(pi) <class 'float'>
#You can use the type method to check the value of an object.

>>> type(3) 
<class 'int'> 
>>> type(3.14) 
<class 'float'> 
>>> pi = 3.14 
>>> type(pi) 
<class 'float'>

#You can use the basic mathematical operators:

>>>3+3 
6 
>>>3-3 
0 
>>>3/3 
1.0 
>>>3/2
```

##### Strings
```
#A string of characters - anything you can type on the keyboard in one keystroke
#Python recognizes '' and "" as the beginning and end of strings

>>> a = "first" 
>>> b = "last" 
>>>a+b 
'firstlast'

#String methods for you to choose from - like upper(), lower(), replace(), and count()
#
>>>str = 'woah!' 
>>>str.upper() 
'WOAH!'

>>>str.lower() 
'woah!'

>>>str.replace('a', 'r')
>>>str.replace('h', 'd') 
'word'

>>>str.count('w')
1

#You can format/create strings with the format() method.
>>>"{0} is a lot of {1}".format("Python", "fun!") 
'Python is a lot of fun!'
```


##### Booleans
```
#Boolean values are simply True or False
#We check to see if a value is equal to another value with two equal signs.

>>>10==10 
True 
>>>10==11 
False
>>> "jack" == "jack" 
True
>>> "jack" == "jake" 
False

#To check for inequality use !=
>>>10!=10 
False 
>>>10!=11 
True
>>> "jack" != "jack" 
False
>>> "jack" != "jake" 
True

#You can also test for>,<,>=, and<=
>>>10>10 
False 
>>>10<11
True 
>>>10>=10 
True 
>>>10<=11 
True
>>>10<=10<0 
False 
>>>10<=10<11 
True
>>> "jack" > "jack" 
False

```


### Collections
#### Lists
```
#Lists are containers for holding values as variables
>>> number_list =['one', 'two', '3' 'one', 'two', 'two'] 

#To access the elements in the list you can use their index value. 
#Just remember that all lists starts at index 0, not 1

>>> number_list[2]
'two'

#You can count from the end as well
>>> number_list[-3]
'one'

#Lists also contain methods
#Use len to check the size of the list
>>> number_list.len()
6

#Check to see if a value exists 
>>> 'two' in number_list
True
```
#### Dictionaries
```
#Dictionaries use key/value pairs for element lookup
>>> words = {'apple': 'red','lemon': 'yellow'} 
>>> words
{'apple': 'red', 'lemon': 'yellow'}
>>> words['apple']
'red'
>>> words['lemon'] 
'yellow'

#Output all the keys with keys() and all the values with values()
>>> words.keys() 
dict_keys(['apple', 'lemon']) 
>>> words.values() 
dict_values(['red', 'yellow'])
```
### Control Statements
#### If/Else Statements
```
>>>num=20
>>> if num == 20:
        print('the number is 20')
    elif num > 20:
        print('the number is greater than 20')
    else:
      print('the number is not 20')


the number is 20

```
#### Loops
```
#Python uses for-loops and while-loops

>>> colors = ['red', 'green', 'blue'] 
>>> colors
['red', 'green', 'blue']
>>> for color in colors:
       print('I love ' + color)

I love red I love green I love blue

>>>num=1
>>> num
1 
>>> while num <= 5: print(num)
        print(num)
        num+=1

1 
2 
3
4 
5
```
### Functions
```
#Functions are blocks of reusable code that perform a single task.

>>> def multiply(num1, num2=10):    
        return num1 * num2
 
>>> multiply(2)
20

```

### File Handling

Python makes it easy for us to interact with files of various formats.

#### Opening and Closing a File

##### Opening a File
```
my_file = open('data.txt', 'w')

```
In order to open a file you use the `open()` function and pass in a filename that represents the relative or absolute path to the file you're referencing, and an argument that determines the mode of opening. There are different modes, which determine the actions you're able to do with the open file.

Some modes include:
mode | description
--|--
r | (default) mode to open file for reading
w | open the file for writing (overwriting any existing data)
x | creates a new file (fails if file already exists)
a | open the file for writing (appending new data to the end)
b | write binary data to files
+ | allow reading and writing to a mode (ex: `w+` allows writing then reading)

##### Closing a File
```
my_file.close()

```
To close a file, you can call the `close()` function on the object you created when opening. It is important to close the file after you've used it in order to save CPU space and evade data corruption possibilities.

In order to make it easier to automatically close files after Python has used it you can use the `with` keyword like so:

```
with open('data.txt', 'w') as my_file:
        pass # you can write code to handle the file here

```

Using the `with` keyword is the recommended approach for opening files.

#### Saving to a Text File
```
with open('data.txt', 'w') as my_file:
        my_file.write('Hello World!\n')
        my_file.write('We're writing to a file!\n')
```
The `write()` function takes in a string and puts the content into our file. We insert a newline character `\n` into the string in order to make sure the text is added to new lines.

##### Saving Multiple Lines
```
with open('data.txt', 'w') as my_file:
        fruits = ['Apple\n', 'Banana\n', 'Cherry\n']
        my_file.writelines(fruits)
```
The `writelines()` function takes in a sequence of strings or bytes and puts the content into our file. This function does not work with other data types and objects however.


### In Class Exercises

### Group Challenge with Python Functions

#### Challenge One (Input and String Formatting)

You and a partner will try to use your knowledge of Python to create a MadLib function.

HOW-TO: Create a multi-line string variable called my_story which contains a short story about an animal in a specific borough of New York, performing some action involving one specific type of food.

TODO: Ask the user through the command line for their picks for 'animal', 'borough', 'action' and 'food'

TODO: Create a Python program that swaps those items in your story

TODO: Print the user's story to the command line

#### Challenge Two (Input and Boolean Logic)

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
* Rock beats scissors
* Scissors beats paper
* Paper beats rock

#### Challenge Three (Dictionaries)

Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:
```
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
```
#### Challenge Four (List Operations)

Write a function called is_palindrome that determines whether a given string is a palindrome and returns True or False. A palindrome is a word that is spelled the same forward, and backward (i.e. "WOW", "MOM", "RACECAR") 


#### Challenge Five (Classes)

Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 

Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

Write a Python class named Triangle constructed by a base and a height, a list of angles, and a method to calculate the area of a triangle.

## Resources
* [Python practice exercises](https://www.w3resource.com/python-exercises/python-functions-exercises.php)
* [W3Schools - Learn Python for Free](https://www.w3schools.com/python/python_getstarted.asp)
* [More Python Knowledge](https://realpython.com/learning-paths/python3-introduction/)
* [Saving Text/JSON/CSV to a file](https://stackabuse.com/saving-text-json-and-csv-to-a-file-in-python/)
* [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
