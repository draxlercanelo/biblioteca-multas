
"""Módulo para calcular multas por retraso en préstamos de biblioteca."""


def calcular_multa(dias_retraso: int, tarifa_diaria: float) -> float:
    """Calcula la multa total según los días de retraso y la tarifa diaria.

    Args:
        dias_retraso: Número de días de retraso en la devolución.
        tarifa_diaria: Importe de la multa por cada día de retraso.

    Returns:
        El importe total de la multa.

    Raises:
        ValueError: Si los días o la tarifa son negativos.
    """
    if dias_retraso < 0:
        raise ValueError("Los días de retraso no pueden ser negativos.")

    if tarifa_diaria < 0:
        raise ValueError("La tarifa diaria no puede ser negativa.")

    return dias_retraso * tarifa_diaria


if __name__ == "__main__":
    print("La multa es:", calcular_multa(3, 2.0))
