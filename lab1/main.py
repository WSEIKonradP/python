def log_parameters(func):
    def wrapper(*args, **kwargs):
        params_dict = {}
        for i in range(len(args)):
            name = "param_" + str(i)
            params_dict[name] = type(args[i]).__name__
        for name, value in kwargs.items():
            params_dict[name] = type(value).__name__
        print(params_dict)
        return func(*args, **kwargs)
    return wrapper


@log_parameters
def add(a, b):
    return a + b


@log_parameters
def greet(name, age=0):
    return "Czesc " + str(name)


if __name__ == "__main__":
    add(5, 10)
    add(a=3, b=7)
    greet("Ania", age=20)
