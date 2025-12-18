# 🚚 Análisis de Performance Logística (End-to-End Project)

## 📋 Descripción
Este proyecto simula y analiza el ciclo de vida de envíos logísticos para identificar cuellos de botella en la distribución. Se construyó un pipeline completo de datos: desde la generación de datos sintéticos, pasando por el almacenamiento en base de datos relacional, hasta la visualización para toma de decisiones.

## 🛠️ Tecnologías Utilizadas
* **Python (Pandas, NumPy):** Generación y limpieza de datos (ETL).
* **SQL (PostgreSQL):** Modelado y almacenamiento de datos.
* **Power BI:** Dashboard interactivo y modelado de datos (DAX).

## 📊 Resultados Clave
El análisis reveló ineficiencias críticas en ciertos proveedores:
* Se identificó que **Correo Argentino** presenta una tasa de demora superior al **60%**.
* Se detectaron picos estacionales de retrasos en los meses de Agosto y Octubre.

## 📂 Estructura del Proyecto
* `generacion_datos.py`: Script de Python para generar el dataset y conectarse a SQL.
* `dashboard_logistica.pbix`: Archivo de Power BI con el tablero interactivo.
* `dataset.csv`: Muestra de los datos utilizados.

---
*Proyecto realizado por Henault Nicolas - 2025*
