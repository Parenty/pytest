import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
	fixture = Application()
	def fin():
		fixture.session.logout()
		fixture.destroy()
	request.addfinalizer(fin)
	return fixture