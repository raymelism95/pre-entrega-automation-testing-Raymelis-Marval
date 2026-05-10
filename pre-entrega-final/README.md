# Proyecto QA Automation - SauceDemo

Proyecto de automatización QA desarrollado con Python, Selenium WebDriver y Pytest sobre el sitio SauceDemo.

---

# Objetivo del Proyecto

Automatizar casos de prueba funcionales básicos para validar:

- Login de usuario
- Navegación del catálogo de productos
- Interacción con productos
- Funcionamiento del carrito de compras

El proyecto implementa buenas prácticas de automatización QA utilizando:

- Pytest
- Selenium WebDriver
- Fixtures
- Esperas explícitas
- Evidencias automáticas de fallos
- Reportes HTML

---

# Tecnologías Utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML Reporter
- WebDriver Manager

---

# Estructura del Proyecto

```text
pre-entrega-final/
│   .gitignore
│   README.md
│   reporte.html
│   requirements.txt
│               
├───assets
│       style.css
│       
├───logs
│       ejecucion.log
│       
├───screenshots
├───tests
│   │   conftest.py
│   │   test_saucedemo.py
│   │   __init__.py
│           
└───utils
    │   funciones.py
    │   __init__.py
    │   
    ├───logs
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Ingresar al proyecto

```bash
cd pre-entrega-final
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Dependencias Utilizadas

El proyecto utiliza las siguientes librerías:

```text
selenium
pytest
webdriver-manager
pytest-html
```

---

# Ejecución de Pruebas

## Ejecutar todos los tests

```bash
pytest -v
```

---

## Ejecutar archivo específico

```bash
pytest tests/test_saucedemo.py -v
```

---

## Generar reporte HTML

```bash
pytest tests/test_saucedemo.py -v --html=reporte.html
```

Al finalizar la ejecución se generará el archivo:

```text
reporte.html
```

que puede abrirse desde cualquier navegador.

---

# Casos de Prueba Implementados

## 1. Login Exitoso

Validaciones realizadas:

- Navegación a SauceDemo
- Ingreso de credenciales válidas
- Click en Login
- Validación de redirección a:
  
```text
inventory.html
```

- Validación del título:
  
```text
Products
```

---

## 2. Navegación y Validación de Catálogo

Validaciones realizadas:

- Verificación del título de inventario
- Validación de productos visibles
- Obtención de nombre y precio del primer producto
- Verificación de menú hamburguesa
- Verificación de filtro de productos

---

## 3. Carrito de Compras

Validaciones realizadas:

- Agregado del primer producto al carrito
- Validación del contador del carrito
- Navegación al carrito
- Verificación de producto agregado correctamente

---

# Evidencias Automáticas de Fallos

El proyecto genera evidencias automáticamente cuando un test falla.

## Screenshots automáticos

Si ocurre un fallo se genera una captura en:

```text
screenshots/
```

Ejemplo:

```text
screenshots/test_login_exitoso_20260510_164020.png
```

---

## Logs de ejecución

Se genera automáticamente un archivo de logs en:

```text
logs/ejecucion.log
```

Incluye:

- Inicio de navegador
- Cierre de navegador
- Errores de ejecución
- Ruta de screenshots generados

---

# Buenas Prácticas Implementadas

- Tests independientes
- Uso de fixtures de Pytest
- Esperas explícitas
- Código modularizado
- Separación de responsabilidades
- Manejo automático de evidencias
- Nomenclatura descriptiva
- Estructura escalable

---

# Autor

Proyecto realizado Raymelis Marval para curso de Testing QA Automation.