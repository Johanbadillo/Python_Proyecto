<div align="center">

# Simulador de Gastos Diarios  
**Controla tus finanzas con Python**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Tabulate](https://img.shields.io/badge/Tabulate-4EA94B?style=for-the-badge&logo=table&logoColor=white)

---

**JOHAN MONSALVE**  

![CampusLands • Cajasan 2025](https://img.shields.io/badge/CampusLands_%E2%80%A2_Cajasan_2025-FD7E14?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxIiBoZWlnaHQ9IjEiPjwvc3ZnPg==&labelColor=E65100)
![ruta](https://img.shields.io/badge/RUTA-Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)

</div>

---

## Descripción del Proyecto

**Simulador de Gastos Diarios** es una **herramienta en consola** desarrollada en **Python** que permite:

- Registrar gastos diarios con categoría, monto y fecha  
- Filtrar por **período de tiempo** (día, semana, mes)  
- Calcular totales automáticos  
- Generar **reportes detallados** y **guardarlos en archivos**  
- Visualizar datos en **tablas claras** con `tabulate`  

> **Datos persistentes en `gastos.json`** – ¡Nunca pierdas tu historial!

---

## Funcionalidades

| Función | Descripción |
|--------|-----------|
| **Registrar gasto** | Ingresa monto, categoría y fecha |
| **Ver gastos** | Filtra por día, semana o mes |
| **Calcular totales** | Suma por período o categoría |
| **Generar reporte** | Exporta en `.txt` con formato limpio |
| **Menú interactivo** | Navegación fácil en consola |

```mermaid
graph TD
    A[Menú Principal] --> B[Registrar Gasto]
    A --> C[Ver Gastos]
    A --> D[Calcular Totales]
    A --> E[Generar Reporte]
    A --> F[Salir]
```

# 🛠️ Tecnologías Usadas

| Tecnología     | Uso                              |
|----------------|----------------------------------|
| **Python 3**         | Lógica principal y estructura          |
| **JSON**      | Almacenamiento persistente de datos          |
| **Tabulate**     | Tablas visuales en consola         |
| **Datetime**     | Manejo de fechas y períodos        |

## ⚙️ Instalación y Uso

Sigue estos pasos para ejecutar el proyecto localmente🧑‍💻👇:

```bash
# 1. Instalar dependencia
pip install tabulate

# 2. Clonar el repositorio
git clone https://github.com/Johanbadillo/Python_Proyecto.git

# 3. Entrar al directorio
cd Python_Proyecto

# 4. Ejecutar el programa
python proyecto.py
```

## 📁 Estructura del proyecto
```
📁 Python_Proyecto/
├── 📁 Data/
│   ├── data.json
│   └── dataReportes.json
├── 📁 Funciones/
│   ├── funciones.py
│   ├── funcionesJson.py
│   └── funcionesMensajes.py
├── proyecto.py
├── LICENSE
└── README.md
```

## Video Explicativo
<div align="center">
 
[Video de Demostración](https://www.youtube.com/watch?v=cRWHBtwMylU)

</div>
