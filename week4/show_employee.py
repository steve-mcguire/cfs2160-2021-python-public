def show_employee(name, salary=9000):
    return "Employee name:" + str(name) + ", Salary:" + str(salary)


print(show_employee("Ben", 7000))
print(show_employee("Jessa"))
print(show_employee("Steve", -2000))

