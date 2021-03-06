import pytest
from data.add_group import testdata
from fixture import registration
from data.add_teacher import testdata_reg
from model.registration import Reg


@pytest.mark.run(order=2)
@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_create_group(app, group):
    # auth = Reg()
    # auth.email = testdata_reg
    # user = auth.email
    # pswd = auth.password
    user = 'dmitriev+7@uchi.ru'
    pswd = '1'

    app.session.ensure_login(username=user, password=pswd)
    not_registered = app.group.is_not_registered()
    if not_registered:
        registration.email = user
        registration.password = pswd
        registration.number_class = group.number_class
        registration.name_class = group.name_class
        registration.subject_list = group.subject_list
        app.registration.reg_teacher(registration)

    old_groups = app.group.get_group_list()
    app.group.create(group)

    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

    print("Старые группы: ", old_groups)
    print("Новые группы: ", new_groups)
    print("\n Старое кол-во групп: ", len(old_groups))
    print("Новое кол-во групп: ", len(new_groups))
