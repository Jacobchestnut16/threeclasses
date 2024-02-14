# The Course class could represent different courses offered by an educational
# institution with attributes like course code, title, instructor, etc.
class Course:
    def __init__(self, subject, title, instructor, gpaRequirement):
        self.subject = subject
        self.title = title
        self.instructor = instructor
        self.gpaRequirement = gpaRequirement
        self.enrollmentIDS = []

    def addEnrollment(self, enrollmentID):
        self.enrollmentIDS.append(enrollmentID)
