from  person import Person


class Student(Person):

    def __init__(self, firstName, lastName, middleName, id , type, section, year, course):
        super().__init__(firstName, lastName, middleName, id, type)
        self.section = section
        self.year = year
        self.course = course

    def getYrCourseSec(self):
            return (f'{self.year}/{self.course}/{self.section}')

