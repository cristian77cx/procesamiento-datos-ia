"""
Data Cleaner - Módulo para limpieza de datos
Autor: Cristian Pineda
"""

import pandas as pd
import numpy as np
from typing import Optional, List


class DataCleaner:
    """
    Clase para limpiar y transformar datos.
    """
    
    def __init__(self, filepath: Optional[str] = None, df: Optional[pd.DataFrame] = None):
        """
        Inicializa el limpiador de datos.
        
        Args:
            filepath: Ruta al archivo CSV
            df: DataFrame de pandas (alternativa a filepath)
        """
        if filepath:
            self.df = pd.read_csv(filepath)
        elif df is not None:
            self.df = df.copy()
        else:
            raise ValueError("Debe proporcionar filepath o df")
        
        self.original_shape = self.df.shape
        self.cleaning_report = {}
    
    def remove_duplicates(self) -> 'DataCleaner':
        """Elimina filas duplicadas."""
        duplicates = self.df.duplicated().sum()
        self.df = self.df.drop_duplicates()
        self.cleaning_report['duplicates_removed'] = duplicates
        print(f"✅ Duplicados eliminados: {duplicates}")
        return self
    
    def handle_missing_values(self, strategy: str = 'drop', threshold: float = 0.5) -> 'DataCleaner':
        """
        Maneja valores nulos.
        
        Args:
            strategy: 'drop', 'mean', 'median', 'mode'
            threshold: Porcentaje máximo de nulos permitido por columna
        """
        missing_before = self.df.isnull().sum().sum()
        
        # Eliminar columnas con muchos nulos
        null_pct = self.df.isnull().sum() / len(self.df)
        cols_to_drop = null_pct[null_pct > threshold].index
        self.df = self.df.drop(columns=cols_to_drop)
        
        if strategy == 'drop':
            self.df = self.df.dropna()
        elif strategy == 'mean':
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
        elif strategy == 'median':
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        elif strategy == 'mode':
            for col in self.df.columns:
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
        
        missing_after = self.df.isnull().sum().sum()
        self.cleaning_report['missing_values_handled'] = missing_before - missing_after
        print(f"✅ Valores nulos manejados: {missing_before - missing_after}")
        return self
    
    def remove_outliers(self, columns: Optional[List[str]] = None, method: str = 'iqr') -> 'DataCleaner':
        """
        Elimina outliers usando IQR o Z-score.
        
        Args:
            columns: Lista de columnas a analizar (None = todas las numéricas)
            method: 'iqr' o 'zscore'
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        rows_before = len(self.df)
        
        if method == 'iqr':
            for col in columns:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
        
        elif method == 'zscore':
            from scipy import stats
            for col in columns:
                z_scores = np.abs(stats.zscore(self.df[col]))
                self.df = self.df[z_scores < 3]
        
        outliers_removed = rows_before - len(self.df)
        self.cleaning_report['outliers_removed'] = outliers_removed
        print(f"✅ Outliers eliminados: {outliers_removed}")
        return self
    
    def convert_dtypes(self) -> 'DataCleaner':
        """Convierte tipos de datos automáticamente."""
        # Convertir columnas de fecha
        for col in self.df.columns:
            if 'date' in col.lower() or 'fecha' in col.lower():
                try:
                    self.df[col] = pd.to_datetime(self.df[col])
                    print(f"✅ Columna '{col}' convertida a datetime")
                except:
                    pass
        
        # Convertir columnas categóricas
        for col in self.df.select_dtypes(include=['object']).columns:
            if self.df[col].nunique() < 10:
                self.df[col] = self.df[col].astype('category')
                print(f"✅ Columna '{col}' convertida a category")
        
        return self
    
    def clean(self, remove_duplicates: bool = True, 
              handle_missing: bool = True,
              remove_outliers: bool = False) -> pd.DataFrame:
        """
        Ejecuta el pipeline completo de limpieza.
        
        Args:
            remove_duplicates: Eliminar duplicados
            handle_missing: Manejar valores nulos
            remove_outliers: Eliminar outliers
        
        Returns:
            DataFrame limpio
        """
        print("🧹 Iniciando limpieza de datos...")
        print(f"📊 Shape original: {self.original_shape}")
        
        if remove_duplicates:
            self.remove_duplicates()
        
        if handle_missing:
            self.handle_missing_values()
        
        if remove_outliers:
            self.remove_outliers()
        
        self.convert_dtypes()
        
        print(f"📊 Shape final: {self.df.shape}")
        print("✅ Limpieza completada!")
        
        return self.df
    
    def save(self, filepath: str):
        """Guarda el DataFrame limpio."""
        self.df.to_csv(filepath, index=False)
        print(f"💾 Datos guardados en: {filepath}")
    
    def get_report(self) -> dict:
        """Retorna el reporte de limpieza."""
        return self.cleaning_report


if __name__ == "__main__":
    # Ejemplo de uso
    print("📊 Data Cleaner - Módulo de limpieza de datos")
    print("Autor: Cristian Pineda")
