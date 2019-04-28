import pytest
from selenium import webdriver
from fixture.application import Application

@pytest.fixture
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture


def test_login(app):
	app.login(username='dmitriev@uchi.ru', password='123')
	app.logout()



