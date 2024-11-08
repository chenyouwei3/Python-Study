#装饰器第一层都是func函数入口层，后续才是接受参数的
#装饰器
def my_decorator(func):
    def wrapper(name):
        func()
        print("xxx",name)
    return wrapper

@my_decorator
def greet(name="刘航"):
    print(f"Hello {name}")

greet("John")

#带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


