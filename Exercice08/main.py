def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de la fonction '{func.__name__}'.")
        result = func()            
        print(f"La fonction '{func.__name__}' est décorée. ")
        return result
    return wrapper
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
