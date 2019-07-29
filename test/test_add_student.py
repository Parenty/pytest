import pytest
from data.add_teacher import testdata_reg


@pytest.mark.run(order=3)
@pytest.mark.parametrize('registration', testdata_reg, ids=[repr(x) for x in testdata_reg])
def test_add_student(app, registration):
    user = 'dmitriev@uchi.ru'
    pswd = '123'

    app.session.ensure_login(username=user, password=pswd)
    not_registered = app.group.is_not_registered()
    if not_registered:
        registration.email = user
        registration.password = pswd("scrollBy(0,250);")
        app.registration.reg_teacher(registration)

    # old_groups = app.group.get_group_list()
    old_students = app.addstudent.get_students_list()
    app.addstudent.add_student()
    new_students = app.addstudent.get_students_list()
    assert len(old_students) + 1 == len(new_students)

    print("Старые студенты ", old_students)
    print("Новые студенты", new_students)
    print("\n Старое кол-во студентов: ", len(old_students))
    print("Новое кол-во студентов: ", len(new_students))
