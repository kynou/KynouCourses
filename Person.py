class Person:
    first_name = ""
    last_name = ""

    def __init__(self, first_name_arg, last_name_arg):
        self.first_name = first_name_arg
        self.last_name = last_name_arg

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"It's like ToString in C# => {self.get_fullname()}"

# new_person = Person("Paula", "Santos")
# print(new_person.get_fullname())
# print(new_person)
