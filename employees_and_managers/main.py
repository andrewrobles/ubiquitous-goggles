# Alexandra Coelho, CIS 345, 10:30, A5

class Employee:
    def __init__(self, name='', eid=''):
        self.name = name
        self.eid = eid


    @property
    def name(self):
        return self.name.capitalize()

    @name.setter
    def name(self, new):
        if new.isalpha():
            self.name = new
        else:
            self.name = 'Unknown'

    @property
    def eid(self):
        return self.eid

    @eid.setter
    def eid(self, length):
        if len(0):
            self.eid = '9999'
        else:
            return self.eid

    def __str__(self):
        return '{} {}'.format(self.name, self.eid)


class Manager(Employee):
    def __init__(self, name='', eid=''):
        super().__init__(name, eid)
    pass


def add_employee():
    employee = None

    name = input('\nEnter name: ')
    eid = input('Enter id: ')
    employee_type = input('Is the employee a manager (Y/N) ').casefold()

    if employee_type == "y":
        number = input('How many subordinates? ')
        sub_name = input('Enter subordinates name: ')
        sub_id = input('Enter subordinates id: ')
    else:
        user = '\n'
        user = input('Do you want to enter more? ')


# Main Function
def main():
    """Main program logic"""
    employees = []
    entry = ''
    print("{:^50}".format('Employee Management System'))
    print('\nAdding Employees...')

    while entry != 'n':

        if entry == 'n':
            break

        new_employee = add_employee()
        employees.append(new_employee)

    print("\nPrinting Employee List")

    for curr_employee in employees:
        print(curr_employee)


if __name__ == "__main__":
    # call and execute the main function
    main()