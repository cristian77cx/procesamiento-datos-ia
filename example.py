"""
Ejemplo de uso del sistema de procesamiento de datos
Autor: Cristian Pineda
"""

import pandas as pd
import numpy as np
from src.data_cleaner import DataCleaner
from src.eda import ExploratoryDataAnalysis
from src.preprocessor import DataPreprocessor


def create_sample_dataset():
    """Crea un dataset de ejemplo para demostración."""
    np.random.seed(42)
    
    n_samples = 1000
    
    data = {
        'edad': np.random.randint(18, 70, n_samples),
        'salario': np.random.normal(50000, 15000, n_samples),
        'experiencia': np.random.randint(0, 30, n_samples),
        'educacion': np.random.choice(['Bachiller', 'Técnico', 'Universitario', 'Posgrado'], n_samples),
        'ciudad': np.random.choice(['Cali', 'Bogotá', 'Medellín', 'Yumbo'], n_samples),
        'satisfaccion': np.random.randint(1, 11, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Agregar algunos valores nulos
    df.loc[np.random.choice(df.index, 50), 'salario'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'experiencia'] = np.nan
    
    # Agregar algunos duplicados
    df = pd.concat([df, df.iloc[:20]], ignore_index=True)
    
    # Agregar algunos outliers
    df.loc[np.random.choice(df.index, 10), 'salario'] = np.random.uniform(200000, 300000, 10)
    
    return df


def main():
    """Función principal de demostración."""
    print("=" * 70)
    print("📊 SISTEMA DE PROCESAMIENTO DE DATOS PARA IA")
    print("Autor: Cristian Pineda")
    print("=" * 70)
    
    # 1. Crear dataset de ejemplo
    print("\n1️⃣ Creando dataset de ejemplo...")
    df = create_sample_dataset()
    print(f"✅ Dataset creado: {df.shape}")
    
    # 2. Limpieza de datos
    print("\n2️⃣ LIMPIEZA DE DATOS")
    print("-" * 70)
    cleaner = DataCleaner(df=df)
    df_clean = cleaner.clean(
        remove_duplicates=True,
        handle_missing=True,
        remove_outliers=True
    )
    
    # 3. Análisis Exploratorio
    print("\n3️⃣ ANÁLISIS EXPLORATORIO")
    print("-" * 70)
    eda = ExploratoryDataAnalysis(df_clean)
    report = eda.generate_report()
    
    # 4. Visualizaciones
    print("\n4️⃣ GENERANDO VISUALIZACIONES")
    print("-" * 70)
    print("📊 Generando gráficos de distribución...")
    eda.plot_distributions(columns=['edad', 'salario', 'experiencia'])
    
    print("📊 Generando matriz de correlación...")
    eda.plot_correlations()
    
    print("📊 Generando boxplots...")
    eda.plot_boxplots(columns=['edad', 'salario', 'experiencia'])
    
    print("📊 Generando gráficos categóricos...")
    eda.plot_categorical()
    
    # 5. Preprocesamiento para ML
    print("\n5️⃣ PREPROCESAMIENTO PARA MACHINE LEARNING")
    print("-" * 70)
    preprocessor = DataPreprocessor(df_clean)
    preprocessor.encode_categorical()
    preprocessor.scale_features(columns=['edad', 'salario', 'experiencia'])
    
    X_train, X_test, y_train, y_test = preprocessor.prepare_for_ml(
        target_column='satisfaccion',
        test_size=0.2
    )
    
    # 6. Resumen final
    print("\n6️⃣ RESUMEN FINAL")
    print("=" * 70)
    print(f"✅ Datos originales: {df.shape}")
    print(f"✅ Datos limpios: {df_clean.shape}")
    print(f"✅ Train set: {X_train.shape}")
    print(f"✅ Test set: {X_test.shape}")
    print(f"\n📊 Reporte de limpieza:")
    for key, value in cleaner.get_report().items():
        print(f"   {key}: {value}")
    
    print("\n✅ ¡Procesamiento completado exitosamente!")
    print("=" * 70)


if __name__ == "__main__":
    main()
