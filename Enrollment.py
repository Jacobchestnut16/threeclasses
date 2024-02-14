#The Enrollment class could manage the enrollment of students in courses,
# including methods for adding/removing students from courses, calculating
# average grades, etc.
import Student
import Course

class Enrollment:
    def __init__(self, student = Student.Student('null', 0, 0), course = Course.Course('null','null','null',0)):
        self.Student = student
        self.Course = course

    def isCompatible(self):
        return self.Student.GPA >= self.Course.gpaRequirement

    def enrol(self):
        if self.isCompatible():
            self.Student.addCourse(self.Course.title)
            self.Course.addEnrollment(self.Student.id)

    def isEnrolled(self):
        enrolledStudents = self.Course.getEnrollmentIDs()
        for student in enrolledStudents:
            if self.Student.id == student:
                return True
        return False