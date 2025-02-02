# Module 1: Introduction to Programming Concepts
## 1.1 Computers and Programs (general)
- Python focuses on learning the problem-solving strategies and techniques that a computer scientist uses

## 1.2 Programming (general)
### Computer program basics
Computer programs are abundant in many people's lives today, carrying out applications on smartphones, tablets, and laptops, powering businesses like Amazon and Netflix, helping cars drive and planes fly, and much more.<br/>
A computer program consists of instructions executing one at a time. Basic instruction types are:
- **Input**: A program gets data, perhaps from a file, keyboard, touchscreen, network, etc.
- **Process**: A program performs computations on that data, such as adding two values like x + y.
- **Output**: A program puts that data somewhere, such as to a file, screen, or network.
Programs use variables to refer to data, like x, y, and z below. The name is due to a variable's value "varying" as a program assigns a variable like x with new values.

### Computational Thinking
Mathematical thinking became increasingly important throughout the industrial age, enabling people to successfully live and work. In the information age, many people believe computational thinking, or creating a sequence of instructions to solve a problem, will become increasingly important for work and everyday life. A sequence of instructions that solves a problem is called an algorithm.

## 1.3 Language History
### Scripting languages and Python
As computing evolved throughout the 1960s and 1970s, programmers began creating scripting languages to execute programs without the need for compilation. A script is a program whose instructions are executed by another program called an interpreter. Interpreted execution is slower due to requiring multiple interpreter instructions to execute one script instruction, but has advantages including avoiding the compilation step during programming, and being able to run the same script on different processors as long as each processor has an interpreter installed.<br/>
In the late 1980s, Guido van Rossum began creating a scripting language called Python and an accompanying interpreter. He derived Python from an existing language called ABC. The name Python came from Guido being a fan of the TV show Monty Python. The goals for the language included simplicity and readability, while providing as much power and flexibility as other scripting languages like Perl.

## 1.4 Programming Using Python
### Python interpreter
The Python interpreter is a computer program that executes code written in the Python programming language. An interactive interpreter is a program that allows the user to execute one line of code at a time.<br/>

Code is a common word for the textual representation of a program (and hence programming is also called coding). A line is a row of text.<br/>

The interactive interpreter displays a prompt (">>>") that indicates the interpreter is ready to accept code. The user types a line of Python code and presses the enter key to instruct the interpreter to execute the code. Initially you may think of the interactive interpreter as a powerful calculator. The example program below calculates a salary based on a given hourly wage, the number of hours worked per week, and the number of weeks per year. The specifics of the code are described elsewhere in the chapter.

### Executing a Python Program
The Python interactive interpreter is useful for simple operations or programs consisting of only a few lines. However, entering code line-by-line into the interpreter quickly becomes unwieldy for any program spanning more than a few lines.<br/>
Instead, a programmer can write Python code in a file, and then provide that file to the interpreter. The interpreter begins by executing the first line of code at the top of the file, and continues until the end is reached.<br/>
- A statement is a program instruction. A program mostly consists of a series of statements, and each statement usually appears on its own line.
- Expressions are code that return a value when evaluated; for example, the code wage * hours * weeks is an expression that computes a number. The symbol * is used for multiplication. The names wage, hours, weeks, and salary are variables, which are named references to values stored by the interpreter.
- A new variable is created by performing an assignment using the = symbol, such as salary = wage * hours * weeks, which creates a new variable called salary.
- The print() function displays variables or expression values.
- '#' characters denote comments, which are optional but can be used to explain portions of code to a human reader.
- Many code editors color certain words, as in the below program, to assist a human reader in understanding various words' roles.

### Quiz
1. What is the purpose of variables? (stores values for later use)
2. The code 20 * 40 is an expression? (True)
3. How are most Python programs developed? (Writing code in files)
4. Comments are required in a program? (False)
