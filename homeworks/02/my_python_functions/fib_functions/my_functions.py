def cache_decorator(func_to_decorate):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func_to_decorate(n)
        return cache[n]
    return wrapper

@cache_decorator
def fib(n):
    if n == 0:
        return 0
    if  n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

