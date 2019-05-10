from model.group import Group

def test_create_group(app):
	app.session.login(username='dmitriev@uchi.ru', password='123')
	app.group.create(Group(number_class = '2 класс', name_class = 'тестовый класс', subject_list =['rus', 'eng', 'env']))