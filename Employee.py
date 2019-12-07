from Person import *


class Employee(Person):
    employee_id = 0

    def __init__(self, emp_id_arg, fn_arg, ln_arg):
        Person.__init__(self, fn_arg, ln_arg)
        self.employee_id = emp_id_arg

    @property
    def get_employee_info(self):
        return f"{self.employee_id} {Person.get_fullname(self)}"


employee: Employee = Employee(10, "Adriana", "Smith")
print(employee.get_employee_info)
