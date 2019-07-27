import pytest
from data.add_group import testdata
import pytest

from data.add_group import testdata


@pytest.mark.run(order=4)
@pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
def test_delete_group(app, group):
    app.session.ensure_login(username='dmitriev@uchi.ru', password='123')
    old_groups = app.group.get_group_list()
    if len(old_groups) == 0:
        app.group.create(group)
    # Здесь:
    # number_class - номер класса,
    # name_class - название класса (сделал чтобы вводилось вручную в коде)
    # subject_list - список с предметами, которые нужно добавить
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

    print("\n Старое кол-во групп: ", len(old_groups))
    print("Новое кол-во групп: ", len(new_groups))
    print("\n старые группы ", old_groups)
    print("новые группы ", new_groups)
