import pytest

from data.add_group import testdata
# from data.add_teacher import testdata_reg


# @pytest.mark.skip
from model.group import Group


@pytest.mark.run(order=4)
# @pytest.mark.parametrize('group', testdata[1], ids=[repr(x) for x in testdata])
def test_delete_group(app):
    app.session.ensure_login(username="dmitriev+9@uchi.ru", password="1")
    old_groups = app.group.get_group_list()
    if len(old_groups) == 0:
        group = Group()
        group.name_class = "подлежит уничтожению"
        group.subject_list = ['rus', 'eng', 'env', 'math', 'prog']
        group.number_class = "1"
        app.group.create(group)
    # Здесь:
    # number_class - номер класса,
    # name_class - название класса (сделал чтобы вводилось вручную в коде)
    # subject_list - список с предметами, которые нужно добавить
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

    print("\n Старое кол-во групп: ", len(old_groups))
    print("Новое кол-во групп: ", len(new_groups))
    print("\n старые группы ", old_groups)
    print("новые группы ", new_groups)
