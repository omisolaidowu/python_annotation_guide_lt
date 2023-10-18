import inspect

#variable type hints
first_name: str = "Idowu"

last_name: str = "Omisola"

age: int = 30

languages: list = ["Python", "Golang", "C"]


print(type(age))

# function type hint
def test_should_do_x(age:int, languages: list, name: str, *args:str, **kwargs:str)->tuple:
    return age, languages, args, kwargs


def gone()->str:
    
    return "Idowu"

print(test_should_do_x(30, ["Python"], "Idowu", "optional", test="11", land="87"))


# Getting all annotations
print("annotation:", inspect.get_annotations(test_should_do_x))

print(test_should_do_x.__annotations__)

#*args will return a tupple with trailing coma because the function can take n number of positional arguments
#**kwargs will give a dictionary containing the number of keyword arguments passed into the function



