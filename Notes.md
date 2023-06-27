# Python Basics

## Advantages and disadvantages
Advantages
* Portable (being interpreted it works on every machine)

Disadvantages 
* Slow Speed (even when confronted with other interpreted languages such as Java)
* Not memory efficient (it occupies more memory than it needs)

## Using Python 

IPython Shell allows you to use system commands (with Python Shell it's not possible). 

Python scripts can be easily integrated within a Unix environment (once you have written your code and saved the file with ".py" extension, you can run int from command line using a Python interpreter or make it executable with chmod and then use "./" command)

pip in Python is the equivalent of apt-get in Linux.

## Main function 

def is the keyword to define the beginning of a function.

In general, python scripts are executed from the first to the last line. 

## Naming rules

Python & C: lowercase names and underscores
Java: camelcase

Names with __ in Python stand for private methods that shouldn't be modified (it's a convention).

## Variable assignments 

```Python 
#multiple variables, multiple values -> unpacking, useful in loop
a, b, c = 5, 3.2, 'Hello'
#multiple variables, one value -> valid syntax in C too
x = y = z = 'same value'
```

Python doesn't have primitive types, while Java does.

In Python references (variables) are not typed (unlike Java), while objects variables refer to are.

To access attributes and methods of an object, Python (like Java) uses the dot "." notation.

## Literals 

Python types are called literals.

### String Literals

Like Java, strings in Python are represented by Unicode characters (16 bits), while C uses single 8 bits.

## Implicit Casting 

Python equivalent of Java instanceof is isinstance. 

Both Java and Python (and many other languages) have implicit casting.

## Strings 

### len()

While in Java the length of an object is returned by a method of that object, Python as a general built-in function that, given a sequence as input, returns its length (internally it calls a method of the sequence passed as input).



**Python list is the equivalent of Java ArrayList.**

### Accessing characters

Indexing is the same as Java and C.

Slicing excludes the second element of the instruction.

### Changing Strings 

Java: assign to an existing reference null.

Python: del keyword.

## Combining Strings

Both Java and Python use the '+' operator for concatenating strings (both cases are strongly inefficient because each time '+' is used a new string is generated instead of modifying the existent one).

In case non-string objects are passed as parameters, Java converts them to string automatically, while Python requires that every object is a string (otherwise an error is thrown).

Python '{} {}'.format is the equivalent of C and Java printf (format is a strings' method) -> recommended.

## if..elif..else

In Java, it is else-if explicitly while Python adds a new keyword elif.

## Comparison Operators

In Java '==' operator works on references, in Python it works on contents.

Usually, in Java to verify membership of elements to a sequence are used methods that are called "contains" while in Python there is the operator in.

## Loops

Python for is similar to Java for each.

Python while is similar to Java and C while.

Python keyword pass has no equivalent in Java and C.

## Functions 

In Python does not exist return type (due to its being dynamically typed). 

Passing parameters in Python is similar to Java.

## Default arguments

They're not present in Java (to obtain the same effect you have to overload methods -> methods with the same name but different parameters).




**Python dictionary is the equivalent of Java hashmap. (couples key-value)**

## Returning multiple values

This feature is not available in Java, but only in Python.


**Python self is the equivalent of Java this.**

@dataclass allows you to obtain a minimal class to store and to retrieve values writing less than creating a normal class.

## Lambda functions

Example: pass to a sort function the criterion.

Java: implementation of Comparable interface

Python: call the sort function passing as parameter a lambda function which represents the criterion.

## Exceptions 

Like Java, Python exceptions are organized in a hierarchy. 

At the top of the hierarchy, there is Exception (same name as Java). 

Python try-except block is the equivalent of Java try-catch block.

To give the exception a name and use it within the code block, you have to use the keyword as.

Like Java, Python allows having more except blocks (from the most specific one to the most general one).

In Python does not exist the distinction between checked and unchecked exceptions (unlike Java), so all the exceptions have to be handled manually.

In Python, it is not necessary to add exception to method signature (unlike Java).

Like Java, in Python it is possible to generate exceptions (raise in Python is the equivalent of throw in Java).

Use custom exception is not recommended (as it was not in Java).

Unlike Java, Python allows the programmer to add an else block to execute code in case no exception has been found in the try block.

Like Java, Python allows the programmer to add a finally block (which has the same meaning of the Java one).

## Decorators

Like Java, there are decorators in Python too. 

They are annotations starting with @ that precede calls to methods or functions which are used to configure or modify their behaviour without needing to rewrite them (pie syntax, available both in Java and Python).

Unlike Java, Python allows the programmer to define functions within other functions. 

Decorators are wrappers that add custom code before or after the execution of the function.

## File I/O

In Python, managing file and I/O is easier than Java.

# Python Data Structures






















