# Manual Técnico: Sistema de Análisis de Datos del SNIES

## 1. Descripción General

El sistema Nacional de Información de la Educación Superior (SNIES) en Colombia recopila una gran cantidad de datos 
sobre lo que son las instituciones de educación superior y los programas académicos que ofrece. Este proyecto permite 
analizar datos relacionados con la inscripción, admisión y graduación, ayudando en la toma de decisiones en lo que 
concierne al ambito educativo

## 2. Requisitos del Sistema

### 2.1 Hardware

- CPU: Procesador Intel o AMD de 2 GHZ.
- RAM: 4 GB o más
- Almacenamiento: 10 GB de espacio libre
- Sistema Operativo: windows 10, windos 11,  linux

### 2.2 Software

- Python 3.8 o superior.
- Librerías de Python: **streamlit, pandas**
- Entorno de desarrollo (Opcional): Visual Studio Code o PyCharm

## 3. Estructura del Proyecto

### 3.1 Directorios y Archivos

- **docs/inputs/**: Carpeta que contiene los archivos **xlsx** para el análisis
- **Model/**: Carpeta que contiene los archivos base del programa

## 3.2. Configuración del Entorno

1. Clonar el repositorio
![Clonamos el Repositorio](./assets/clone.png)

2. Instalar las dependencias
![Instalamos las dependencias necesarias](./assets/dependencias.png)

## 4. Carga de Información

### 4.1 Descripción

### 4.2 Código de Carga de Arhivos

***INSERTE CÓDIGO AQUÍ***

## 5. Filtrado de Información

### 5.1 Busqueda por palabras claves

Los usuarios podrán ingresar palabras clave para identificar programas académicos relevantes

### 5.2 Código de filtrado

***INSERTE CÓDIGO AQUÍ***

## 6 Procesamiento de Datos

### 6.1 Descripción

El sistema procesará los datos para calcular, por cada programa y año:

- **Estudiantes inscritos**
- **Estudiantes graduados**
- **Estudiantes matriculados**
- **Estudiantes admitidos**
- **Estudiantes matriculados por primera vez**

### 6.2 Código de Procesamiento

***INSERTE CÓDIGO AQUÍ***

## Conlusión

Este manual técnico proporciona una guía detallada para el desarrollo e implementación de una aplicación web interactiva
utilizando Streamlit para el análisis de datos del SNIES. Se describen los pasos necesarios para la carga, filtrado y
procesamiento de la información, lo que permite asegurar que el sistema sea fácil de usar y altamente funcional
