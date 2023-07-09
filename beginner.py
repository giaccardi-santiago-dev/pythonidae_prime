print()
print('~ Executing \"beginner.py\" file ~')
print('Welcome to the Pythonidae Prime Course. Remember you can stop it by pressing CTRL + C')
print()
print('#')
print()

"""

Tutorial section

The usage of the triple quotation marks (\""" \""") -also known as DOCSTRING- is for the 
purpose of making this file as interactive as possible, giving the reader the power to choose which
part of the code to be executed, without over encumbering the terminal. The docstring usage will be
given more detail once the special string literal category is reached far below.

To use the striple quotation marks (\""" \""") properly these steps should be followed:
1- Identify the given example you want to run inside this file 
2- Add three " over the first comment below the example that says "# ~ Example finish"
3- Add three " below the first comment over the example that says "# ~ Example start"
4- Run the file and manipulate it as you see fit
5- Remove the " you added by the step 2 and step 3 of this guide
6- Go back to step 1

The usage of the special character "#" -also known as COMMENT- is to tell interpreter to ignore the
rest of the line when the
program is run. It is used to provide information or explanations about the code for the readers.
The usage of the extension "better comments" is advised, as it improves readability.

The examples demand input of the reader and offers output for each example in order to give more
interaction to the user with the learning process. The file asks for input by the implement of the
function "input()" and offers output by the implementation of the function "print()", which will be
covered in detail once the usage of functions has been reached.

The steps to get the most out of this file is:
1- Read the documentation about the desired subject, e.g: Variables.
2- Choose the desired example to be tested, e.g: String data type.
3- Experiment with the code, making changes and learning it's behavior by running the script
4- Implement the knowledge into your own personal projects to solidify the learning process
5- Advance logically to the next subject, e.g: Boolean data type.

# TODO Beginner section

# / Subject: Variables
# / Explanation: Tools for storing data inside memory for later usage. 

# ? Types: Variables can store four (4) data types: integers, floats, strings, and booleans.
# ? Tip: There are no native constants in python, by convention, when assigning a constant, it should
# ? be entirely capitalized.

# * General capabilities: data storage, data types, data structures, scope, assignment
# * General limitations: naming conventions, case sensitivity, memory limitations, type errors, scope
# * confusion.

# = Types list

# = Variable usage with integer data type
# + Capabilities: basic arithmetic operations, comparison operations and bitwise operations
# - Limitations: overflow and underflow, division behavior, and memory usage
\"""
print(' ~ Start of the example of variable usage with integer data type ~ ')
integer_variable = int(input('Variable \"integer_variable" was just created. Please, assign a value to it: ')) 
# Remember, it can be almost any integer number from -♾️ to ♾️ 
print ('Thanks, now the value of the variable \"integer_variable\" is:',integer_variable)
print(' ~ Finish of the example of variable usage with integer data type  ~ ')
print()
\"""
# = Variable usage with 'float' data type
# + Capabilities: basic arithmetic operations, comparison operations, floating-point precision and scientific computing libraries.
# - Limitations: extreme case precision errors, limited range, speed
\"""
print('~ Start of the example of variable usage with float data type ~')
float_variable = float(input('Variable \"float_variable\" was just created. Please, assign a value to it: ')) 
#It can be almost any floating point number from -♾️ to ♾️ 
print ('Thanks, now the value of the variable \"float_variable\" is:',float_variable)
print('~ Finish of the example of variable usage with float data type ~')
print()
\"""
# Variable usage with 'string' data type
# -Capabilities: basic string operations, string formatting, string manipulation, unicode support
# -Limitations: immutability, memory usage and encoding issues
\"""
print('~ Start of the example of variable usage with string data type ~')
string_variable = input('Variable \"string_variable\" was created. Please, assign a value to it: ') 
# It can include almost any ammount of letters, digits, and symbols.
print ('Thanks, now the value of the variable \"string_variable\" is:',string_variable)
print('~ Finish of the example of variable usage with string data type  ~')
print()
\"""
# Variable example with usage of 'boolean' data type
# -Capabilities: logical operations, comparison operations, control flow, boolean conversion and logical shortcuts
# -Limitations: limited values, limited arithmetic operations, potential confusion with different data types
\"""
print('~ Start of the example of variable usage with boolean data type ~')
boolean_variable = True
print('Variable \"boolean_variable\" was just created. To modify it\'s value with user input more advanced knowledge is required')
print('The value of the \"boolean_variable\" variable is:',boolean_variable)
print('~ Finish of the example of variable usage with boolena data type  ~')
print()
\"""
# / Subject: Objects
# / Explanation: Tools for storing data inside memory for later usage. 

# ? Types: Variables can store four (4) data types: integers, floats, strings, and booleans.
# ? Tip: There are no native constants in python, by convention, when assigning a constant, it should
# ? be entirely capitalized.

# * General capabilities: data storage, data types, data structures, scope, assignment
# * General limitations: naming conventions, case sensitivity, memory limitations, type errors, scope
# * confusion.

# Variable example with usage of 'boolean' data type
# -Capabilities: logical operations, comparison operations, control flow, boolean conversion and logical shortcuts
# -Limitations: limited values, limited arithmetic operations, potential confusion with different data types
\"""
print('~ Start of the example of variable usage with boolean data type ~')
boolean_variable = True
print('Variable \"boolean_variable\" was just created. To modify it\'s value with user input more advanced knowledge is required')
print('The value of the \"boolean_variable\" variable is:',boolean_variable)
print('~ Finish of the example of variable usage with boolena data type  ~')
print()
\"""
#! REMEMBER TO TAKE 10 MINUTES BREAKES EVERY 50 MINUTES OF READING

# Operators: Tools to implement interaction between data strutures, flow control and more

# Arithmetic Operators:
# Types:

# General capabilities:
# General limitations

# Addition operator usage (+): Adds two values together.
# + Capabilities:
# -Limitations:
\"""
print('~ Start of the example of addition operator usage ~')
print('The next arithmetic operation will be performed after values are assigned:')
print('AdditionExample = AdditionExample_value_1 + AdditionExample_value_2')
AdditionExample = float(0)
AdditionExample_value_1 = float(input('Assign a value to the \"AdditionExample_value_1\" variable: '))
AdditionExample_value_2 = float(input('Assign another value to the \"AdditionExample_value_2\" variable: '))
AdditionExample = AdditionExample_value_1 + AdditionExample_value_2
print('The value of the \"AdditionExample\" variable was set to: ',AdditionExample)
print(AdditionExample,'=',AdditionExample_value_1,'+',AdditionExample_value_2)
print('~ Finish of the example of addition operator usage  ~')
print()
\"""
#Substraction operator usage (-): Substracts the second value from the first.
\"""
print('~ Start of the example of substraction operator usage ~')
print('The next arithmetic operation will be performed after required values are assigned:')
print('SubstractionExample = SubstractionExample_value_1 + SubstractionExample_value_2')
SubstractionExample = float(0)
SubstractionExample_value_1 = float(input('Assign a value to the \"SubstractionExample_value_1\" variable: '))
SubstractionExample_value_2 = float(input('Assign another value to the \"SubstractionExample_value_2\" variable: '))
SubstractionExample = SubstractionExample_value_1 - SubstractionExample_value_2
print(SubstractionExample,'=',SubstractionExample_value_1,'-',SubstractionExample_value_2)
print('The value of the \"SubstractionExample\" variable was set to:',SubstractionExample)
print('~ Finish of the example of substraction operator usage  ~')
print()
\"""
#Multiplication (*): Multiplies two values together.
\"""
print('~ Start of the example of multiplication operator usage ~')
print('The next arithmetic operation will be performed after required values are assigned:')
print('MultiplicationExample = MultiplicationExample_value_1 * MultiplicationExample_value_2')
MultiplicationExample = float(0)
MultiplicationExample_value_1 = float(input('Assign a value to the \"MultiplicationExample_value_1\" variable: '))
MultiplicationExample_value_2 = float(input('Assign another value to the \"MultiplicationExample_value_2\" variable: '))
MultiplicationExample = MultiplicationExample_value_1 * MultiplicationExample_value_2
print(MultiplicationExample,'=',MultiplicationExample_value_1,'*',MultiplicationExample_value_2)
print('The value of the \"MultiplicationExample\" variable was set to:',MultiplicationExample)
print('~ Finish of the example of multiplication operator usage  ~')
print()
\"""
#Division (/): Divides the first value by the second.
\"""
print('~ Start of the example of division operator usage ~')
print('The next arithmetic operation will be performed after required values are assigned:')
print('DivisionExample = DivisionExample_value_1 / DivisionExample_value_2')
DivisionExample = float(0)
DivisionExample_value_1 = float(input('Assign a value to the \"DivisionExample_value_1\" variable: '))
DivisionExample_value_2 = float(input('Assign another value to the \"DivisionExample_value_2\" variable: '))
DivisionExample = DivisionExample_value_1 / DivisionExample_value_2
print(DivisionExample,'=',DivisionExample_value_1,'/',DivisionExample_value_2)
print('The value of the \"DivisionExample\" variable was set to:',DivisionExample)
print('~ Finish of the example of division operator usage  ~')
print()
\"""
#Modulus (%): Returns the remainder of the division of the first value by the second.
\"""
print('~ Start of the example of modulus operator usage ~')
print('The next arithmetic operation will be performed after required values are assigned')
print('ModulusExample = ModulusExample_value_1 % ModulusExample_value_2')
ModulusExample = float(0)
ModulusExample_value_1 = float(input('Assign a value to the \"ModulusExample_value_1\" variable: '))
ModulusExample_value_2 = float(input('Assign another value to the \"ModulusExample_value_2\" variable: '))
ModulusExample = ModulusExample_value_1 % ModulusExample_value_2
print('The remainder of',ModulusExample_value_1,'divided by',ModulusExample_value_2,'is:',ModulusExample)
print('The value of the \"ModulusExample\" variable was set to:',ModulusExample)
print('~ Finish of the example of modulus operator usage ~')
print()
\"""
#Exponentiation (**): Raises the first value to the power of the second.
\"""
print('~ Start of example: exponentiation operator usage ~')
print('The next arithmetic operation will be performed after required values are assigned')
print('ExponentiationExample = ExponentiationExample_value_1 ** ExponentiationExample_value_2')
ExponentiationExample = float(0)
ExponentiationExample_value_1 = float(input('Assign a value to the \"ExponentiationExample_value_1\" variable: '))
ExponentiationExample_value_2 = float(input('Assign another value to the \"ExponentiationExample_value_2\" variable: '))
ExponentiationExample = ExponentiationExample_value_1 ** ExponentiationExample_value_2
print(ExponentiationExample_value_1,'rised to the power of',ExponentiationExample_value_2,'is:',ExponentiationExample)
print('The value of the \"ExponentiationExample\" variable was set to:',ExponentiationExample)
print('~ Finish of example: exponentiation operator usage ~')
print()
\"""
#! REMEMBER TO TAKE 10 MINUTES BREAKES EVERY 50 MINUTES OF READING. WALKING OUTSIDE AND DRINKING WATER IS ADVISED.

Comparison Operators:

# Equal to (==): Returns True if the first value is equal to the second.
\"""
print('~ Start of example: "Equal to" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(EqualToExample_value_1 == EqualToExample_value_2) > EqualToExample')
EqualToExample = bool(None)
EqualToExample_value_1 = float(input('Variable \"EqualToExample_value_1\" was just created. Please, assign a value to it: '))
EqualToExample_value_2 = float(input('Variable \"EqualToExample_value_2\" was just created. Please, assign a value to it: '))
if EqualToExample_value_1 == EqualToExample_value_2:
    EqualTo_example = True
else
    EqualTo_example = False
print('The variable "EqualToExample_value_1" value is:',EqualToExample_value_1,', and the variable "EqualToExample_value_1" value is:',EqualToExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "EqualToExample" variable:', EqualToExample)
print('~ Finish of example: "Equal to" comparison operator usage ~')
print()
\"""
#Not equal to (!=): Returns True if the first value is not equal to the second.
\"""
print('~ Start of example: "Not equal to" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(NotEqualToExample_value_1 != NotEqualToExample_value_2) > NotEqualToExample')
NotEqualToExample = bool(None)
NotEqualToExample_value_1 = float(input('Variable \"NotEqualToExample_value_1\" was just created. Please, assign a value to it: '))
NotEqualToExample_value_2 = float(input('Variable \"NotEqualToExample_value_2\" was just created. Please, assign a value to it: '))
if EqualToExample_value_1 != EqualToExample_value_2:
    EqualTo_example = True
else:
    EqualTo_example = False
print('The variable "NotEqualToExample_value_1" value is:',NotEqualToExample_value_1,', and the variable "NotEqualToExample_value_1" value is:',NotEqualToExample_value_2)
print('So the result of the "Not equal to" comparison between those two variables ends up assigning the next value to the "NotEqualToExample" variable:',NotEqualToExample)
print('~ Finish of example: "Not Equal to" comparison operator usage ~')
print()
\"""
# Greater than (>): Returns True if the first value is greater than the second.
\"""
print('~ Start of example: "Greater than" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(GreaterThanExample_value_1 > GreaterThanExample_value_2) > GreaterThanExample')
GreaterThanExample = bool(None)
GreaterThanExample_value_1 = float(input('Variable \"GreaterThanExample_value_1\" was just created. Please, assign a value to it: '))
GreaterThanExample_value_2 = float(input('Variable \"GreaterThanExample_value_2\" was just created. Please, assign a value to it: '))
if GreaterThanExample_value_1 > GreaterThanExample_value_2:
    GreaterThanExample = True
else:
    GreaterThanExample = False
print('The variable "GreaterThanExample_value_1" value is:',GreaterThanExample_value_1,', and the variable "GreaterThanExample_value_2" value is:',GreaterThanExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "GreaterThanExample" variable:', GreaterThanExample)
print('~ Finish of example: "Greater than" comparison operator usage ~')
print()
\"""
# Less than (<): Returns True if the first value is less than the second.
\"""
print('~ Start of example: "Less than" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(LessThanExample_value_1 < LessThanExample_value_2) = LessThanExample')
LessThanExample = bool(None)
LessThanExample_value_1 = float(input('Variable \"LessThanExample_value_1\" was just created. Please, assign a value to it: '))
LessThanExample_value_2 = float(input('Variable \"LessThanExample_value_2\" was just created. Please, assign a value to it: '))
if LessThanExample_value_1 == LessThanExample_value_2:
    LessThanExample = True
else:
    LessThanExample = False
print('The variable "LessThanExample_value_1" value is:',LessThanExample_value_1,', and the variable "LessThanExample_value_2" value is:',LessThanExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "LessThanExample" variable:', LessThanExample)
print('~ Finish of example: "Greater than" comparison operator usage ~')
print()
\"""
# Greater than or equal to (>=): Returns True if the first value is greater than or equal to the second.
\"""
print('~ Start of example: "Greater than or equal to" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(GreaterThanOrEqualToExample_value_1 == GreaterThanOrEqualToExample_value_2) > GreaterThanOrEqualToExample')
GreaterThanOrEqualToExample = bool(None)
GreaterThanOrEqualToExample_value_1 = float(input('Variable \"GreaterThanOrEqualToExample_value_1\" was just created. Please, assign a value to it: '))
GreaterThanOrEqualToExample_value_2 = float(input('Variable \"GreaterThanOrEqualToExample_value_2\" was just created. Please, assign a value to it: '))
if GreaterThanOrEqualToExample_value_1 == GreaterThanOrEqualToExample_value_2:
    GreaterThanOrEqualToExample = True
else:
    GreaterThanOrEqualToExample = False
print('The variable "GreaterThanOrEqualToExample_value_1" value is:',GreaterThanOrEqualToExample_value_1,', and the variable "GreaterThanOrEqualToExample_value_2" value is:',GreaterThanOrEqualToExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "GreaterThanOrEqualToExample" variable:', GreaterThanOrEqualToExample)
print('~ Finish of example: "Greater than or equal to" comparison operator usage ~')
print()
\"""
# Less than or equal to (<=): Returns True if the first value is less than or equal to the second.
\"""
print('~ Start of example: "Less than or equal to" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(LessThanOrEqualToExample_value_1 == LessThanOrEqualToExample_value_2) > GreaterThanExample')
LessThanOrEqualToExample = bool(None)
LessThanOrEqualToExample_value_1 = float(input('Variable \"LessThanOrEqualToExample_value_1\" was just created. Please, assign a value to it: '))
LessThanOrEqualToExample_value_2 = float(input('Variable \"LessThanOrEqualToExample_value_2\" was just created. Please, assign a value to it: '))
if LessThanOrEqualToExample_value_1 == LessThanOrEqualToExample_value_2:
    LessThanOrEqualToExample = True
else:
    LessThanOrEqualToExample = False
print('The variable "LessThanOrEqualToExample_value_1" value is:',LessThanOrEqualToExample_value_1,', and the variable "LessThanOrEqualToExample_value_2" value is:',LessThanOrEqualToExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "LessThanOrEqualToExample" variable:', LessThanOrEqualToExample)
print('~ Finish of example: "Less than or equal to" comparison operator usage ~')
print()
\"""
# Logical Operators:

# And (and): Returns True if both the first and second values are True.
\"""
print('~ Start of example: "And" logic operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(AndExample_value_1 == AndExample_value_2) > AndExample')
AndExample = bool(None)
AndExample_value_1 = True
AndExample_value_2 = False
if AndExample_value_1 and AndExample_value_2 then:
    AndExample = True
else:
    AndExample = False
print('The variable "AndExample_value_1" value is:',AndExample_value_1,', and the variable "AndExample_value_2" value is:',AndExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "AndExample" variable:', AndExample)
print('~ Finish of example: "And" comparison operator usage ~')
print()
\"""
# Or (or): Returns True if either the first or second value is True.
\"""
print('~ Start of example: "Or" logical operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(OrExample_value_1 == OrExample_value_2) > OrExample')
OrExample = bool(None)
OrExample_value_1 = float(input('Variable \"OrExample_value_1\" was just created. Please, assign a value to it: '))
OrExample_value_2 = float(input('Variable \"OrExample_value_2\" was just created. Please, assign a value to it: '))
if OrExample_value_1 == OrExample_value_2:
    OrExample = True
else:
    OrExample = False
print('The variable "OrExample_value_1" value is:',OrExample_value_1,', and the variable "OrExample_value_2" value is:',OrExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "OrExample" variable:', OrExample)
print('~ Finish of example: "Or" logic operator usage ~')
print()
\"""
# Not (not): Returns True if the first value is False.
\"""
print('~ Start of example: "Not" comparison operator usage ~')
print('The next logic operation will be performed after required values are assigned')
print('(NotExample_value_1 == NotExample_value_2) > NotExample')
NotExample = bool(None)
NotExample_value_1 = float(input('Variable \"NotExample_value_1\" was just created. Please, assign a value to it: '))
NotExample_value_2 = float(input('Variable \"NotExample_value_2\" was just created. Please, assign a value to it: '))
if NotExample_value_1 == NotExample_value_2:
    NotExample = True
else:
    NotExample = False
print('The variable "NotExample_value_1" value is:',NotExample_value_1,', and the variable "NotExample_value_2" value is:',NotExample_value_2)
print('So the result of the logical comparison between those two variables ends up assigning the next value to the "NotExample" variable:', NotExample)
print('~ Finish of example: "Notn" comparison operator usage ~')
print()
\"""
# Assignment Operators:

# Assign (=): Assigns the value on the right to the variable on the left.
\"""
print('~ Start of example: "=" assignment operator usage ~')
AssignExample = input('Variable \"AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"AssignExample\" is:',AssignExample)
print('~ Finish of the example of variable usage with integer data type  ~')
print()
\"""
# Add and assign (+=): Adds the value on the right to the variable on the left and assigns the result to the variable on the left.
\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""
# Subtract and assign (-=): Subtracts the value on the right from the variable on the left and assigns the result to the variable on the left.
\"""
print('~ Start of example: "Substract and assign" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "-=" assignment operator usage ~')
print()
\"""

# Multiply and assign (*=): Multiplies the variable on the left by the value on the right and assigns the result to the variable on the left.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

# Divide and assign (/=): Divides the variable on the left by the value on the right and assigns the result to the variable on the left.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

#Modulus and assign (%=): Calculates the remainder of dividing the variable on the left by the value on the right and assigns the result to the variable on the left.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

#Exponentiation and assign (**=): Raises the variable on the left to the power of the value on the right and assigns the result to the variable on the left.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

Bitwise Operators:

#Bitwise AND (&): Performs a bitwise AND operation between the binary representations of the two values.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

#Bitwise OR (|): Performs a bitwise OR operation between the binary representations of the two values.

\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""

#Bitwise XOR (^): Performs a bitwise XOR operation between the binary representations of the two values.
\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""
#Bitwise NOT (~): Performs a bitwise NOT operation on the binary representation of the value.
\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""
#Left shift (<<): Shifts the bits of the binary representation of the first value to the left by the number of positions specified by the second value.
\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""
#Right shift (>>): Shifts the bits of the binary representation of the first value to the right by the number of positions specified by the second value.
\"""
print('~ Start of example: "+=" assignment operator usage ~')
Add&AssignExample = input('Variable \"Add&AssignExample\" was just created. Please, assign a value to it: ')) 
print ('Thanks, now the value of the variable \"Add&AssignExample\" is:',Add&AssignExample)
print('~ Finish of the example: "+=" assignment operator usage ~')
print()
\"""
#! REMEMBER TO TAKE 10 MINUTES BREAKES EVERY 50 MINUTES OF READING. WALKING OUTSIDE AND DRINKING WATER IS ADVISED.

-ENTERING WORK IN PROGRESS AREA!!!-

# Control flow statements: Tools that allow you to control the flow of your program
# Types: There are fourteen (14) different statements: if, else, elif, while, for, break, continue, pass, try/except, raise, assert, with, try/finally, and async/await
# General capabilities: Conditional execution, repeated execution, exception handling, context managment
# General limitations: Readability, performance impact, and error-prone

# If statement
#-Capabilities: conditional logic, comparison operators, boolean logic, nested 'if' statements
#-Limitations: limited to boolean expressions, only one condition per statement, no automatic type conversion, code indentation

\"""
if integer_example > float_example:
print(integer_example, 'is greater than', float_example)
\"""

# Else statement
#-Capabilities: alternative logic, nested 'if-else' statements, multiple 'else' statements
#-Limitations: limited to boolean expressions, no condition evaluation, code indentation

\"""
if float_example > integer_example:
print(float_example, 'is greater than', integer_example)
else
print(float_example, 'is not greater than', integer_example)
\"""

# Elif (else if)

# While

# For

# Break

# Continue

# Pass

# Try/Except

# Raise

# Assert

# With

# Try/Finally

# Async/Await

#Functions: Reusable blocks of code that perform a specific task. They have four parts: definition, body, finisher, and calling.
Definition:
Body:
Finisher:
Calling:

# Types:
# General capabilities:
# General limitations:
There are built-in functions inside the python interpreter, which only need to be called to perform. 

Here is a comprehensive and detailed list of the most used ones

abs(): Returns the absolute value of a number
all(): Returns True if all elements in an iterable are true, otherwise False
any(): Returns True if any element in an iterable is true, otherwise False
bin(): Converts an integer to a binary string
bool(): Converts a value to a Boolean (True or False)
callable(): Returns True if an object is callable (can be called like a function), otherwise False
chr(): Returns a string representing a character whose Unicode code point is the specified integer
dict(): Creates a new dictionary object
enumerate(): Returns an iterator that generates tuples containing the index and values of an iterable
float(): Converts a string or number to a floating-point number
format(): Formats a value based on a specified format string
input(): Reads a line of text from standard input (keyboard)
int(): Converts a string or number to an integer
len(): Returns the number of items in an object (e.g. a list, tuple, or string)
list(): Creates a new list object
max(): Returns the largest item in an iterable or the largest of two or more arguments
min(): Returns the smallest item in an iterable or the smallest of two or more arguments
open(): Opens a file and returns a file object
ord(): Returns the Unicode code point of a character
pow(): Returns the value of a number raised to a specified power
print(): Prints a message to the console
range(): Returns an iterator that generates a sequence of numbers
round(): Rounds a floating-point number to the nearest integer
set(): Creates a new set object
sorted(): Returns a sorted list of the items in an iterable
str(): Converts a value to a string
sum(): Returns the sum of the items in an iterable
tuple(): Creates a new tuple object
type(): Returns the type of an object
zip(): Returns an iterator that aggregates elements from multiple iterables

Here is a list of the less common built-in functions

len(): Returns the length (number of items) of a sequence such as a string, list, or tuple.
max(): Returns the maximum value from a sequence or set of values.
min(): Returns the minimum value from a sequence or set of values.
sorted(): Returns a sorted list of the items in a sequence.
sum(): Returns the sum of the items in a sequence or set of values.
range(): Returns a sequence of numbers from a starting value to an ending value, with an optional step value.
enumerate(): Returns a sequence of (index, value) tuples for a given sequence, where index is the index of the value in the sequence.
zip(): Returns a sequence of tuples, where the i-th tuple contains the i-th element from each of the input sequences or iterables.

# Data structures

Lists: An ordered collection of elements, which can be of any data type.
Tuples: Similar to lists, but immutable (cannot be modified after creation).
Sets: An unordered collection of unique elements.
Dictionaries: A collection of key-value pairs, where each key is associated with a value.
Arrays: A collection of elements of the same data type, stored in contiguous memory locations.
Queues: A data structure that follows the First-In-First-Out (FIFO) principle.
Stacks: A data structure that follows the Last-In-First-Out (LIFO) principle.
Linked Lists: A data structure consisting of a sequence of nodes, where each node contains a value and a reference to the next node in the sequence.
Trees: A hierarchical data structure consisting of nodes, where each node has zero or more child nodes.
Graphs: A collection of nodes (vertices) connected by edges, where each edge represents a relationship between two vertices.

# Input and output



#modules and packages

os - provides a way to interact with the operating system
sys - provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter
math - provides a set of mathematical functions and constants
random - provides functions for generating random numbers
time - provides functions for working with time and dates
datetime - provides classes for working with dates and times
calendar - provides classes for working with calendars
argparse - provides a way to parse command-line arguments
json - provides methods for working with JSON data
csv - provides methods for working with CSV (Comma Separated Values) files
re - provides regular expression matching operations
itertools - provides functions for working with iterators and generators
collections - provides alternatives to built-in types, including named tuples, ordered dictionaries, and default dictionaries
urllib - provides methods for working with URLs
requests - provides methods for making HTTP requests
socket - provides methods for working with network sockets
multiprocessing - provides methods for working with multiple processes
threading - provides methods for working with multiple threads

#file handling

open() - opens a file and returns a file object
read() - reads the entire content of a file
readline() - reads a single line from a file
readlines() - reads all lines from a file and returns a list of strings
write() - writes a string to a file
writelines() - writes a list of strings to a file
close() - closes the file object
with statement - provides a way to open and close a file automatically

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) - opens a file and returns a file object. The mode parameter specifies the mode in which the file is opened (e.g., read, write, append). The other parameters are optional and provide additional options for opening the file.
read(size=-1) - reads the entire content of a file, or up to size bytes if specified.
readline(size=-1) - reads a single line from a file, or up to size bytes if specified.
readlines(hint=-1) - reads all lines from a file and returns a list of strings. The optional hint parameter specifies the maximum number of bytes to read.
write(string) - writes a string to a file.
writelines(list) - writes a list of strings to a file.
seek(offset[, whence]) - changes the current file position to the given offset, relative to the position specified by whence (e.g., the beginning, the end, or the current position).
tell() - returns the current file position.
truncate(size=None) - truncates the file to the specified size (in bytes). If size is not specified, it truncates the file to the current position.
flush() - flushes the write buffer of the file.
close() - closes the file object.
with statement - provides a way to open and close a file automatically.
os module - provides functions for working with files and directories, such as os.path.exists, os.path.isfile, os.path.isdir, os.path.basename, os.path.dirname, os.path.join, os.mkdir, os.rmdir, and os.remove.
shutil module - provides functions for working with files and directories, such as shutil.copy, shutil.move, shutil.rmtree, and shutil.make_archive.
pickle module - provides functions for serializing and deserializing Python objects to and from files.
csv module - provides functions for working with CSV files, such as csv.reader, csv.writer, and csv.DictReader.
json module - provides functions for working with JSON files, such as json.dump, json.dumps, json.load, and json.loads.

# Exception handling:

try - The try block lets you test a block of code for errors.
except - The except block lets you handle the error.
finally - The finally block lets you execute code, regardless of the result of the try- and except blocks.
else - The else block lets you specify code to run if no exceptions were raised in the try block.

exceptions

Exception - The base class for all exceptions.
AttributeError - Raised when an attribute reference or assignment fails.
IndexError - Raised when an index is out of range.
KeyError - Raised when a dictionary key is not found.
TypeError - Raised when an operation or function is applied to an object of inappropriate type.
ValueError - Raised when an operation or function receives an argument of the right type but an inappropriate value.
IOError - Raised when an I/O operation (such as a file read or write) fails.
NameError - Raised when a local or global name is not found.
ZeroDivisionError - Raised when the second operand of a division or modulo operation is zero.

Objects and classes

Parts of an object
Parts of a class

libraries

In Python, a module is a file containing Python definitions and statements that can be imported and
 used in other Python code. A module typically contains related functions, classes, or variables, 
 and it helps to organize code and make it more reusable.

A package is simply a directory containing a collection of related Python modules. The purpose of a
 package is to provide a hierarchical organization of related modules, so that they can be easily 
 managed and imported as a single unit.

A library in Python is a collection of related packages and modules that provide functionality for 
a specific purpose. A library typically contains a set of related functionalities that can be 
reused in many different projects.

To summarize, a module is a single Python file, a package is a directory of related modules, and a 
library is a collection of related packages and modules.

os - Provides a way of interacting with the file system.
sys - Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
math - Provides a range of mathematical functions.
random - Provides functions for generating random numbers.
datetime - Provides classes for working with dates and times.
calendar - Provides functions for working with calendars.
time - Provides functions for working with time.
re - Provides regular expression matching operations.
json - Provides functions for working with JSON data.
csv - Provides functions for working with CSV files.
pickle - Provides functions for serializing and deserializing Python objects.
sqlite3 - Provides a way of interacting with SQLite databases.
requests - Provides a way of making HTTP requests.
beautifulsoup4 - Provides a way of parsing HTML and XML documents.
numpy - Provides support for large, multi-dimensional arrays and matrices, as well as a large collection of high-level mathematical functions to operate on these arrays.
pandas - Provides support for data manipulation and analysis.
matplotlib - Provides a way of creating data visualizations.
scikit-learn - Provides machine learning algorithms and tools.
tensorflow - Provides a way of building and training neural networks.

"""
print ('#')
print ()
print ('Finished executing \"beginner.py\"')
print ()
