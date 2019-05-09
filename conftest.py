import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
	fixture = Application()
	fixture.session.login(username='dmitriev@uchi.ru', password='123')
	request.addfinalizer(fixture.destroy)
	return fixture