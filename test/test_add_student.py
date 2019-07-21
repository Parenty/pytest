import pytest
from model.registration import Reg
from data.add_group import testdata
from data.add_teacher import testdata_reg
import time

@pytest.mark.run(order=3)
@pytest.mark.parametrize('registration', testdata_reg, ids = [repr(x) for x in testdata_reg])
def test_add_student(app, registration):

	user='dmitriev+54@uchi.ru'
	pswd = '1'

	app.session.ensure_login(username=user, password=pswd)
	not_registered = app.group.is_not_registered()
	if not_registered == True:
		registration.email = user
		registration.password = pswd
		app.registration.reg_teacher(registration)

	old_groups = app.group.get_group_list()
	app.addstudent.add_student()