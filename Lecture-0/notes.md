# Week 0: 
### terminal commands 
*create a python file named file_name.py*   
  ```code file_name.py ```

*Run a python file named file_name.py*
```python file_name.py```

*list all files in current folder*  
  ```ls ```

*copy file*  
  ```cp```

*move file*  
  ```mv```

*remove file*  
  ```rm```

*make a directory*  
  ```mkdir```

*change directory*  
  ```cd```

*remove a directory*  
  ```rmdir```

*clear the terminal*  
  ```clear```

### Functions
can be thought of as verbs or actions that the computer language already knows how to perform.

can take multiple arguments. should be seperated by ```,```

functions can have default arguments. 
ie. ```print("hello,", end="\n")```
end has a default value of "\n" which creates a new line. You can alter it by providing a different value.
ie.```print("hello,", end="")```

functions can run on other functions. the inner function is run first, and then the outer one. in following example ``input`` is run first then ``in``.
eg. ``x = int(input("What's x? "))``
 
### Variables
a container for a value within the program
introduced by assigning a value
```example_variable = 1```

###  Comments
Identified by a # 
eg. ```# this is a comment```

Can be used to "pseudocode", or create a to-do list within the code.

### Data Types
**Strings**
- a sequence of text.
- to format strings you can use ```f``` in ```print(f"hello, {name}")```
- don't expect users to have common sense. So make sure you check, or correct user input.
- ```.strip``` removes all whitespace to left and right of users input. eg. ```name.strip()```
- ```.title```will title case the user's name. 
- you can add as many of these methods as you want. eg. ```name = input("What's your name? ").strip().title()```

**Integers**
- represented by ```int```
- can take math operators 
- string can be converted to integer. eg. ```x = int(input("What's x? "))```

**Floating Numbers** 
- a real number with a decimal. 
- you can change a value to float.    
	eg. ``x = float(input("What's x? "))``
- can be rounded to the nearest integer. 
	eg. ``x = float(input("What's x? "))``
	      ``x = round(x)``
- available arguments are ``round(number[n, ndigits])``
- can specify how many decimals to round to. 
	eg. ``x = round(a / b, 2)``
	or   ``print(f"{x:.2f}")``

Can add commas to larger numbers. 
``print(f"{num:,}")``

### Creating Your Own Functions
new functions can be defined with ``def`` 
eg. 
```
def hello():
	print("hello")

hello()
```	 

can tell the interpreter that your function takes a single parameter. eg. function ``hello`` takes parameter ``(to)`` 	
eg. ``def hello(to)``
     
### Returning Values
This allows you to return a value back to another part of the program. 

eg. the function square returns the result of squaring n back to the  function main.
```
def main():
	x = int(input(""What's x? "))
	print("x squared is", square(x))

def square(n)
	return n * n
main()
 ```


