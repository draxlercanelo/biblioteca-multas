
import pytest

from biblioteca import calcular_multa


def test_calcular_multa():
    assert calcular_multa(3, 2) == 6


def test_multa_sin_retraso():
    assert calcular_multa(0, 2) == 0


def test_multa_con_tarifa_cero():
    assert calcular_multa(3, 0) == 0


def test_dias_negativos():
    with pytest.raises(ValueError):
        calcular_multa(-1, 2)


def test_tarifa_negativa():
    with pytest.raises(ValueError):
        calcular_multa(3, -2)
