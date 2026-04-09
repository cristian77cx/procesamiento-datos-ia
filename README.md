# 📊 Sistema de Procesamiento de Datos para IA

Proyecto de procesamiento, limpieza y preparación de datos para entrenar modelos de inteligencia artificial.

## 🚀 **DEMO INTERACTIVA - ¡Pruébalo Ahora!**

### Aplicación Web en Vivo

```bash
streamlit run app.py
```

**La aplicación se abrirá en tu navegador:** `http://localhost:8501`

### ✨ Lo que puedes hacer en la app:

- 📁 **Subir tus propios archivos** CSV o Excel
- 🎲 **Generar datos de ejemplo** con un clic
- 🧹 **Limpiar datos automáticamente** (duplicados, nulos, outliers)
- 📊 **Ver visualizaciones interactivas** en tiempo real
- 🤖 **Preparar datos para Machine Learning** automáticamente
- ⬇️ **Descargar resultados procesados** listos para usar

---

## 🎯 Objetivo

Desarrollar un pipeline completo de procesamiento de datos que incluya:
- Limpieza y transformación de datos
- Análisis exploratorio (EDA)
- Feature engineering
- Preparación de datasets para modelos de ML
- Visualizaciones interactivas

## 🚀 Características

- ✅ Limpieza automática de datos (valores nulos, duplicados, outliers)
- ✅ Análisis exploratorio con estadísticas descriptivas
- ✅ Visualizaciones con Matplotlib y Seaborn
- ✅ Normalización y escalado de datos
- ✅ Encoding de variables categóricas
- ✅ División de datos (train/test)
- ✅ Exportación de datos procesados

## 📁 Estructura del Proyecto

```
proyecto-procesamiento-datos-ia/
├── data/
│   ├── raw/              # Datos originales
│   └── processed/        # Datos procesados
├── notebooks/
│   └── analisis_exploratorio.ipynb
├── src/
│   ├── data_cleaner.py   # Limpieza de datos
│   ├── eda.py            # Análisis exploratorio
│   └── preprocessor.py   # Preprocesamiento
├── visualizations/       # Gráficos generados
├── requirements.txt      # Dependencias
└── README.md
```

## 🛠️ Tecnologías

- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/proyecto-procesamiento-datos-ia.git
cd proyecto-procesamiento-datos-ia

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Uso

### 1. Limpieza de Datos

```python
from src.data_cleaner import DataCleaner

# Cargar y limpiar datos
cleaner = DataCleaner('data/raw/dataset.csv')
df_clean = cleaner.clean()
cleaner.save('data/processed/dataset_clean.csv')
```

### 2. Análisis Exploratorio

```python
from src.eda import ExploratoryDataAnalysis

# Realizar EDA
eda = ExploratoryDataAnalysis(df_clean)
eda.generate_report()
eda.plot_distributions()
eda.plot_correlations()
```

### 3. Preprocesamiento

```python
from src.preprocessor import DataPreprocessor

# Preparar datos para ML
preprocessor = DataPreprocessor(df_clean)
X_train, X_test, y_train, y_test = preprocessor.prepare_for_ml(
    target_column='target',
    test_size=0.2
)
```

## 📊 Ejemplo de Resultados

### Antes del Procesamiento
- Valores nulos: 15%
- Duplicados: 234 registros
- Outliers: 89 registros

### Después del Procesamiento
- ✅ Datos limpios: 100%
- ✅ Sin duplicados
- ✅ Outliers tratados
- ✅ Variables normalizadas
- ✅ Listo para ML

## 📈 Visualizaciones

El proyecto genera automáticamente:
- Distribuciones de variables
- Matriz de correlación
- Boxplots para detección de outliers
- Gráficos de dispersión
- Histogramas

## 🎓 Aprendizajes

- Técnicas de limpieza de datos
- Análisis exploratorio de datos (EDA)
- Feature engineering
- Normalización y escalado
- Manejo de valores nulos y outliers
- Preparación de datos para ML

## 📝 Próximas Mejoras

- [ ] Implementar detección automática de tipos de datos
- [ ] Agregar más técnicas de feature engineering
- [ ] Implementar pipeline con Scikit-learn
- [ ] Agregar tests unitarios
- [ ] Crear dashboard interactivo con Streamlit

## 👤 Autor

**Cristian Pineda**
- Email: pinedandres002@gmail.com
- LinkedIn: [linkedin.com/in/cristian-pineda](https://linkedin.com/in/cristian-pineda)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

⭐ Si te gusta este proyecto, dale una estrella en GitHub!
