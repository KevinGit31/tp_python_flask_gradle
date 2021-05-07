from toto import totototo
from src import api_flask


def hello(name):
    return 'Hello ' + name


def test_hello():
    assert hello('Celine') == 'Hello Celine'


def test_tototo():
    assert totototo.printtoto() == "Salt"


def test_index():
    assert api_flask.index() == "Hello Kevin"

