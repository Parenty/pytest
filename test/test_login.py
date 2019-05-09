def test_login(app):
	app.session.login(username='dmitriev@uchi.ru', password='123')
	app.session.logout()



