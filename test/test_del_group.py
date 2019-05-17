from model.group import Group

def test_delete_group(app):
	app.session.ensure_login(username='dmitriev@uchi.ru', password='123')
	old_groups = app.group.get_group_list()
	# Здесь:
	# number_class - номер класса,
	# name_class - название класса (сделал чтобы вводилось вручную)
	# subject_list - список с предметами, которые нужно добавить
	app.group.delete_first_group()
	new_groups = app.group.get_group_list()
	assert len(old_groups)-1 == len(new_groups)

	print ("\n Старое кол-во групп: ", len(old_groups))
	print ("Новое кол-во групп: ", len(new_groups))