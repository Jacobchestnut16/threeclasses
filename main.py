import Student, Course, Enrollment
student = Student('Jon Doe', '4442229998710', 2.6)
course = Course('CIST', 'Object Oriented', 'Jeremy Callinan', 2.5)

enrollment = Enrollment(student, course)

print('The student,', student.id(), 'can join the course', course.title, ':', enrollment.is_enrolled)
if enrollment.isCompatible():
    print('The student is now enrolled')
    enrollment.enroll()
else:
    print('The student cannot enroll')

course = Course('MATH', 'Calculus 467', 'Calvin Manchester', 3.4)
enrollment = Enrollment(student, course)

print('The student,', student.id(), 'can join the course', course.title, ':', enrollment.is_enrolled)
if enrollment.isCompatible():
    print('The student is now enrolled')
    enrollment.enroll()
else:
    print('The student cannot enroll')
