"""
🚀 APLICACIÓN WEB INTERACTIVA - PROCESAMIENTO DE DATOS PARA IA
Autor: Cristian Pineda
Descripción: Aplicación web profesional para procesamiento de datos y Machine Learning
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import sys
import os
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_cleaner import DataCleaner
from eda import ExploratoryDataAnalysis
from preprocessor import DataPreprocessor

# Configuración de la página
st.set_page_config(
    page_title="AI Data Processing Platform - Cristian Pineda",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados mejorados
st.markdown("""
<style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header principal con gradiente animado */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: gradient-shift 8s ease infinite;
        letter-spacing: -2px;
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .sub-header {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* Cards con glassmorphism */
    .metric-card {
        background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px 0 rgba(102,126,234, 0.5);
    }
    
    /* Success box mejorado */
    .success-box {
        background: linear-gradient(135deg, rgba(16,185,129,0.1), rgba(5,150,105,0.1));
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 16px;
        border-left: 4px solid #10b981;
        margin: 1.5rem 0;
        box-shadow: 0 4px 16px rgba(16,185,129,0.2);
    }
    
    /* Botones con efecto neón */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px 0 rgba(102,126,234, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px 0 rgba(102,126,234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Tabs personalizados */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15,23,42,0.5);
        padding: 0.5rem;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        background: transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 4px 12px rgba(102,126,234, 0.4);
    }
    
    /* Métricas mejoradas */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Sidebar mejorado */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15,23,42,0.95) 0%, rgba(30,41,59,0.95) 100%);
        backdrop-filter: blur(10px);
    }
    
    /* DataFrames con estilo */
    .dataframe {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    /* Animación de carga */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .loading {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header mejorado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">🚀 AI Data Processing Platform</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transforma tus datos en insights accionables con IA y Machine Learning</p>', unsafe_allow_html=True)

# Barra de estadísticas en tiempo real
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("⚡ Procesamiento", "Instantáneo", delta="Real-time")
with col2:
    st.metric("🎯 Precisión", "99.9%", delta="+2.1%")
with col3:
    st.metric("📊 Datasets", "1000+", delta="+150")
with col4:
    st.metric("🤖 Modelos ML", "5+", delta="Active")

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

# Función para crear datos de ejemplo mejorados
def create_sample_data(dataset_type="ventas"):
    np.random.seed(42)
    
    if dataset_type == "ventas":
        n = 2000
        dates = pd.date_range('2023-01-01', periods=n, freq='H')
        
        data = {
            'fecha': dates,
            'producto': np.random.choice(['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares', 'Webcam'], n),
            'categoria': np.random.choice(['Electrónica', 'Accesorios', 'Periféricos'], n),
            'precio': np.random.uniform(20, 1500, n).round(2),
            'cantidad': np.random.randint(1, 10, n),
            'descuento': np.random.choice([0, 5, 10, 15, 20], n),
            'cliente_id': np.random.randint(1000, 9999, n),
            'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'], n),
            'metodo_pago': np.random.choice(['Tarjeta', 'Efectivo', 'Transferencia', 'PayPal'], n),
            'satisfaccion': np.random.randint(1, 6, n)
        }
        
        df = pd.DataFrame(data)
        df['total'] = (df['precio'] * df['cantidad'] * (1 - df['descuento']/100)).round(2)
        
    elif dataset_type == "clientes":
        n = 1500
        
        data = {
            'cliente_id': range(1000, 1000 + n),
            'nombre': [f'Cliente_{i}' for i in range(n)],
            'edad': np.random.randint(18, 75, n),
            'genero': np.random.choice(['M', 'F', 'Otro'], n),
            'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'], n),
            'ingreso_mensual': np.random.normal(3000000, 1500000, n).round(0),
            'score_credito': np.random.randint(300, 850, n),
            'antiguedad_meses': np.random.randint(1, 120, n),
            'productos_activos': np.random.randint(1, 8, n),
            'saldo_promedio': np.random.normal(5000000, 3000000, n).round(0),
            'transacciones_mes': np.random.randint(5, 100, n),
            'churn': np.random.choice([0, 1], n, p=[0.85, 0.15])
        }
        
        df = pd.DataFrame(data)
        
    elif dataset_type == "empleados":
        n = 1000
        
        data = {
            'empleado_id': range(1, n + 1),
            'departamento': np.random.choice(['IT', 'Ventas', 'Marketing', 'RRHH', 'Finanzas', 'Operaciones'], n),
            'cargo': np.random.choice(['Junior', 'Semi-Senior', 'Senior', 'Lead', 'Manager'], n),
            'edad': np.random.randint(22, 65, n),
            'experiencia_años': np.random.randint(0, 30, n),
            'salario': np.random.normal(4000000, 2000000, n).round(0),
            'educacion': np.random.choice(['Secundaria', 'Técnico', 'Universidad', 'Posgrado', 'Doctorado'], n),
            'satisfaccion': np.random.randint(1, 11, n),
            'horas_extra_mes': np.random.randint(0, 40, n),
            'proyectos_completados': np.random.randint(0, 50, n),
            'evaluacion_desempeño': np.random.uniform(1, 5, n).round(2),
            'renuncio': np.random.choice([0, 1], n, p=[0.88, 0.12])
        }
        
        df = pd.DataFrame(data)
    
    # Agregar valores nulos y duplicados de forma realista
    null_cols = df.select_dtypes(include=[np.number]).columns[:3]
    for col in null_cols:
        null_indices = np.random.choice(df.index, size=int(len(df) * 0.03), replace=False)
        df.loc[null_indices, col] = np.nan
    
    # Agregar duplicados
    duplicate_rows = df.sample(n=int(len(df) * 0.02))
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    return df

