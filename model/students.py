class Students:

    def __init__(self, num_student=None, password_student=None, student_name=None, student_surname=None):
        self.num_student = num_student
        self.password_student = password_student
        self.student_name = student_name
        self.student_surname = student_surname

    def __repr__(self):
        return "%s:%s" % (self.num_student, self.password_student)
