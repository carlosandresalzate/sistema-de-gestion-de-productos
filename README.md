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

trabajo\_integrador/
├── app/
│   ├── db/
│   │   └── manager.py            # Conexión y creación de esquema SQLite3
│   ├── services/
│   │   └── products.py           # CRUD de productos y lógica de negocio
│   ├── ui/
│   │   ├── menu.py               # Menús, entradas y navegación
│   │   ├── table.py              # Tabla con productos (formato fijo y truncado)
│   │   ├── message.py            # Colores y mensajes con emojis (info, error, etc.)
│   │   ├── handler.py            # Coordinador de menús y acciones
│   │   └── decorators.py         # Estilo de impresión: centrado, boxed, headers
│   ├── utils/
│   │   ├── close\_app.py          # Cierre con mensaje y manejo de errores
│   │   ├── random\_farewell.py    # Mensajes de despedida aleatorios
│   │   └── mkdir.py              # Inicialización de carpetas y rutas
├── data/
│   └── inventario.db             # Base de datos SQLite3 (auto creada)
├── requirements.txt
└── main.py                       # Punto de entrada

```



## 🧪 Ejemplo de uso

```

==========================
📦 GESTIÓN DE PRODUCTOS 📦
==========================

```
Sistema de administración para productos de stock.
Cargá, buscá, editá y eliminá productos fácilmente.

```

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

**Mostrar productos**

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
- Uso de `match` para navegación
- Buenas prácticas inspiradas en Angular (separación por módulo)



## 🧠 Conceptos clave aplicados

- Entrada del usuario validada (try/except)
- Separación UI / lógica / persistencia
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



