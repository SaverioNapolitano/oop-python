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
They will be called from built-in external functions.

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


## Returning multiple values

This feature is not available in Java, but only in Python.

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

## Iterables

Like Java, Python data structures are based on the concept of iterable.

Iterator protocol in Python is the equivalent of iterable interface in Java.

iter() method called on an iterator returns the iterator itself.

*Every iterator is an iterable, but not every iterable is an iterator.*

Iterator: object that implements __ iter() __ and __ next() __ methods.

Iterable: object that can produce an iterator.

If I try to call the next() method on iterable, I get a TypeError.

Like Java, Python allows the conversion between data structures (for instance, construct a list from a string).

## List

Python list is the equivalent of Java ArrayList.

Unlike Java, Python lists can contain items of different types. 

Lists support slicing, which allows us to have a partial copy of the list.

The cross-way to remove items from iterables is using the del keyword.

We can also use the remove method (if we want to search the item based on its content) or the pop method
(if we want to search the item based on its index).

## Tuple

Tuples are implemented using C structures (fields are unchangeable).

Tuples distinctive element is ',' (parentheses are used to make the code more readable).

## Set

Python set is the equivalent of Java HashSet.

Operator in applied to sets is extremely fast (especially if compared to lists).

Python update() is the equivalent of Java addAll().

The difference between discard() and remove() methods in Python is also present in Java.

Like Java, one of the main uses of sets in Python is to remove duplicates from lists.

Python module timeit is the equivalent of Java time.

## Dictionary 

Python dictionary is the equivalent of Java hashmap (couples key-value).

The keys() method returns a set (no duplicates), while the values() method returns a list (allows duplicates).

The items() method returns a list of tuples.

Unpacking:
for can cycle on more than one variable at the same time
if at the right of in there is an object which is a container for other objects.

## Generators

Generators occupy much less memory compared to iterators,
due to the fact that generators do not store in memory the values
but know how to generate the next item when it is requested.

For this reason, if you try to print the content of a generator using the generator itself, it won't work
(you need to store its data in some data structure, for instance, a list).

## Generator Comprehension 

```(<expression> for <var> in <iterable> [if <condition>])```

1. ```for <var> in <iterables>``` generates the initial values
2. ```[if <condition>]``` optionally filters the values produced by for loop
3. ```<expression>``` is applied the values produced by for loop and eventually filtered

## Itertools

enumerate() provides new iterable composed of tuples: each tuple is always composed of two elements,
the second one is always the original object of the iterable that was enumerated,
the first one is the index the element had in the original iterable.

zip() allows the programmer to pack different iterables collections into a single one, whose items are tuples.

## Deep copy

Tuples are shared also in deep copies because they are immutable
(they can be reassigned, but in that case, they are automatically duplicated).

What above applies to every immutable part of data structures.

# Python Object-Oriented 

Object-oriented programming is independent of the language,
so all the main concepts seen in Java (encapsulation, inheritance, polymorphism) apply to Python too. 

## Object identity, type, internal state

Python id() has the same effect of printing an object in Java which has not overridden toString() method.

Internal state is the state of the variables (what each object contains).

## Class definition

Python self is the equivalent of Java this.

While in Java this is available through all the class'
body (you can write it everywhere with it),
in Python self is not available but needs to be passed to every method of the class (and has to be the first parameter).

Constructor (__ init __) has to be the first method of the class.

Python does not have the new operator when creating an object instance nor requires to specify the type of the variable.

Self is not required when instantiating an object
(it is automatically passed to the class' methods by Python Virtual Machine).

## Class attributes 

They are defined at the beginning of the class definition and are not preceded by the 'self' keyword. 

Like Java, they are shared among all the instances 

## Class methods

Methods annotated with @classmethod are used to create factories:
static methods which can create new objects (alternatives to constructor).

## String representations

Python __ repr() __ and __ str() __ are the equivalent of Java toString().

Internally, print() calls __ str() __ and repr() calls __ repr() __.

It's not recommended to differentiate __ repr() __ and __ str() __ unless you know exactly what you are doing.

Usually __ str() __ is a 'pretty printing' function.

Every Python object can access to private attribute __ dict __ which represents the internal state of the object.

It is recommended to always implement __ rep() __.

## Docstring 

Python Docstring is the equivalent of Java Javadoc.

It can be retrieved both from objects (class' instances) and class itself.

Unlike Java, Python does not have publicity indicators: everything is public. 

Private attributes can just be denoted using a convention

## Encapsulation 

Due to the fact that using getter and setter is discouraged in Python, you should use properties.

The idea is to have attributes initialized in a standard way within the constructor (without using the _ notation),
and pair with them annotated methods.

Annotated methods have the same name as the attribute they are paired with:
* the method annotated with @property acts as a getter,
takes just self as parameter and returns the internal attribute self._attributename. 
* the method annotated with @attributename.setter acts as a setter, takes self and value as parameters and changes 
the internal attribute self._attributename. 
* the method annotated with @attributename.deleter acts as a deleter, takes just self as parameter and deletes 
the internal attribute self._attributename.

Every time you try to access an attribute,
Python Virtual Machine does not modify immediately the attribute but calls annotated methods. 

## Inheritance 

The principles are the same as Java's.

In the definition of the derived class after the name, 
you have to put parentheses which will contain the name of the base class.

## Multilevel Inheritance 

Like Java, Python allows multilevel inheritance.

## Multiple Inheritance

Like C++ and unlike Java,
Python allows multiple inheritance (in Java you have to use interfaces to achieve the same goal).

## Method Resolution Order

Like Java, every class in Python derives from object.

## Polymorphism

In Java, it comes from methods'
overloading (methods with the same name and different parameters,
discarded in Python in favour of default values for functions' parameters) and methods'
overriding (redefine the method within a derived class)

## Informal Interfaces

Unlike Java, interfaces and abstract classes are not natively supported in Python.

It can be achieved through an accurate study of Python module [collections.abc](https://docs.python.org/3.9/library/collections.abc.html?highlight=collections.abc#module-collections.abc).

Informal interfaces declare methods without defining them (through the pass keyword). 

Python does not check whether the inherited methods are implemented or not. 

## Sorting user-defined objects

## The operator module

operator.attrgetter() (recommended) is faster than a lambda function and allows multilevel sorting.

You need to pass to the attrgetter() the strings representing the attributes you want to use for sorting the collection
(if an attribute is not found, an exception is raised).

## Modules and classes 

While in Java each file could have just one public class which must have the same name of the file,
in a Python module you can store whatever you want without constraints.

Classes' naming convention is the same as Java, while modules' naming convention is more similar to C.









































































