class gestor_metricas:
    def __init__(self, archivo) -> None:
        self.archivo = archivo
    
    def obtener_metricas_strings(self, filtro):
        try:
            if self.archivo[filtro].dtype == "object":
                conteo = self.archivo[filtro].value_counts().to_dict()
                return conteo
        except KeyError as e:
            raise ValueError(f"Error al obtener la suma de la columna {filtro}: {e}")
        except Exception as e:
            raise ValueError(f"Error al obtener la suma de la columna {filtro}: {e}")
        
    def consolidado(self):
        columnas_unicas = ["CÓDIGO DE LA INSTITUCIÓN", "IES_PADRE", "ID SECTOR IES"
                           "ID CARACTER", "CÓDIGO DEL DEPARTAMENTO (IES)", "CÓDIGO DEL MUNICIPIO IES"
                           "CÓDIGO SNIES DEL PROGRAMA", "ID NIVEL ACADÉMICO", "ID NIVEL DE FORMACIÓN"
                           "ID METODOLOGÍA", "ID ÁREA", "ID NÚCLEO", "ID CINE CAMPO AMPLIO", "ID CINE CAMPO ESPECIFICO",
                           "ID CINE CODIGO DETALLADO", "CÓDIGO DEL DEPARTAMENTO (PROGRAMA)", "CÓDIGO DEL MUNICIPIO (PROGRAMA)",
                           "ID SEXO", "AÑO", "SEMESTRE"]
        df_consolidado = self.archivo.groupby(columnas_unicas).sum(numeric_only=True).reset_index()
        return df_consolidado


        

