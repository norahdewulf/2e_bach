class Course:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def getCourseName(self):
        return self.__name

    def addStudent(self, student):
        self.__students.append(student)

    def dropStudent(self, student):
        self.__students.remove(student)

    def getStudents(self):
        return self.__students

    def getNumberOfStudents(self):
        return len(self.__students)

    def print_students_course(self):
        for student in self.__students:
            print(student) #the name of the student is printed