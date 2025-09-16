# 🛒 CHAMBA TECH | Tienda de Componentes y Periféricos

## Descripción del Proyecto

**CHAMBA TECH** es una plataforma de comercio electrónico diseñada para la venta de componentes y periféricos de alta tecnología. El proyecto fue desarrollado como una demostración de una aplicación web funcional, enfocada en la facilidad de uso y la experiencia de usuario.

---

### 🚀 Características Principales

* **Autenticación Sencilla:** Sistema de inicio de sesión y registro sin contraseñas.
* **Carrito de Compras:** Funcionalidad para agregar y remover productos dinámicamente.
* **Catálogo de Productos:** Una amplia selección de mouses, teclados, monitores y más.
* **Navegación Intuitiva:** Páginas de categorías y productos detalladas.

---

### 💻 Tecnologías Utilizadas

* **Backend:** Python 3 y el framework **Flask**.
* **Frontend:** HTML, CSS y JavaScript.

---

### ⚙️ Instalación y Uso Local

Sigue estos pasos para ejecutar el proyecto en tu computadora. Se recomienda usar un entorno virtual para evitar conflictos con otros proyectos.

1.  Asegúrate de tener Python 3 instalado.
2.  Clona este repositorio o descarga el código fuente.
3.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```
5.  Ejecuta la aplicación desde la terminal:
    ```bash
    python app.py
    ```
6.  Abre tu navegador y visita `http://127.0.0.1:5000/`.

---

### ☁️ Despliegue en Producción

Esta aplicación está configurada para ser desplegada en servicios de PaaS (Platform as a Service) como **Render** o **Heroku**. La aplicación utiliza **Gunicorn** como servidor web en producción.

**Comando para el despliegue:**
```bash
gunicorn app:app
