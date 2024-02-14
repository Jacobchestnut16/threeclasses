#The Enrollment class could manage the enrollment of students in courses,
# including methods for adding/removing students from courses, calculating
# average grades, etc.
from Student import Student


class Enrollment:
    def __init__(self, student, course):
        self.Student = student
        self.Course = course

    def isCompatible(self):
        if self.Student.Grade >= self.Course.gpaRequirement:
            return True

    def enrol(self):
        if self.isCompatible():
            self.Student.addCourse(self.Course.title)
            self.Course.addEnrollment(self.Student.id)