import pytest


def test_add_student(app):

	app.session.ensure_login(username='dmitriev@uchi.ru', password='1')
	old_groups = app.group.get_group_list()
	app.addstudent.add_student()