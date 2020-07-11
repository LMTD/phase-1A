# LMTD Phase One - Unit One - Lab
Writing BASH Shell Scripts

## About This Lab
This lab is designed to give you an opportunity to continue your learning of Linux and BASH. Shell scripts are an important component to Linux programming that involve the execution of multiple Linux commands through files created in text-editors. In this Lab you and your group will write multiple BASH scripts to apply your knowledge of essential Linux commands.
 
## About Scripting
A shell script is a file that contains Linux commands written in [ASCII text](http://www.asciitable.com). To create a shell script, you need to create a BASH file, use a text editor to write your commands, set the right file permissions and put it in your path as an executable. BASH scripts are executed by calling the file name through the command line and can also be scheduled to run automatically using a special Linux command called `cron`. 

### Text Editors
Text editors are programs, like a word processor, that read and write ASCII text files. You can use text editors to write a number of different types of files including standard text (.txt), markdown (.md), and various programming languages (.py, .js, .html to name a few) There are many, many text editors available. Some are specifically built to run on Linux systems, and work from either the command line environment or a GUI. Here is a list of some common ones:

name|description|interface
--|--|--
vi/vim | vi is a powerful editor available on most UNIX-like systems making it a valuable tool to any Linux programmer. It's interface has a bit of a learning curve but is considered a rite-of-passage to other programmers working on UNIX-like operating systems. vim is an enhanced version of the traditional vi carried in most Linux distros | command line
emacs | emacs is another powerful editor available in UNIX-like systems including Linux. It was built by GNUs Richard Stallman and is considered to be a feature-rich text editor. It is a bit more intuitive than vi/vim and emacs and vi fans like to battle over which is better. | command line
nano | nano is an editor that is pretty lightweight and fairly easy to use. It is a great first editor for first-time users looking for a command line text editor. | command line
[VSCode](https://code.visualstudio.com/download) | Visual Studio Code is a program that works on most computers including Linux machines. It is a powerful GUI based text editor that is popular in a wide array of programming disciplines across the stack. | GUI
[Atom](https://atom.io) | Atom is another popular text editor used in a number of different programming disciplines across the stack. | GUI

### BASH files
There are a number of ways to create a new BASH file. The simplest way to do so from the command line though would be to use the `touch` command and pass your desired filename as an argument. Ex: `touch my_script` Now that you have created that file you can open it using a command line text editor using the name of the editor as a command. Ex: `nano my_script` (to open the file in nano).

Once you open your file in your text editor, the most important next step for any BASH file is to designate it as such for the shell to know what type of program is going to interpret the script.

Add this line to the top of all of your bash files: 
`#!/bin/bash`

The first line of the script is important. This is called a shebang. It tells the shell what type of program should be used to interpret the script. In our case this is /bin/bash but other scripting languages such as Perl or Python use this same mechanism.

### Example Shell Script

`#!/bin/bash`
`# My Awesome Script`
`echo "Hello World!"`

The second line is a comment. Anything appearing after a "#" symbol is ignored by bash when it's running. Use comments as your scripts get larger and more complicated so that other programmers can understand what is going on. The third line should be no surprise to most of you. This script uses the `echo` command to print "Hello World!" to the command line using STDOUT. 

### Setting Permissions
We use the `chmod` command in Linux to change a file's permissions. To use `chmod` to set permissions we need to tell it *Who* we are setting permissions for, *What* changes we are making whether adding or removing a permission, and *Which* permissions we're setting. We can do this via options or using a numerical shorthand. Learn more about setting user permissions [here](https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/) In order to edit and run our scripts we need to **make sure we have read, write, and executable permissions** as a user.

### Running a Command
Bash scripts are called on the command line like so: `bash my_script`. Another way to run the script is as so: `./my_script`. To make sure that you've written everything correctly in your file you can use the `cat` command to print the contents to the command line. Ex: `cat my_script` If your file isn't running as expected with the `./` syntax, double check your Linux commands, and ensure you have updated the proper user permissions. 


### Putting the Script in your PATH with /usr/local/bin

When you type any Linux commands normally, you don't usually need to write `bash` or `./` though right? The shell maintains a list of directories where executable files are kept and searches those directories for your file. The computer doesn't search it's entire harddrive for the program. If it does not find the program in that list of directories, it returns the error *command not found*

The list of directories that your computer searches is called your **PATH**, and any command stored in the path can be run simply by calling the command itself. This is important because if your script is not in your PATH the only way to call it is to call it from the directory where it was written using `bash` or `./` 

You can print the directories in your PATH by executing this command: `echo $PATH` 

One of the directories normally designated for folks to save important scripts they will call often is the `/usr/local/bin` You can move any of your important scripts there using the `mv` command as so: `mv my_script /usr/local/bin` once there, granted your file has the right executable permissions you should now be able to call the function from any sub-directory just as followed: `my_script`.


## Lab 1 Objective
Working with a group, your goal for this Lab is to write 5 Linux scripts while learning more about structuring Linux commands. You have creative freedom as a group to choose what your scripts do but each one should address the themes below. After you've finished, your group should try a creative challenge to connect the dots and write a more robust script to share.

## Collaborating as a Group
You can definitely use the Linux VM on NETACAD to practice your own commands. But in order to collaborate with your group or to save your work for later we're going to ask you to create an account on [REPL.it](https://repl.it) a free collaborative cloud based editor that lets you write in a number of different languages. One of the languages they support is BASH meaning your group can [start a new project](https://repl.it/languages/bash) and add eachother as collaborators to have one space to [work collaboratively](https://repl.it/site/multiplayer) and test your programs as well! Thank you Cloud Computing!

 Your group should start by breaking down the responsibilities of the work so that each person can be involved in writing at least one script, and that everyone is able to read and present the final scripts you build. You can very well write all 5 scripts together so everyone learns, but pair-program and switch who is mainly responsible for writing the script so everyone gets practice. Also doing code reviews is an important aspect of work life so get in the habit of keeping comments in your code and being able to talk someone through what's happening at each stage.

## Lab Assignment

### Script 1: STDIN & STDOUT
Write a script that reads user submitted input from the command line and prints the value back out for the user. 
Ex: Reading a user's name and printing a nice message back with it! 

### Script 2: Variables / CONDITIONALS
Write a script that utilizes an if/else statement to compare some values and perform an action based on *variables* inputted by the user. 
EX: Asking a yes/no question, taking a user's response as input, and performing a command based on their answer.

### Script 3: LOOPS
Write a script that uses a basic *for-loop* or a *while-loop* to run commands in a loop.
EX: Asking the user for their favorite number, and using it as a variable in a loop that prints a character like `*` that many times. 

### Script 4: FUNCTIONS / COMMAND ARGUMENTS
Write a script that defines and uses a function with arguments from the command line. 
EX: A script that takes two arguments and performs a mathematical function like add/multiply.

### Script 5: READING FROM FILE / REDIRECTION
Write a script that reads from a file and redirects the output to a different file.
EX: Read in a list of names & output those starting with a certain letter to a new file.  

### Group Challenge 1 - Create a Command Line Text Adventure Game
If you're looking for a challenge as a group, think of a fun way to combine all of the above concepts into an interactive experience for the user on the command line. For instance in a REPL.it(https://repl.it/languages/bash) BASH instance, run the following command `git clone https://gitlab.com/slackermedia/bashcrawl.git` to download a copy of an interactive command line game called Bashcrawl which teaches folks about Linux. The game uses shell scripts to teach users about Linux commands. You don't need to play the entire game or recreate the educational aspect of what it's doing but can use it as an example of a command line text adventure game that uses multiple Linux concepts to create an interactive experience for users. What can you all build when you put your minds together?

### Group Challenge 2 - Write a Shell Script that customizes an HTML and CSS file
Another great challenge as a group would be to think of a way to use Linux to create an HTML (index.html) and CSS (index.css) file with either inputs from the user on the command line, or by reading in a `config.txt` file using Linux. HTML and CSS files have very specific structures that you can build cleverly using a few Linux commands. Take a look at an example on how the HTML/CSS files should look and connect [here](https://www.quackit.com/css/external_style_sheets.cfm). You can use Linux to customize a few HTML elements in the HTML body if you want to get fancy. Once the files are created you can also test how they look on REPL by [opening an HTML/CSS instance](https://repl.it/languages/html) and pasting your work there to see it live. 

## Cheat Sheet
Here is a [cheat sheet](https://devhints.io/bash) to help you get started writing your commands! 

## Submission
Please share a copy of your group's REPL link to us via the Lab submission form shared in Slack when you've finished.

## Resources
* [Shell Script Beginner's Guide](https://medium.com/tech-tajawal/writing-shell-scripts-the-beginners-guide-4778e2c4f609)
* [Learn Bash in Y Minutes](https://learnxinyminutes.com/docs/bash/)
* [Writing Shell Scripts](http://linuxcommand.org/lc3_writing_shell_scripts.php)
* [Advanced BASH Scripting Guide](https://tldp.org/LDP/abs/html/)
* [UX Tips for Shell Scripts](https://codeburst.io/13-tips-tricks-for-writing-shell-scripts-with-awesome-ux-19a525ae05ae)
