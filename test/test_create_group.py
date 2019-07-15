from model.group import Group
import pytest
from data.add_group import testdata

@pytest.mark.parametrize('group', testdata, ids = [repr(x) for x in testdata])
def test_create_group(app, group):
	app.session.ensure_login(username='dmitriev@uchi.ru', password='1')
	old_groups = app.group.get_group_list()
	# Здесь:
	# number_class - номер класса,
	# name_class - название класса (сделал чтобы вводилось вручную)
	# subject_list - список с предметами, которые нужно добавить
	# Вводим данные для создания класса
	app.group.create(group)

	new_groups = app.group.get_group_list()
	assert len(old_groups)+1 == len(new_groups)

	print ("Старые группы: ", old_groups)
	print ("Новые группы: ", new_groups)
	print ("\n Старое кол-во групп: ", len(old_groups))
	print ("Новое кол-во групп: ", len(new_groups))
	

