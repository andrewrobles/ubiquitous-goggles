# Alexandra Coelho, CIS 345, 10:30, PE9

# TODO: Student class
class Student:
    def __init__(self, fname='', lname=''):
        self.first_name = fname.capitalize() if fname.isalpha() else 'Unknown'
        self.last_name = lname.capitalize() if lname.isalpha() else 'Unknown'

    @property
    def name(self):

        return self.__name.capitalize()

    @name.setter
    def name(self, new):
        if new.isalpha():
            self.__name = new
        else:
            self.__name = 'Unknown'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


# TODO: GradStudent class
class GradStudent(Student):
    def __init__(self, fname='', lname='', thesis=''):
        super().__init__(fname, lname)
        self.thesis = thesis.upper()

    @property
    def thesis(self):
        return self.thesis

    @thesis.setter
    def thesis(self, thesis):
        self.thesis.upper()

    def __str__(self):
        return '{} {}\n\tTHESIS: {}'.format(self.first_name, self.last_name, self.thesis)


# TODO: PhDStudent class
class PhDStudent(Student):
    def __init__(self, fname='', lname='', dissertation=''):
        super().__init__(fname, lname)
        self.dissertation = dissertation.upper()

    @property
    def dissertation(self):
        return self.dissertation

    @dissertation.setter
    def dissertation(self, dissertation):
        self.dissertation.upper()

    def __str__(self):
        return '{} {}\n\tDISSERTATION: {}'.format(self.first_name, self.last_name, self.dissertation)


def add_student(studentType):
    """Get student data and create an object to be returned"""
    student = None
    # Get first and last name here because all students need this data
    first = input('Enter first name: ')
    last = input('Enter last name: ')

    # TODO: Determine student type and construct an object and save in student
    if studentType == "G":
        thesis_title = input('Enter thesis title: ').casefold()
        new_student = GradStudent(first, last, thesis_title)

    elif studentType == "P":
        dissertation_title = input('Enter dissertation title: ').casefold()
        new_student = PhDStudent(first, last, dissertation_title)

    # TODO: Assign last_name using our object's property then return student
    else:
        new_student = Student(first, last)

    return new_student


# Main Function
def main():
    """Main program logic"""
    students = []
    entry = ''
    print("{:^50}".format('Student Management System'))

    while entry != 'X':
        studentTypes = ['S', 'G', 'P']
        # Get user entry and capitalize the entry
        entry = input('\nEnter (S)tudent, (G)radStudent, (P)hDStudent or (X)exit: ')
        entry = entry.upper()

        if entry == 'X':
            break

        # TODO: Is user entry one of studentTypes. Yes - add_student to list
        new_student = add_student(entry)
        students.append(new_student)

    # TODO: print students and dissertation if the student is a PhD type
    print("\nThe following students were added...")

    for curr_student in students:
        print(curr_student)


if __name__ == "__main__":
    # call and execute the main function
    main()
