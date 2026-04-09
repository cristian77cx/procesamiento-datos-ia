"""
🚀 APLICACIÓN WEB INTERACTIVA - PROCESAMIENTO DE DATOS PARA IA
Autor: Cristian Pineda
Descripción: Aplicación web donde los usuarios pueden subir sus datos y ver el procesamiento en tiempo real
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_cleaner import DataCleaner
from eda import ExploratoryDataAnalysis
from preprocessor import DataPreprocessor

# Configuración de la página
st.set_page_config(
    page_title="Procesamiento de Datos IA - Cristian Pineda",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(135deg, #4F8CFF, #22D3EE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #888;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, rgba(79,140,255,0.1), rgba(34,211,238,0.1));
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(79,140,255,0.3);
        margin: 0.5rem 0;
    }
    .success-box {
        background: rgba(34,211,238,0.1);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #22D3EE;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #4F8CFF, #22D3EE);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(79,140,255,0.4);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📊 Procesamiento de Datos para IA</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sube tu archivo CSV o Excel y observa el procesamiento automático en tiempo real</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/data-configuration.png", width=80)
    st.title("⚙️ Configuración")
    
    st.markdown("### 👨‍💻 Desarrollador")
    st.markdown("**Cristian Pineda**")
    st.markdown("Analista de Datos Junior")
    st.markdown("📧 pinedandres002@gmail.com")
    st.markdown("🔗 [GitHub](https://github.com/cristian77cx)")
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/cristian-pineda)")
    
    st.markdown("---")
    st.markdown("### 🎯 Opciones de Limpieza")
    remove_duplicates = st.checkbox("Eliminar duplicados", value=True)
    handle_missing = st.checkbox("Manejar valores nulos", value=True)
    remove_outliers = st.checkbox("Eliminar outliers", value=True)
    
    st.markdown("---")
    st.markdown("### 📊 Opciones de Preprocesamiento")
    scaling_method = st.selectbox(
        "Método de escalado",
        ["standard", "minmax", "robust"]
    )
    
    st.markdown("---")
    st.markdown("### 💡 Instrucciones")
    st.info("""
    1. Sube un archivo CSV o Excel
    2. Revisa el análisis automático
    3. Descarga los datos procesados
    4. ¡Listo para Machine Learning!
    """)

# Función para crear datos de ejemplo
def create_sample_data():
    np.random.seed(42)
    n = 1000
    
    data = {
        'edad': np.random.randint(18, 70, n),
        'salario': np.random.normal(50000, 15000, n),
        'experiencia': np.random.randint(0, 30, n),
        'educacion': np.random.choice(['Secundaria', 'Universidad', 'Posgrado'], n),
        'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla'], n),
        'satisfaccion': np.random.randint(1, 11, n)
    }
    
    df = pd.DataFrame(data)
    
    # Agregar algunos valores nulos y duplicados
    df.loc[np.random.choice(df.index, 50), 'salario'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'experiencia'] = np.nan
    df = pd.concat([df, df.iloc[:20]], ignore_index=True)
    
    return df

# Tabs principales
tab1, tab2, tab3, tab4 = st.tabs(["📁 Cargar Datos", "🧹 Limpieza", "📊 Análisis", "🤖 ML Prep"])

with tab1:
    st.header("📁 Carga de Datos")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Arrastra tu archivo aquí o haz clic para seleccionar",
            type=['csv', 'xlsx', 'xls'],
            help="Formatos soportados: CSV, Excel (.xlsx, .xls)"
        )
    
    with col2:
        st.markdown("### 🎲 ¿No tienes datos?")
        if st.button("🎯 Generar Datos de Ejemplo"):
            st.session_state['df_original'] = create_sample_data()
            st.success("✅ Datos de ejemplo generados!")
            st.balloons()
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.session_state['df_original'] = df
            st.success(f"✅ Archivo cargado exitosamente: {uploaded_file.name}")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")
    
    if 'df_original' in st.session_state:
        df = st.session_state['df_original']
        
        st.markdown("### 📋 Vista Previa de los Datos")
        st.dataframe(df.head(10), use_container_width=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📏 Filas", f"{df.shape[0]:,}")
        with col2:
            st.metric("📊 Columnas", df.shape[1])
        with col3:
            st.metric("💾 Tamaño", f"{df.memory_usage(deep=True).sum() / 1024:.2f} KB")
        with col4:
            st.metric("❌ Nulos", f"{df.isnull().sum().sum():,}")

with tab2:
    st.header("🧹 Limpieza de Datos")
    
    if 'df_original' not in st.session_state:
        st.warning("⚠️ Por favor, carga un archivo primero en la pestaña 'Cargar Datos'")
    else:
        df = st.session_state['df_original'].copy()
        
        st.markdown("### 📊 Estado Inicial")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Duplicados", f"{df.duplicated().sum():,}")
        with col2:
            st.metric("Valores Nulos", f"{df.isnull().sum().sum():,}")
        with col3:
            st.metric("Filas Totales", f"{len(df):,}")
        
        if st.button("🚀 Iniciar Limpieza Automática"):
            with st.spinner("🔄 Procesando datos..."):
                cleaner = DataCleaner(df)
                df_clean = cleaner.clean(
                    remove_duplicates=remove_duplicates,
                    handle_missing=handle_missing,
                    remove_outliers=remove_outliers
                )
                
                st.session_state['df_clean'] = df_clean
                st.session_state['cleaning_report'] = cleaner.get_cleaning_report()
                
                st.success("✅ ¡Limpieza completada exitosamente!")
                st.balloons()
        
        if 'df_clean' in st.session_state:
            df_clean = st.session_state['df_clean']
            report = st.session_state['cleaning_report']
            
            st.markdown("### ✨ Resultados de la Limpieza")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(
                    "Duplicados Eliminados",
                    report.get('duplicates_removed', 0),
                    delta=f"-{report.get('duplicates_removed', 0)}"
                )
            with col2:
                st.metric(
                    "Nulos Manejados",
                    report.get('missing_values_handled', 0),
                    delta=f"-{report.get('missing_values_handled', 0)}"
                )
            with col3:
                st.metric(
                    "Outliers Removidos",
                    report.get('outliers_removed', 0),
                    delta=f"-{report.get('outliers_removed', 0)}"
                )
            with col4:
                reduction = ((len(df) - len(df_clean)) / len(df) * 100)
                st.metric(
                    "Reducción",
                    f"{reduction:.1f}%",
                    delta=f"-{len(df) - len(df_clean)} filas"
                )
            
            st.markdown("### 📋 Datos Limpios")
            st.dataframe(df_clean.head(10), use_container_width=True)
            
            # Botón de descarga
            csv = df_clean.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Descargar Datos Limpios (CSV)",
                data=csv,
                file_name="datos_limpios.csv",
                mime="text/csv",
            )

with tab3:
    st.header("📊 Análisis Exploratorio de Datos")
    
    if 'df_clean' not in st.session_state:
        st.warning("⚠️ Por favor, limpia los datos primero en la pestaña 'Limpieza'")
    else:
        df_clean = st.session_state['df_clean']
        
        eda = ExploratoryDataAnalysis(df_clean)
        
        st.markdown("### 📈 Estadísticas Descriptivas")
        st.dataframe(df_clean.describe(), use_container_width=True)
        
        # Seleccionar columnas numéricas
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) > 0:
            st.markdown("### 📊 Visualizaciones")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Distribuciones")
                selected_cols = st.multiselect(
                    "Selecciona columnas para visualizar",
                    numeric_cols,
                    default=numeric_cols[:3] if len(numeric_cols) >= 3 else numeric_cols
                )
                
                if selected_cols:
                    fig = eda.plot_distributions(selected_cols)
                    st.pyplot(fig)
            
            with col2:
                st.markdown("#### Matriz de Correlación")
                fig = eda.plot_correlations()
                st.pyplot(fig)
            
            st.markdown("#### Boxplots - Detección de Outliers")
            if selected_cols:
                fig = eda.plot_boxplots(selected_cols)
                st.pyplot(fig)
        
        # Columnas categóricas
        cat_cols = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()
        if len(cat_cols) > 0:
            st.markdown("#### Variables Categóricas")
            fig = eda.plot_categorical()
            st.pyplot(fig)

with tab4:
    st.header("🤖 Preparación para Machine Learning")
    
    if 'df_clean' not in st.session_state:
        st.warning("⚠️ Por favor, limpia los datos primero en la pestaña 'Limpieza'")
    else:
        df_clean = st.session_state['df_clean'].copy()
        
        st.markdown("### ⚙️ Preprocesamiento Automático")
        
        if st.button("🚀 Preparar Datos para ML"):
            with st.spinner("🔄 Preparando datos..."):
                preprocessor = DataPreprocessor(df_clean)
                
                # Codificar categóricas
                preprocessor.encode_categorical()
                
                # Escalar features
                preprocessor.scale_features(method=scaling_method)
                
                # Dividir datos
                X_train, X_test, y_train, y_test = preprocessor.split_data(test_size=0.2)
                
                st.session_state['X_train'] = X_train
                st.session_state['X_test'] = X_test
                st.session_state['preprocessor'] = preprocessor
                
                st.success("✅ ¡Datos preparados para Machine Learning!")
                st.balloons()
        
        if 'X_train' in st.session_state:
            X_train = st.session_state['X_train']
            X_test = st.session_state['X_test']
            
            st.markdown("### ✨ Resultados del Preprocesamiento")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🎯 Train Set", f"{X_train.shape[0]:,} filas")
            with col2:
                st.metric("🧪 Test Set", f"{X_test.shape[0]:,} filas")
            with col3:
                st.metric("📊 Features", X_train.shape[1])
            
            st.markdown("### 📋 Vista Previa - Train Set")
            st.dataframe(pd.DataFrame(X_train).head(10), use_container_width=True)
            
            st.markdown("### 📋 Vista Previa - Test Set")
            st.dataframe(pd.DataFrame(X_test).head(10), use_container_width=True)
            
            # Descargar datos procesados
            col1, col2 = st.columns(2)
            with col1:
                train_csv = pd.DataFrame(X_train).to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="⬇️ Descargar Train Set",
                    data=train_csv,
                    file_name="train_set.csv",
                    mime="text/csv",
                )
            with col2:
                test_csv = pd.DataFrame(X_test).to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="⬇️ Descargar Test Set",
                    data=test_csv,
                    file_name="test_set.csv",
                    mime="text/csv",
                )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 2rem;'>
    <p><strong>Desarrollado por Cristian Pineda</strong></p>
    <p>Analista de Datos Junior | Especializado en Procesamiento de Datos para IA</p>
    <p>📧 pinedandres002@gmail.com | 🔗 <a href='https://github.com/cristian77cx'>GitHub</a> | 🔗 <a href='https://linkedin.com/in/cristian-pineda'>LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)
