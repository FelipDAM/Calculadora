'''importar'''
import pytest
from src.main import CalcApp


@pytest.fixture # Es carrega sempre al principi del test
def app(qtbot):
    '''metode app'''
    test_app = CalcApp()
    qtbot.addWidget(test_app.ui)
    return test_app


def test_marcar1(app):
    '''Test per a comprovar que es pot introduir el número 1'''
    # Simulem un clic al botó "1"
    app.ui.Button1.click()

    # Verifiquem que el display mostra "1"
    assert app.ui.display.value() == int('1')

def test_marcar2(app):
    '''Test per a comprovar que es pot introduir el número 1'''
    # Simulem un clic al botó "1"
    app.ui.Button2.click()

    # Verifiquem que el display mostra "1"
    assert app.ui.display.value() == int('2')

def test_sumar(app):
    '''Test per comprovar que es pot sumar'''
    app.ui.Button2.click()
    app.ui.sumaButton.click()
    app.ui.Button2.click()
    app.ui.igualButton.click()

    assert app.ui.display.value() == int('4')

def test_restar(app):
    '''Test per comprovar que es pot sumar'''
    app.ui.Button2.click()
    app.ui.restaButton.click()
    app.ui.Button2.click()
    app.ui.igualButton.click()

    assert app.ui.display.value() == int('0')

def test_netejarpantalla(app):
    '''Test per comprovar que es pot netejar la pantalla'''
    app.ui.Button2.click()
    app.ui.Button2.click()
    app.ui.borrarButton.click()

    assert app.ui.display.value() == int("0")
