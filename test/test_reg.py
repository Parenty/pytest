from model.group import Group
import pytest
from data.add_group import testdata_reg

@pytest.mark.parametrize('group', testdata_reg, ids = [repr(x) for x in testdata_reg])
def test_reg_teacher(app, group):
	app.open_home_page()
	app.registration.reg_teacher(group)