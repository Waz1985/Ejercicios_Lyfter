def pre_post_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Pre function logic prints: {args} and {kwargs}")
        result = func(*args, **kwargs)
        print("Post function logic")
        return result
    return wrapper

@pre_post_decorator
def show_user(name, age):
    print(f"User name is {name} and age is {age}")
    return f"{name} - {age}"

show_user("Jose", 35)