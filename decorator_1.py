def my_decorator(f):
    def wrapper():
        print("Something is happening before the function is called.")
        f()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Define a function to be decorated
def say_hello():
    print("Hello!")

# Decorate the function
say_hello_decorated = my_decorator(say_hello)

# Call the decorated function
say_hello_decorated()