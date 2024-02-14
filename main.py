import Student
import Course
import Enrollment
student = Student.Student('Jon Doe', '4442229998710', 2.6)
course = Course.Course('CIST', 'Object Oriented', 'Jeremy Callinan', 2.5)

enrollment = Enrollment.Enrollment(student, course)

print('The student,', student.id(), 'can join the course', course.title, ':', enrollment.isCompatible())
if enrollment.isCompatible():
    enrollment.enrol()
    if enrollment.isEnrolled():
        print('The student has been enrolled.')
else:
    print('The student cannot enroll')

course = Course.Course('MATH', 'Calculus 467', 'Calvin Manchester', 3.4)
enrollment = Enrollment.Enrollment(student, course)

print('The student,', student.id(), 'can join the course', course.title, ':', enrollment.isCompatible())
if enrollment.isCompatible():
    enrollment.enrol()
    if enrollment.isEnrolled():
        print('The student has been enrolled.')
else:
    print('The student cannot enroll')
