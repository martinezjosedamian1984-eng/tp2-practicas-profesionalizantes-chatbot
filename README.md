# Chatbot E-commerce ComercioJoyDami

# Descripción general

Este proyecto consiste en un chatbot web desarrollado con Python y Flask, orientado a consultas básicas sobre productos, stock y ventas de un comercio simulado.

El chatbot permite interactuar con el usuario mediante una interfaz web y responder consultas relacionadas con el estado del negocio, productos con bajo stock, productos más caros, stock por categoría, recomendaciones de reposición y ayuda general.

El objetivo del proyecto es aplicar conceptos de programación, organización de archivos, lógica condicional y desarrollo web básico, integrando Python con HTML, CSS y JavaScript.

# Tecnologías utilizadas

* Python
* Flask
* HTML
* CSS
* JavaScript
* Git
* GitHub

# Estructura del proyecto

```text
tp2-practicas-profesionalizantes-chatbot/
│
├── app.py
├── reglas.py
├── README.md
├── respuestas_scrum.md
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── script.js
    ├── styles.css
    └── img/
        └── fondo.png
```

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Ingresar a la carpeta del proyecto:

```bash
cd tp2-practicas-profesionalizantes-chatbot
```

3. Crear un entorno virtual:

```bash
python3 -m venv .venv
```

4. Activar el entorno virtual:

```bash
source .venv/bin/activate
```

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Ejecutar la aplicación:

```bash
python app.py
```

7. Abrir el navegador en:

```text
http://127.0.0.1:5000
```

# Funcionalidades principales

* Consulta de productos con bajo stock.
* Consulta de productos más caros.
* Consulta de stock total por categoría.
* Recomendación de productos para reponer.
* Resumen general del negocio.
* Interfaz web con diseño personalizado.
* Separación entre servidor Flask, lógica del sistema experto y archivos estáticos.

# Ejemplos de consultas

El usuario puede escribir o seleccionar consultas como:

```texto
stock bajo
más caros
stock por categoría
reponer stock
resumen general
ayuda
estado negocio
```

# Conclusiones personales

Este proyecto me permitió comprender mejor cómo se puede integrar Python con una interfaz web para crear una aplicación interactiva. También pude practicar la organización de carpetas, el uso de Flask para crear rutas, el manejo de peticiones desde JavaScript y la separación de la lógica del programa en distintos archivos.

Además, el proyecto me ayudó a relacionar conceptos de programación con situaciones cercanas al mundo laboral, como el análisis de productos, stock y ventas dentro de un comercio. Documentarlo en GitHub también me permitió practicar buenas prácticas de presentación y control de versiones.