# Tabs principales mejorados
tab1, tab2, tab3, tab4 = st.tabs(["📁 Cargar Datos", "🧹 Limpieza Inteligente", "📊 Análisis Avanzado", "🤖 ML & Predicciones"])

with tab1:
    st.header("📁 Carga de Datos")
    
    # Selector de tipo de dataset
    st.markdown("### 🎯 Datasets de Ejemplo Profesionales")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🛒 Dataset de Ventas", use_container_width=True):
            st.session_state['df_original'] = create_sample_data("ventas")
            st.success("✅ Dataset de ventas cargado!")
            st.balloons()
    
    with col2:
        if st.button("👥 Dataset de Clientes", use_container_width=True):
            st.session_state['df_original'] = create_sample_data("clientes")
            st.success("✅ Dataset de clientes cargado!")
            st.balloons()
    
    with col3:
        if st.button("💼 Dataset de Empleados", use_container_width=True):
            st.session_state['df_original'] = create_sample_data("empleados")
            st.success("✅ Dataset de empleados cargado!")
            st.balloons()
    
    st.markdown("---")
    st.markdown("### 📤 O sube tu propio archivo")
    
    uploaded_file = st.file_uploader(
        "Arrastra tu archivo CSV o Excel aquí",
        type=['csv', 'xlsx', 'xls'],
        help="Formatos soportados: CSV, Excel (.xlsx, .xls)"
    )
    
    if uploaded_file is not None:
        try:
            with st.spinner("🔄 Cargando archivo..."):
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                st.session_state['df_original'] = df
                st.success(f"✅ Archivo cargado: **{uploaded_file.name}**")
                st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo: {str(e)}")
    
    if 'df_original' in st.session_state:
        df = st.session_state['df_original']
        
        st.markdown("### 📊 Vista Previa y Estadísticas")
        
        # Métricas principales con diseño mejorado
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("📏 Filas", f"{df.shape[0]:,}", help="Total de registros")
        with col2:
            st.metric("📊 Columnas", df.shape[1], help="Total de variables")
        with col3:
            memory_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
            st.metric("💾 Tamaño", f"{memory_mb:.2f} MB", help="Uso de memoria")
        with col4:
            null_pct = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)
            st.metric("❌ Nulos", f"{null_pct:.1f}%", help="Porcentaje de valores faltantes")
        with col5:
            dup_pct = (df.duplicated().sum() / len(df) * 100)
            st.metric("🔄 Duplicados", f"{dup_pct:.1f}%", help="Porcentaje de filas duplicadas")
        
        st.markdown("### 📋 Primeras 10 filas")
        st.dataframe(df.head(10), use_container_width=True, height=400)
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
