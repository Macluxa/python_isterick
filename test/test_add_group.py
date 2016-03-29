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
    app.login('admin', 'secret')
    app.create_group(Group(name='test test', header='test test', footer='test test'))
    app.logout()
