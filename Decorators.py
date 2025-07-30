"""
_summary_
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
