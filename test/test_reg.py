
import pytest

from data.add_student import testdata_add_student
from data.add_teacher import testdata_reg

@pytest.mark.run(order=1)
@pytest.mark.parametrize('registration', testdata_reg, ids=[repr(x) for x in testdata_reg])
def test_reg_teacher(app, registration):
	app.open_home_page()
	app.registration.reg_teacher(registration)