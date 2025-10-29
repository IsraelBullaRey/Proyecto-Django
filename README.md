# Proyecto Django — Biblioteca

Este proyecto es una aplicación web desarrollada con **Django**, que permite gestionar **autores, libros y reseñas**.  
Incluye un panel de administración con CRUD completo y validaciones personalizadas para cada modelo.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- **Python en su versión 3.10 o más** 🐍 
- **Git** 💾 
- **Virtualenv** o **venv** para crear entornos virtuales, si no lo tiene se puede crear luego dentro del proyecto.

---

## Instalación y ejecución

### 🌟 Clonar el repositorio

```bash
git clone https://github.com/IsraelBullaRey/Proyecto-Django.git
cd Proyecto-Django
```

---

### 🌟 Crear y activar el entorno virtual

#### En Windows (CMD)

```bash
python -m venv venv
venv\Scripts\activate.bat
```

#### En macOS o Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🌟 Verificar que Django este instalado
Windows
```bash
py -m django --version
```
Linux o Mac
```bash
python -m django --version
```

#### Si no se instaló, ejecutar lo siguiente:
Windows
```bash
py -m pip install Django
```
Linux o Mac
```bash
python -m pip install Django
```

### 🌟 Aplicar migraciones

Ejecuta las migraciones de Django para preparar la base de datos:

```bash
python manage.py migrate
```

---

## 🧠 Poblar la base de datos con datos de ejemplo

El proyecto incluye un script llamado `poblar_datos.py` dentro de la carpeta `biblioteca/`  
que agrega autores, libros y reseñas de prueba.

Puedes ejecutarlo de dos formas:

### Opción 1: Desde el shell propio de python

```bash
python manage.py shell
```

Luego, dentro del shell:

```python
exec(open('biblioteca/poblar_datos.py', encoding='utf-8').read())
```

---

### Opción 2: Directamente desde la terminal

```bash
python manage.py shell < biblioteca/poblar_datos.py
```
---

### 🌟 Crear un superusuario

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones (nombre, correo y contraseña).

---

### 🌟 Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Luego abre tu navegador en:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ✅ Validaciones incluidas

- **Autor:** valida que el nombre no esté vacío ni tenga solo espacios.  
- **Libro:** valida que el resumen tenga una longitud mínima.  
- **Reseña:** valida que la calificación esté dentro del rango permitido (por ejemplo, 1–5).

---

💻 Desarrollado con **Django** y **Python**
