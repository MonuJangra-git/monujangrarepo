'''Python is dynamically typed,
 meaning you don’t have to declare variable types explicitly.
   But since Python 3.5+, we can use type hints (annotations) to make 
   code more readable, maintainable, and compatible with 
   tools like mypy or IDEs.
Key Takeaways
Type hints don’t enforce types at runtime (Python still runs dynamically).

They’re mainly for readability, debugging, and static analysis.

Use typing module for complex definitions.

Use aliases and TypedDict for cleaner, structured code.
   '''

num = 66
#or 
num : str = 67
print(num)
num : int = 69
print(num)
num : float = 70
print(num)
#as we saw there is no effect of typing their type they are
#  just increase understanding for us and other coder
#  who want to read our code
# now we can also type key words for 
# touples , dictoneries ,strings ,fuctions and more
