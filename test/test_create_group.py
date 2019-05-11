from model.group import Group

def test_create_group(app):
	app.session.ensure_login(username='dmitriev@uchi.ru', password='123')
	# Здесь:
	# number_class - номер класса,
	# name_class - название класса (сделал чтобы вводилось вручную)
	# subject_list - список с предметами, которые нужно добавить
	app.group.create(Group(number_class = '5 класс', name_class = 'тестовый класс', subject_list =['rus', 'eng', 'geo', 'soc']))