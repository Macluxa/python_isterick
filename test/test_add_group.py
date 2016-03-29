#-*- coding: utf -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_new_group(app):
    app.session.login(username='admin', password='secret')
    app.create_group(Group(name='test test', header='test test', footer='test test'))
    app.session.logout()
