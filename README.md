# Manual Técnico: Sistema de Análisis de Datos del SNIES

# LINK DE LA APP https://proyecto-3-pinchetrump-uvteneml9guwk9nbyprjr6.streamlit.app/

## 1. Descripción General

El sistema Nacional de Información de la Educación Superior (SNIES) en Colombia recopila una gran cantidad de datos
sobre lo que son las instituciones de educación superior y los programas académicos que ofrece. Este proyecto permite
analizar datos relacionados con la inscripción, admisión y graduación, ayudando en la toma de decisiones en lo que
concierne al ambito educativo en el presebte documento obtendra detalles sobre a implementacion de as caracteristicas
principales en caso de que desee modificarlo o implementar su propia version

## 2. Estructura del Proyecto

### 2.1 Directorios y Archivos

- **docs/inputs/**: Carpeta que contiene los archivos **xlsx** para el análisis
- **Model/**: Carpeta que contiene los archivos base del programa

## 3. Configuración del Entorno

1. Clonar el repositorio

![Clonamos el Repositorio](./assets/clone.png)

3. Instalar las dependencias

![Instalamos las dependencias necesarias](./assets/dependencias.png)

## 4. Carga de Información

### 4.1 Descripción
Utilizamos funciones de las librerias Streamlit y Os para que el usuario pueda cargar sus propios archivos (Siempre y cuando cumplan con e formato previsto)
### 4.2 Código de Carga de Arhivos

![Code](./assets/CargadoDeArchivos.png)
## 5. Filtrado de Información

### 5.1 Busqueda por palabras claves

Los usuarios podrán elegir una columna y en ella a traves de un menu despegable con funcion de busqueda y autocompleto podran filtrar a traves de palabras clave.
### 5.2 Código de filtrado

![Code](./assets/AplicadoFiltros.png)

## 6 Procesamiento de Datos

### 6.1 Descripción

El sistema procesará los datos para calcular, por cada programa y año los datos provinientes de:

- **Estudiantes inscritos**
- **Estudiantes graduados**
- **Estudiantes matriculados**
- **Estudiantes admitidos**
- **Estudiantes matriculados por primera vez**

### 6.2 Código de Procesamiento

![Code](./assets/ProcesarData.png)

### Fin manual tecnico


# UML
```mermaid
classDiagram
    class gestor_lectura {
        -archivo
        +__init__(archivo=None)
        +obtener_indice_encabezados()
        +obtener_encabezados(index)
        +obtener_filas_filtro(columna_filtro, fila_filtro)
        +obtener_archivos_rango(rango, categoria, base_path)
        +columna_numerica(filtro_columna)
        +columna_string(filtro_columna)
        +obtener_columna(filtro_columna)
    }

    class gestor_escritura {
        -archivo
        +__init__(archivo)
        +guardar_excel(nombre_archivo)
        +guardar_json(nombre_archivo)
        +guardar_csv(nombre_archivo)
    }

    class gestor_metricas {
        -archivo
        +__init__(archivo)
        +obtener_metricas(filtro)
        +consolidado()
        +agrupamiento(columna1, columna2)
    }

    class Utility {
        +html_code()
        +html_code2()
        +html_code3()
        +save_coments(comentarios, persona, coment)
        +coments(comentarios)
    }

    class analisis_utility {
        +charge_file(uploadedfile)
        +show_files()
        +charge_new_file()
    }

    class menus_secundarios_informacion {
        +cargar_datos(archivos)
        +corregir_tipo(archivo)
        +obtener_valores_sin_repeticion(columna, archivo)
        +boton_volver()
        +boton_descargar()
        +boton_estadisticas()
        +boton_ver_informacion()
        +menu_seleccion_filtro()
        +opciones_filtros(lector, filtro)
    }

    class menu_filtros {
        +opcion_caja_seleccion(filtro)
        +opcion_entrada_texto()
    }

    class menu_estadisticas {
        +boton_volver_categoria()
        +obtener_grafico()
        +generar_grafico_barras(archivo, categoria, columna)
    }


    class menu_ver_informacion {
        +boton_volver_categoria()
        +menu_ver_informacion()
    }

    class menu_descargas {
        +menu_descargas()
        +boton_volver_categoria()
        +boton_descargar(opcion, escritor)
    }
Utility --> App
gestor_escritura --> menu_descargas
gestor_lectura --> menu_descargas
gestor_lectura --> menu_ver_informacion
gestor_lectura --> menu_estadisticas
gestor_lectura --> menus_secundarios_informacion
gestor_metricas --> menu_estadisticas
menu_filtros --> menus_secundarios_informacion
analisis_utility --> analisis_de_datos_page
```





## Conlusión

Este manual técnico proporciona una guía detallada para el desarrollo e implementación de una aplicación web interactiva
utilizando Streamlit para el análisis de datos del SNIES. Se describen los pasos necesarios para la carga, filtrado y
procesamiento de la información, lo que permite asegurar que el sistema sea fácil de usar y altamente funcional





