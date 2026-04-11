# 🚀 Cómo Desplegar la Demo en Vivo

## Opción 1: Streamlit Community Cloud (RECOMENDADO - GRATIS)

### Paso 1: Ir a Streamlit Cloud
1. Abre tu navegador y ve a: **https://share.streamlit.io/**
2. Haz clic en **"Sign in"** o **"Get started"**
3. Inicia sesión con tu cuenta de GitHub (**cristian77cx**)

### Paso 2: Crear Nueva App
1. Click en el botón **"New app"** (esquina superior derecha)
2. Llena el formulario:
   - **Repository:** `cristian77cx/procesamiento-datos-ia`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (opcional):** `procesamiento-datos-ia` (o el nombre que prefieras)

### Paso 3: Deploy
1. Click en **"Deploy!"**
2. Espera 2-3 minutos mientras se despliega
3. ¡Listo! Tu app estará en una URL como:
   ```
   https://procesamiento-datos-ia.streamlit.app
   ```
   o
   ```
   https://cristian77cx-procesamiento-datos-ia.streamlit.app
   ```

### Paso 4: Actualizar el Portafolio
Una vez tengas la URL, actualiza el archivo `index.html` en tu portafolio:

Busca esta línea (aproximadamente línea 310):
```html
<a href="https://github.com/cristian77cx/procesamiento-datos-ia/blob/main/DEMO.md" target="_blank" class="project-btn demo-btn">
```

Cámbiala por:
```html
<a href="TU_URL_DE_STREAMLIT_AQUI" target="_blank" class="project-btn demo-btn">
```

Ejemplo:
```html
<a href="https://procesamiento-datos-ia.streamlit.app" target="_blank" class="project-btn demo-btn">
  <i class="fas fa-rocket"></i> Demo en Vivo
</a>
```

---

## ✨ Ventajas de Streamlit Cloud

✅ **100% Gratis** - Sin límites para apps públicas  
✅ **Actualización automática** - Cada push a GitHub actualiza la app  
✅ **URL permanente** - No caduca  
✅ **SSL incluido** - HTTPS automático  
✅ **Sin configuración** - Todo funciona out-of-the-box  

---

## 🔄 Actualizaciones Automáticas

Cada vez que hagas `git push` en el repositorio `procesamiento-datos-ia`, Streamlit Cloud detectará los cambios y actualizará la app automáticamente. ¡No necesitas hacer nada más!

---

## 📊 Monitoreo

En el dashboard de Streamlit Cloud puedes ver:
- 📈 Número de visitantes
- ⏱️ Tiempo de actividad
- 🔄 Estado del deployment
- 📝 Logs en tiempo real

---

## 🆘 Solución de Problemas

### Error: "Module not found"
- Asegúrate de que `requirements.txt` esté actualizado
- Verifica que todas las dependencias estén listadas

### Error: "App is sleeping"
- Las apps gratuitas se duermen después de inactividad
- Se reactivan automáticamente cuando alguien las visita
- Toma ~30 segundos en despertar

### Error de memoria
- Reduce el tamaño de los datasets de ejemplo
- Optimiza el código para usar menos RAM

---

## 🎯 Resultado Final

Una vez desplegado, los clientes podrán:

1. **Visitar tu portafolio:** https://cristian77cx.github.io
2. **Click en "Demo en Vivo"** en el proyecto
3. **Usar la aplicación directamente** sin instalar nada
4. **Subir sus propios datos** y ver el procesamiento
5. **Descargar resultados** procesados

---

## 💡 Tips Profesionales

1. **Personaliza la URL** - Usa un nombre corto y memorable
2. **Agrega analytics** - Usa Google Analytics para ver visitantes
3. **Comparte en LinkedIn** - Publica sobre tu proyecto
4. **Actualiza regularmente** - Agrega nuevas features

---

## 📞 Soporte

Si tienes problemas:
- 📚 Documentación: https://docs.streamlit.io/streamlit-community-cloud
- 💬 Foro: https://discuss.streamlit.io/
- 📧 Email: pinedandres002@gmail.com

---

**¡Tu demo estará disponible 24/7 para que los clientes la prueben!** 🚀
