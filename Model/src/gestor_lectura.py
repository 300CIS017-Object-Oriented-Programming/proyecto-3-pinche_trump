class gestor_lectura:
    def __init__(self, archivo):
        self.archivo = archivo

    def obtener_indice_encabezados(self):
        index = self.archivo[self.archivo.iloc[:, 0] == "CÓDIGO DE LA INSTITUCIÓN"].index[0]
        return index

        
    def obtener_encabezados(self, index):
        header = self.archivo.iloc[index]
        return header

    def obtener_filas_filtro(self, columna_filtro, fila_filtro):
        filas_con_filtro = self.archivo[self.archivo[columna_filtro] == fila_filtro]
        if not filas_con_filtro.empty:
            return filas_con_filtro
        else:
            raise ValueError(f"No se encontraron filas con el filtro: {fila_filtro}")