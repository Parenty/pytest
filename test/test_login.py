def test_login(app):
	app.session.ensure_login(username='dmitriev@uchi.ru', password='1')
	



