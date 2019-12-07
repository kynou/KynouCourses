FILE_NAME = "names.txt"


def add_name(first_name_arg, last_name_arg):
    text_line = f"{first_name_arg} {last_name_arg}"
    file = open(FILE_NAME, "a")
    file.write(text_line + "\n")
    file.close()


# add_name("John", "Smith")
# add_name("Claudia", "Baker")


def read_names():
    file = open(FILE_NAME, "r")
    for line in file.readlines():
        print(line)
    file.close()


# read_names()

generate_fullname_func = lambda first_name, last_name: F"{first_name} {last_name}"


def pass_me_a_lambda(lambda_fun, fn, ln):
    print(lambda_fun(fn, ln))


# It's almost like a delegate
pass_me_a_lambda(generate_fullname_func, "Fernanda", "Silva")
