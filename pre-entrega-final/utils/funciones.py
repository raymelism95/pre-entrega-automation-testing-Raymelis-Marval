from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"

USUARIO = "standard_user"
PASSWORD = "secret_sauce"


def login(driver):

    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    # Usuario
    campo_usuario = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys(USUARIO)

    # Password
    campo_password = driver.find_element(By.ID, "password")
    campo_password.send_keys(PASSWORD)

    # Botón login
    boton_login = driver.find_element(By.ID, "login-button")
    boton_login.click()


def validar_inventory(driver):

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url

    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"


def validar_catalogo(driver):

    wait = WebDriverWait(driver, 10)

    # Validar título
    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    # Validar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) > 0

    # Obtener primer producto
    primer_nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    primer_precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"\nPrimer producto: {primer_nombre}")
    print(f"Precio: {primer_precio}")

    # Validar menú
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()

    # Validar filtro
    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert filtro.is_displayed()


def agregar_primer_producto(driver):

    wait = WebDriverWait(driver, 10)

    # Obtener nombre producto
    nombre_producto = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    ).text

    # Agregar producto
    boton_add = driver.find_element(
        By.CLASS_NAME,
        "btn_inventory"
    )

    boton_add.click()

    # Validar contador carrito
    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1"

    # Ir al carrito
    carrito = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    carrito.click()

    return nombre_producto


def validar_carrito(driver, nombre_producto):

    wait = WebDriverWait(driver, 10)

    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre_producto