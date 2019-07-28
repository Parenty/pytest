class Students:

    def __init__(self, num_student=None, password_student=None):
        self.num_student = num_student
        self.password_student = password_student

    def __repr__(self):
        return "%s:%s" % (self.num_student, self.password_student)
