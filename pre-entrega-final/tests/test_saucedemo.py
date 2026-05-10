from utils.funciones import (
    login,
    validar_inventory,
    validar_catalogo,
    agregar_primer_producto,
    validar_carrito
)


def test_login_exitoso(driver):

    login(driver)

    validar_inventory(driver)


def test_catalogo_productos(driver):

    login(driver)

    validar_catalogo(driver)


def test_carrito_compras(driver):

    login(driver)

    nombre_producto = agregar_primer_producto(driver)

    validar_carrito(driver, nombre_producto)