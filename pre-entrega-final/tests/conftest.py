import os
import logging
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# =========================
# CONFIGURACIÓN DE LOGS
# =========================

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# FIXTURE DRIVER
# =========================

@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logging.info("Navegador iniciado")

    yield driver

    driver.quit()

    logging.info("Navegador cerrado")


# =========================
# SCREENSHOT AUTOMÁTICO
# =========================

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    # Solo si el test falló
    if rep.when == "call" and rep.failed:

        driver = item.funcargs["driver"]

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        nombre_test = item.name

        screenshot_path = (
            f"screenshots/{nombre_test}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        logging.error(
            f"Fallo en test: {nombre_test}"
        )

        logging.error(
            f"Screenshot guardado en: {screenshot_path}"
        )