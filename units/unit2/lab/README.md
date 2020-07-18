# LMTD Phase One - Unit Two - Lab
Object Oriented Python Programs on the Command Line

## About This Lab
This lab is designed to extend your knowledge of Python, and give you an opportunity to write your first robust application for the command line. Object Oriented Programming is a widely used programming paradigm that allows you to represent aspects of the real-world in code. In this Lab you and your group will write an Object-Oriented program that sets a blueprint for multiple classes / objects to be created via an application on the command line.
 
## About OOP
An Object Oriented Program (OOP) is a programming paradigm focused on structuring programs around objects containing intrinsic *properties* and *behaviors*. The OOP approach allows us to model real world things into code. 

### Defining Classes
In an OOP architecture the most important object is the Class. Classes allow us to create more manageable code by providing an interface and blueprint for creating user-defined data structures. Classes define functions, called methods, which instances of the class are able to call.

Defining a class in Python is started with the class keyword, followed by the name of the class (capitalized) and a colon. Everything indented below the class definition is a part of the class's body.

```
class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
```
All classes are required to create a `.__init__()` function which sets the initial state of any new instances of the class. Any parameters passed into the `.__init__` function will be required when a user attempts to create a new object from our class blueprint. 

In the body of the `.__init__` is where we set the default values of any attributes, using the `self` keyword. In the example above `self.length` creates an attribute called length and assigns it's value.

Any attributes created in the `.__init__` function is called an instance attribute, meaning it's values will belong to a specific instance of the class.

The indentation you use for methods in a class declaration is important, as it tells Python whether the variable is a part of the class as an instance attribute or a class attribute.

A class attribute is an attribute defined outside of the `.__init__` function. Class attribues have the same value for all class instances. 

```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

```
In the above example, `shape` is a Class attribute meaning it would be called with: `.shape` on the class `Box.shape` or on any instance of the class.

Use class attributes to define properties that should have the same value for every class instance. Use instance attributes for properties that vary from one instance to another.


### Instantiating Objects

Once you've created your class blueprint, instantiating an object is simple. You just call the class name and pass any required parameters into the `.__init__` like so:
```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

box1 = Box(5,4,3) # instantiating a Box object
box2 = Box(10, 12, 15)

```
To pass arguments to the `.__init__` function you just pass it in the parentheses after the class name. This creates two *instances* of our Box class, `box1` and `box2`. We can use these objects much like we use other data types. We can put them into lists, dictionaries, and sets, use them in other functions we define outside of the Class, and much more.

In order to access the values of these `Box` instances, you can use **dot notation** to retrieve their attributes. 
```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

box1 = Box(5,4,3) # instantiating a Box object
box2 = Box(10, 12, 15)

print(box1.height)

if(box1.height > 5):
    print(True)
else:
    print(False)

boxes = [box1, box2]

```
You can also retrieve class attributes using dot syntax the same way. 
```
print(box1.shape)
'Cuboid'

```
Classes are beneficial because they allow us to organize data in more generalized ways. The class is the blueprint that allows us to create multiple objects with the same attributes and methods.

### Changing Values

```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

box1 = Box(5,4,3) # instantiating a Box object
box2 = Box(10, 12, 15)

print(box1.height)

box1.height = 10 # updating object

```
Any custom object is mutable, meaning you can change it's value dynamically.

### Instance Methods

**Instance methods** are functions that are defined inside a class, and can only be called by instances of the class. 

All instance methods, just like `.__init__` must pass the keyword `self` as the first argument.

```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    # instance method
    def area(self):
        return self.length * self.width * self.height
        
    # instance method
    def ship_to(self, name):
        return f"Box has been shipped to {name}

box1 = Box(5,4,3) # instantiating a Box object

box1.area()
box1.ship_to("Cam")

```

### Special Methods (dunder/magic functions)
When you create classes it's a good idea to have a method that returns a string containing userful info about the instance of the class. For instance when we run: `print([1,2,3])` we get a string that looks like a list.

You can use the special instance method called: `.__str__()` to achieve this functionality with your custom classes.

