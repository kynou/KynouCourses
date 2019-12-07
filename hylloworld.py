from datetime import *
import time

print("Hello World")


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(2, 3)

assert isinstance(result, int)
print(result)

answer = 42
pi = 3.14159
result2 = answer + pi

print(result2)

pi_result = int(pi)
answer_result = float(answer)

print(pi_result)
print(answer_result)

# Strings
single_quote_string = 'Hello World'
double_quote_string = "This is a single quote: ' "
triple_double_quote_string = """"What is this for? So I can use single quote ' and double quote " """

print(single_quote_string)
print(double_quote_string)
print(triple_double_quote_string)

uppercase = "hello".capitalize()
replace_string = "america".replace("eric", "ME")
is_text = "this is text, not number".isalpha()
is_number = "1974".isdigit()

print(uppercase)
print(replace_string)
print(is_text)
print(is_number)

books = "Book1,Book2,Book3".split(",")
print(books)

first_name = "John"
last_name = "Smith"
combine_text = "First Name:{0} Last Name:{1}".format(first_name, last_name)
print(combine_text)

combine_text_2 = f"First Name:{first_name} Last Name: {last_name}"
print(combine_text_2)

bool_value = True
int_bool_value = int(bool_value)
print(bool_value)
print(int_bool_value)

is_null_var = "John Smith"

if is_null_var:
    print("Var is NOT null")
else:
    print("Var is null or None in Python")

input_number = 5

if 3 <= input_number <= 10:
    print("Number is between 3 and 5")

if first_name == "John" and last_name == "Smith":
    print("This is the guy!")

if first_name == "John" or first_name == "Mike":
    print("This is John or Mike")

message_output = "This is John" if first_name == "John" else "This is NOT John"
print(message_output)

first_names = ["Paula", "Mike", "Claudia", "Tom"]
print(first_names[0])
print(first_names[3])
print(first_names[-1])
print(first_names[-4])

first_names.append("Fernanda")
print(first_names)

is_she_there = "Claudia" in first_names
print(is_she_there)

number_of_people = len(first_names)
print(number_of_people)

del first_names[0]
print(first_names)

start_at_claudia = first_names[1:]
print(start_at_claudia)

range_of_names = first_names[1:-1]
print(range_of_names)

for first_name in first_names:
    print(first_name)

x = 0
for i in range(5, 10):
    x += i
    print(x)

range_list = range(10, 100, 5)
# print(range_list)
for i in range_list:
    print(i)

"""""
start_time = datetime.now()
time.sleep(5)
end_time = datetime.now() - start_time
print(end_time.seconds)
"""""

"""""
start_time = datetime.now()
while (datetime.now() - start_time).seconds <= 5:
    print("wait...")
    time.sleep(1)

print("Done!")
"""""

people = []
person1 = {
    "First Name": "John",
    "Last Name": "Smith"
}
people.append(person1)
person2 = {
    "First Name": "Claudia",
    "Last Name": "Baker"
}
people.append(person2)
print(people)

people[0]["First Name"] = "Peter"
print(people)

person_last_name = person1.get("Last Name", "N/A")
person_address = person1.get("Address", "N/A")
print(person_last_name)
print(person_address)

print("Key Names")
print(person1.keys())

print("Key Values")
print(person1.values())

try:
    address_of_person = person1["Address"]
except Exception as error:
    print("There is no Address field in person1")
    print(error)

print("App is not dead!")

enter_first_name = input("Please type your first name:")
enter_last_name = input("Please type your last name:")
result = f"Your Fullname: {enter_first_name} {enter_last_name}"
print(result)


def get_fullname(first_name_arg, last_name_arg, city="Rochester"):
    fullname_result = f"{first_name_arg} {last_name_arg} @ {city}"
    return fullname_result


fullname_returned = get_fullname("Mike", "Baker", "Buffalo")
print(fullname_returned)


def get_me_all(last_name_arg, *args):
    print(last_name_arg)
    print(args)


get_me_all("Smith", "Rochester", "NY", "USA")


def get_all_key_values(last_name_arg, **kwargs):
    print(last_name_arg)
    print(kwargs)


get_all_key_values("Baker", city="Rochester", state="NY")

