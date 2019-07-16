from model.registration import Reg
import pytest
from data.add_teacher import testdata_reg

@pytest.mark.parametrize('registration', testdata_reg, ids = [repr(x) for x in testdata_reg])
def test_reg_teacher(app, registration):
	app.open_home_page()
	app.registration.reg_teacher(registration)
	app.session.ensure_logout()