```
class Box:
    # Class attribute
    shape = "Cuboid"

    #instance method (dunder)
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    #instance method (dunder)
    def __str__(self):
        return f"Length: {self.length}, Width: {self.width}, Height: {self.height}"
    
    # instance method
    def area(self):
        return self.length * self.width * self.height
        
    # instance method
    def ship_to(self, name):
        return f"Box has been shipped to {name}



box1 = Box(5,4,3) # instantiating a Box object

box1.area()
box1.ship_to("Cam")

```
Methods like `.__init__` or `.__str__` are called **dunder methods** because of their use of double underscores at the beginning and end of the function name. There are many dunder methods you can use in Python which you can check out [here](https://dbader.org/blog/python-dunder-methods)

### Inheritance

One of the most important topics with relation to classes and objects, and OOP is **Inheritance** or the process by which one class takes on attributes and methods from another class. When one class is formed off of the blueprint of another it is called a **child class** and the class that served as a blueprint is called the **parent class**

Child classes can extend the attributes and methods of a parent class. The child class *inherits* the properties of the parent class and can also specify attributes and methods of its own.

Say for instance we are in a Shipping Facility where there are many different types of boxes. We can extend our class definition to allow for inheritance and multiple types of Box classes.

```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    # instance method
    def area(self):
        return self.length * self.width * self.height
        
    # instance method
    def ship_to(self, name):
        return f"Box has been shipped to {name}

### Child Class
# pass the Parent class in the parentheses 

class SmallBox(Box):
    pass # so we can fill in later

class MediumBox(Box):
    pass # so we can fill in later

class LargeBox(Box):
    pass # so we can fill in later

```

Even though we have only defined the child class with no extra instance methods, because these classes subclass from our Box class we can still initiate them as we did before using the `.__init__` from the Parent class.

```
class Box:
    # Class attribute
    shape = "Cuboid"

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    # instance method
    def area(self):
        return self.length * self.width * self.height
        
    # instance method
    def ship_to(self, name):
        return f"Box has been shipped to {name}

### Child Class
# pass the Parent class in the parentheses 

class SmallBox(Box):
    pass # so we can fill in later

class MediumBox(Box):
    pass # so we can fill in later

class LargeBox(Box):
    pass # so we can fill in later

box3 = SmallBox(5, 3, 4)
box4 = MediumBox(10, 5, 10)
box5 = LargeBox(20, 10, 20)
```
These instances of the subclasses inherit all the attributes and methods of the parent class including the `.__init__`.

```
box3 = SmallBox(5, 3, 4)
box4 = MediumBox(10, 5, 10)
box5 = LargeBox(20, 10, 20)

print(box3.shape)
'Cuboid'

print(box4.height)
10

box5.ship_to("Cam")
"Box has been shipped to Cam"

```
Don't forget that you can use the `type()` function to determine which class a given object belongs to.

```
type(box5)
<class '__main__.LargeBox'>

```
You can also use the `isinstance()` function to check if an instance is a part of a particular class.

```
isinstance(box5, Box)
True

```

### Extending the Functionality of a Parent Class

With any subclass (child class), you can override any method that was previously defined by the Parent. Here is an example of us overriding the `ship_to()` function we originally created in the `Box` parent class.

```
### Child Class
# pass the Parent class in the parentheses 

class SmallBox(Box):
    def ship_to(self, name):
    return f"Small box has been shipped to {name}"
```

You can also make reference to the parent class from within any method in a child class by using `super()`
```
class SmallBox(Box):
    def area(self):
    return super().area(self.length, self.width, self.height)
```
In this example, we use the super class (parent class) to call the area function we already defined.

One of the important aspects about classes you'll come to understand is **Hierarchy** wherein you can trace the child class back up to the parent classes. Hierarchies can be simple or surprisingly complicated. The more you use Classes to create real-world applications, the more complex hierarchies you'll see.


## Lab 2 Objective
Working with a group, your goal for this Lab is to write an Object Oriented Program using the Command Line as an interface. Your group will be assigned a various real-world scenario and will have to create the Class interfaces and necessary methods to allow a user to interact with your classes via the command line. After you've finished, your group should try extending your program to do more creative functionality.

## Collaborating as a Group
Your group should [start a new project](https://repl.it/languages/python) and add eachother as collaborators to have one space to write and test your programs.

 Your group should start by breaking down the responsibilities of the work so that each person can be involved in writing at least one part of the class, and that everyone is able to read and present the final program you build. 
 

## Lab Assignment

### Step 1 - Define Your Class Interfaces
Start the project by defining your class interfaces meaning the class names, instance methods, and class methods necessary to get your program working.

### Step 2 - Test Your Interface
Instantiate some sample objects to make sure your class methods and attributes are working as expected.

### Step 3 - Create a Menu Class
The Menu class will be used to display a list of choices on the terminal for the user to run. You should instantiate an instance of your main class in your menu and present choices to the user to select from. For instance if I was building a Warehouse class to extend my Box analogy from earlier, my menu may look something like this:
```
class Menu:
 
 ''' Displays a list of choices on the terminal for  the user to run '''
 
 
 
 def __init__(self):
 
 
 
      self.warehouse = Warehouse()
 
 
 
      self.choices = {
 
           "1" : self.show_boxes,
 
           "2" : self.add_box,
 
           "3" : self.search_boxes,
 
           "4" : self.quit
 
 
 
        }
 
 
 
 
 
 def display_menu(self):
 
       print(""" 
 
 
 
             Warehouse Menu  
 
 
 
             1. Show boxes
 
             2. Add box
 
             3. Search boxes
 
             4. Quit program
 
             """)
 
 
 def run(self):
 
     ''' Display menu and respond to user choices '''
 
 
 
     while True:
 
           self.display_menu()
 
           choice = input("Enter an option: " )
 
           action = self.choices.get(choice)
 
           if action:
 
                action()
 
           else:
 
              print("{0} is not a valid choice".format(choice))
 
 
 
 
 
 def show_boxes(self):
    pass
 

 def add_box(self):
    pass
 
 
 def search_boxes(self):
    pass
     
 
 def quit(self):
 
      ''' quit or terminate the program '''
 
      print("Thank you for visiting the warehouse today")
 
      sys.exit(0)
 
 
if __name__ == "__main__":
 
    Menu().run()
```

You can take a look at my project structure on REPL [here](https://repl.it/@camunity/Warehouse-App) for some help with this part

### Refactor Code
Add code to separate files if you'd like to clean things up a bit, continue to test your functions and make sure your program runs as expected.

### Add More Functionality
Continue to create! Ideate and develop any new user experiences you'd like to have in your program!

## Submission
Please share a copy of your group's REPL link to us via the Lab submission form shared in Slack when you've finished. Continue to work on the NETACAD Python Essentials until our next class on Tuesday!

## Resources
* [OOP](https://realpython.com/python3-object-oriented-programming/#dog-park-example)
* [Python Classes](https://www.w3schools.com/python/python_classes.asp)
* [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)