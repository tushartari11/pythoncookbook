def greet_user():
    """Greeting user"""
    print("Hello user")


def greet_user_by_name(name="DefaultUsername", greeting="Hello"):
    """Customized Greeting"""
    print(greeting + ", " + name)


def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value

greet_user()
greet_user_by_name()
greet_user_by_name(input("what is your name ?"))
greet_user_by_name("Dino","Welcome")
greet_user_by_name(greeting="Hello", name="Tushar")

elevenCubed = cube(11)
print(elevenCubed)
