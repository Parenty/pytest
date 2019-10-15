import pytest
from data.add_student import testdata_add_student
from model.registration import Reg


@pytest.mark.run(order=3)
# @pytest.mark.repeat(20)
@pytest.mark.parametrize('students', testdata_add_student, ids=[repr(x) for x in testdata_add_student])
def test_add_student(app, students):
    user = 'dmitriev+9@uchi.ru'
    pswd = '1'

    app.session.ensure_login(username=user, password=pswd)
    not_registered = app.group.is_not_registered()
    if not_registered:
        registration = Reg()
        registration.email = user
        registration.password = pswd
        registration.number_class = "3"
        registration.subject_list = ['math', 'rus', 'eng']
        registration.name_class = "проверка регистрации"
        app.registration.reg_teacher(registration)

    # old_groups = app.group.get_group_list()
    old_students = app.addstudent.get_students_list()
    app.addstudent.add_student(students)
    new_students = app.addstudent.get_students_list()
    assert len(old_students) + 1 == len(new_students)

    print("Старые студенты ", old_students)
    print("Новые студенты", new_students)
    print("\n Старое кол-во студентов: ", len(old_students))
    print("Новое кол-во студентов: ", len(new_students))
