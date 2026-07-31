def prettify(symbol):
    def decorator(func):
        def wrapper(text):
            print(symbol*len(text))
            func(text)
            print(symbol*len(text))
        return wrapper
    return decorator

@prettify("*")
def print_name(name):
    print(name)

@prettify("-")
def print_city(city):
    print(city)

print_name("caio")
print_city("BH")
