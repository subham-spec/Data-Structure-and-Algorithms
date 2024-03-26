
class Employee:
    employees = []
    def __init__(self, name, age, salary, role):
        person = []
        person.append(name)
        person.append(age)
        person.append(salary)
        person.append(role)
        self.employees.append(person)

    def get_data(self):
        print(f"{self.employees}")

if __name__ == "__main__":
    e1 = Employee(
        'Subham Sharma',
        22,
        30000,
        'Software Engineer Intern'
    )

    e2 = Employee(
        'Ashok Kumar Sharma',
        45,
        60000,
        'Sub-Army'
    )

    # print(e1.employees)
    e1.get_data()

