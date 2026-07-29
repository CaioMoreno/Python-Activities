def log_execution(words):
    def decorator(func):
        def wrapper(n1, n2):
            print(f"Starting {words}")
            func(n1, n2)
            print(f"Finished {words}")
        return wrapper
    return decorator

@log_execution("add")
def add(a, b):
    print(f"sum: {a + b}")

@log_execution("arguments")
def arguments(a, b):
    print(f"Arguments: ({a}, {b})")

numbers = arguments(4, 5)
result = add(4, 5)
