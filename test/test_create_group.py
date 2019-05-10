from model.group import Group

def test_create_group(app):
	app.session.login(username='dmitriev@uchi.ru', password='123')
	# Здесь:
	# number_class - номер класса,
	# name_class - название класса (сделал чтобы вводилось вручную)
	# subject_list - список с предметами, которые нужно добавить (пока что можно добавить только 4 основнных предмета)
	app.group.create(Group(number_class = '2 класс', name_class = 'тестовый класс', subject_list =['rus', 'eng', 'env']))