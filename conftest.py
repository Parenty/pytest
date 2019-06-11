import pytest
from fixture.application import Application

fixture  = None

@pytest.fixture
def app(request):
	global fixture
	if fixture is None:
		browser = request.config.getoption('--browser')
		fixture = Application(browser=browser)
	else:
		if not fixture.is_valid():
			fixture = Application()
	return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):

	def fin():
		fixture.session.ensure_logout()
		fixture.destroy()
	request.addfinalizer(fin)
	return fixture


def pytest_addoption(parser):
	parser.addoption('--browser', action='store', default='chrome')