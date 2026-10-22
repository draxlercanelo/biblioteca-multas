# Decisiones técnicas

## Decisión 1: validar antes de calcular

**Problema:** el código inicial calculaba antes de validar los datos.

**Decisión:** comprobar los valores antes de realizar el cálculo.

**Justificación:** evita continuar con entradas inválidas.

## Decisión 2: separar responsabilidades

**Problema:** la función original validaba, calculaba e imprimía mensajes.

**Decisión:** crear funciones de validación y mantener el cálculo separado.

**Justificación:** el código es más fácil de leer y probar.

## Decisión 3: automatizar las comprobaciones

**Decisión:** usar Pytest para verificar los resultados esperados.

**Justificación:** permite repetir las comprobaciones después de cada cambio.
