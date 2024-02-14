#The Student class could represent students with attributes like name, ID, GPA, etc.

class Student:
    def __init__(self, name, id, gpa):
        self.name = name
        self.ID = id
        self.GPA = gpa
        self.courses = []

    def id(self):
        return self.ID

    def hasGPA(self):
        return self.GPA > 0

    def gpa(self):
        return self.GPA

    def addCourse(self, course):
        self.courses.append(course)

    def id(self):
        return self.ID