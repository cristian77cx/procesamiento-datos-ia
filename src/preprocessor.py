"""
Data Preprocessor - Preprocesamiento para Machine Learning
Autor: Cristian Pineda
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from typing import Tuple, Optional, List


class DataPreprocessor:
    """
    Clase para preprocesar datos para Machine Learning.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa el preprocesador.
        
        Args:
            df: DataFrame de pandas
        """
        self.df = df.copy()
        self.scalers = {}
        self.encoders = {}
    
    def encode_categorical(self, columns: Optional[List[str]] = None) -> 'DataPreprocessor':
        """
        Codifica variables categóricas.
        
        Args:
            columns: Lista de columnas (None = todas las categóricas)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=['object', 'category']).columns
        
        for col in columns:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col].astype(str))
            self.encoders[col] = le
            print(f"✅ Columna '{col}' codificada")
        
        return self
    
    def scale_features(self, columns: Optional[List[str]] = None, 
                      method: str = 'standard') -> 'DataPreprocessor':
        """
        Escala variables numéricas.
        
        Args:
            columns: Lista de columnas (None = todas las numéricas)
            method: 'standard' o 'minmax'
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        else:
            raise ValueError("method debe ser 'standard' o 'minmax'")
        
        self.df[columns] = scaler.fit_transform(self.df[columns])
        self.scalers['features'] = scaler
        print(f"✅ Features escaladas con {method}")
        
        return self
    
    def prepare_for_ml(self, target_column: str, test_size: float = 0.2, 
                      random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Prepara datos para Machine Learning.
        
        Args:
            target_column: Nombre de la columna objetivo
            test_size: Proporción del conjunto de prueba
            random_state: Semilla aleatoria
        
        Returns:
            X_train, X_test, y_train, y_test
        """
        # Separar features y target
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        
        # Dividir en train y test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        print(f"✅ Datos divididos:")
        print(f"   Train: {X_train.shape}")
        print(f"   Test: {X_test.shape}")
        
        return X_train, X_test, y_train, y_test
    
    def get_processed_data(self) -> pd.DataFrame:
        """Retorna el DataFrame procesado."""
        return self.df


if __name__ == "__main__":
    print("🔧 Data Preprocessor - Preprocesamiento para ML")
    print("Autor: Cristian Pineda")
