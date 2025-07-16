# 🧮 Gestión de Productos

Una aplicación de consola en Python para gestionar productos en stock de forma clara, modular y bien documentada. Pensada para terminales reducidas (60 columnas), uso educativo y buenas prácticas de desarrollo.


## 📦 Funcionalidades principales

- Agregar productos con validaciones
- Buscar productos por ID, nombre o categoría
- Editar campos seleccionados (descripción, precio, cantidad)
- Eliminar productos con soft-delete (`is_active = 0`)
- Mostrar productos en una tabla formateada (centrada y acotada)
- Encabezados y mensajes estilizados con `colorama`
- Navegación de menús mediante `match` y funciones utilitarias


## 📁 Estructura del proyecto

```
trabajo_integrador/
├── main.py                       # Punto de entrada de la aplicación
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── db/
│   │   └── manager.py            # Conexión y creación de esquema SQLite3
│   ├── services/
│   │   └── products.py           # CRUD de productos y lógica de negocio
│   ├── ui/
│   │   ├── config.py             # Configuraciones generales del UI (constantes, columnas)
│   │   ├── decorators.py         # Estilos: centrado, boxed_text, headers
│   │   ├── form.py               # Entradas de datos con validación
│   │   ├── handler.py            # Controlador general del menú y flujo
│   │   ├── menu.py               # Menús y navegación
│   │   ├── message.py            # Mensajes con color y emojis (info, warning, error)
│   │   └── table.py              # Tabla formateada de productos
│   ├── utils/
│   │   ├── animation.py          # Animaciones de carga y efecto de salida
│   │   ├── close_app.py          # Cierre del programa con despedida
│   │   ├── mkdir.py              # Verifica y crea carpeta `data/`
│   │   └── random_farewell.py    # Mensajes de despedida aleatorios
├── data/
│   └── inventario.db             # Base de datos SQLite3 generada automáticamente
```



## 🧪 Ejemplo de uso


```
============================================================
                  📦 GESTIÓN DE PRODUCTOS 📦
============================================================
     Sistema de administración para productos de stock.
    Cargá, buscá, editá y eliminá productos fácilmente.
------------------------------------------------------------
····························································
·                      Menu Principal                      ·
····························································
          1. Agregar Producto
          2. Mostrar Productos
          3. Editar Producto
          4. Eliminar Producto (soft)
          5. Buscar Producto
          6. Salir
```

**Muestrar  los productos en una tabla**

```

+------+------------+----------------------+---------+----------+
\| id   |   name     |     description       | price   | quantity |
+------+------------+----------------------+---------+----------+
\|  1   |   abaco    | Abaco rojo artesa... |  800.0  |    2     |
+------+------------+----------------------+---------+----------+

```

## 🛠️ Tecnologías y librerías

- Python 3.11+
- SQLite3 (integrado)
- colorama (colores en terminal)
- Estructura modular y sin clases (funcional)
- Funciones decoradoras reutilizables
- Uso de `match` para navegación
- Buenas prácticas inspiradas en Angular (separación por módulo)



## 🧠 Conceptos clave aplicados

- Entrada del usuario validada (try/except)
- Separación clara de responsabilidades: UI, lógica, DB, utils, persistencia
- Diseño para terminal compacta (máximo 60 columnas)
- Funciones decoradoras reutilizables para estilo
- Documentación con Google-style docstrings
- Uso ético y educativo del conocimiento



## 🚧 Por mejorar (Backlog)

- Exportar a CSV productos activos
- Filtros por stock bajo o categoría
- Vista detallada de producto
- Buscador con regex
- Tests automatizados con `pytest`
- Script para popular datos de prueba



## 🧑‍💻 Autor

**Carlos Andres ALzate**, desarrollador autodidacta en formación.  
Apasionado por crear herramientas útiles, reutilizables y bien estructuradas.  
Interesado en programación fullstack, automatización, UX, juegos interactivos y bajo nivel.

---

## 📄 Licencia

~~Proyecto educativo bajo licencia MIT.~~



