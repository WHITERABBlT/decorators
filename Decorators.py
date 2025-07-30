"""
The above code defines a decorator that adds functionality before and after the execution of
functions `func1` and `func2`.

:param func: In the code you provided, `func` is a parameter that represents a function. It is used
as an argument in the `my_decorator` function, which is a decorator that adds functionality to the
functions `func1` and `func2`. The `wrapper` function within the decorator prints a
:return: The `my_decorator` function is a decorator that takes a function as an argument, wraps it
with additional functionality, and returns the wrapper function. In this case, when `func1` and
`func2` are decorated with `@my_decorator`, they are replaced with the wrapper functions returned by
`my_decorator`.
"""

def my_decorator(func):

    def wrapper():
        print (f"Running {func.__name__}.")
        func()
        print ("Complete")
    return wrapper

@my_decorator
def func1():
    print ("Task for function 1.")

@my_decorator
def func2():
    print ("Task for function 1.")

func1()
func2()
