"""
EDA - Análisis Exploratorio de Datos
Autor: Cristian Pineda
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List


class ExploratoryDataAnalysis:
    """
    Clase para realizar análisis exploratorio de datos.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa el análisis exploratorio.
        
        Args:
            df: DataFrame de pandas
        """
        self.df = df
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def generate_report(self) -> dict:
        """Genera un reporte completo del dataset."""
        report = {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'duplicates': self.df.duplicated().sum(),
            'memory_usage': self.df.memory_usage(deep=True).sum() / 1024**2,  # MB
        }
        
        print("=" * 60)
        print("📊 REPORTE DE ANÁLISIS EXPLORATORIO")
        print("=" * 60)
        print(f"\n📏 Dimensiones: {report['shape'][0]} filas x {report['shape'][1]} columnas")
        print(f"💾 Uso de memoria: {report['memory_usage']:.2f} MB")
        print(f"🔄 Duplicados: {report['duplicates']}")
        print(f"\n❌ Valores nulos por columna:")
        for col, nulls in report['missing_values'].items():
            if nulls > 0:
                pct = (nulls / len(self.df)) * 100
                print(f"   {col}: {nulls} ({pct:.2f}%)")
        
        print("\n📈 Estadísticas descriptivas:")
        print(self.df.describe())
        
        return report
    
    def plot_distributions(self, columns: Optional[List[str]] = None, save_path: Optional[str] = None):
        """
        Grafica distribuciones de variables numéricas.
        
        Args:
            columns: Lista de columnas (None = todas las numéricas)
            save_path: Ruta para guardar la imagen
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        n_cols = len(columns)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5 * n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(columns):
            sns.histplot(self.df[col], kde=True, ax=axes[idx], color='skyblue')
            axes[idx].set_title(f'Distribución de {col}')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frecuencia')
        
        # Ocultar ejes vacíos
        for idx in range(n_cols, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {save_path}")
        
        plt.show()
    
    def plot_correlations(self, save_path: Optional[str] = None):
        """
        Grafica matriz de correlación.
        
        Args:
            save_path: Ruta para guardar la imagen
        """
        numeric_df = self.df.select_dtypes(include=[np.number])
        
        if numeric_df.empty:
            print("⚠️ No hay columnas numéricas para calcular correlaciones")
            return
        
        plt.figure(figsize=(12, 10))
        correlation_matrix = numeric_df.corr()
        
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                    center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        
        plt.title('Matriz de Correlación', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {save_path}")
        
        plt.show()
    
    def plot_boxplots(self, columns: Optional[List[str]] = None, save_path: Optional[str] = None):
        """
        Grafica boxplots para detectar outliers.
        
        Args:
            columns: Lista de columnas (None = todas las numéricas)
            save_path: Ruta para guardar la imagen
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        n_cols = len(columns)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5 * n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(columns):
            sns.boxplot(y=self.df[col], ax=axes[idx], color='lightcoral')
            axes[idx].set_title(f'Boxplot de {col}')
            axes[idx].set_ylabel(col)
        
        # Ocultar ejes vacíos
        for idx in range(n_cols, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {save_path}")
        
        plt.show()
    
    def plot_categorical(self, columns: Optional[List[str]] = None, save_path: Optional[str] = None):
        """
        Grafica variables categóricas.
        
        Args:
            columns: Lista de columnas (None = todas las categóricas)
            save_path: Ruta para guardar la imagen
        """
        if columns is None:
            columns = self.df.select_dtypes(include=['object', 'category']).columns
        
        if len(columns) == 0:
            print("⚠️ No hay columnas categóricas para graficar")
            return
        
        n_cols = len(columns)
        n_rows = (n_cols + 1) // 2
        
        fig, axes = plt.subplots(n_rows, 2, figsize=(14, 5 * n_rows))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(columns):
            value_counts = self.df[col].value_counts()
            axes[idx].bar(range(len(value_counts)), value_counts.values, color='steelblue')
            axes[idx].set_xticks(range(len(value_counts)))
            axes[idx].set_xticklabels(value_counts.index, rotation=45, ha='right')
            axes[idx].set_title(f'Distribución de {col}')
            axes[idx].set_ylabel('Frecuencia')
        
        # Ocultar ejes vacíos
        for idx in range(n_cols, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 Gráfico guardado en: {save_path}")
        
        plt.show()


if __name__ == "__main__":
    print("📊 EDA - Análisis Exploratorio de Datos")
    print("Autor: Cristian Pineda")
