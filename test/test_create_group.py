import pytest
from data.add_group import testdata
from data.add_teacher import testdata_reg


@pytest.mark.run(order=2)
@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
@pytest.mark.parametrize('registration', testdata_reg, ids=[repr(x) for x in testdata_reg])
def test_create_group(app, group, registration):
    # user = 'dmitriev@uchi.ru'
    # pswd = '123'

    app.session.ensure_login(username=registration.email, password=registration.password)
    not_registered = app.group.is_not_registered()
    if not_registered:
        registration.email = registration.email
        registration.password = registration.password
        app.registration.reg_teacher(registration)

    old_groups = app.group.get_group_list()
    app.group.create(group)

    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

    print("Старые группы: ", old_groups)
    print("Новые группы: ", new_groups)
    print("\n Старое кол-во групп: ", len(old_groups))
    print("Новое кол-во групп: ", len(new_groups))
