import streamlit as st
import pandas as pd
import anthropic

# Función para generar análisis con Claude
def generate_ai_analysis(df, resumen):
    """
    Genera un análisis inteligente de los datos usando Claude API
    """
    try:
        # Preparar resumen de datos para Claude
        total_enlaces = len(df)
        codigo_301 = resumen.get(301, 0)
        codigo_302 = resumen.get(302, 0)
        codigo_400 = resumen.get(400, 0)
        codigo_403 = resumen.get(403, 0)
        codigo_404 = resumen.get(404, 0)
        
        # Top 5 URLs con más problemas (si hay columna Fuente)
        if 'Fuente' in df.columns:
            top_problemas = df['Fuente'].value_counts().head(5)
            top_urls = "\n".join([f"- {url}: {count} enlaces problemáticos" for url, count in top_problemas.items()])
        else:
            top_urls = "No disponible"
        
        # Construir prompt para Claude
        prompt = f"""Eres un experto en SEO técnico. Analiza los siguientes datos de un rastreo de sitio web y proporciona un análisis ejecutivo conciso y accionable.

DATOS DEL SITIO:
- Total de enlaces problemáticos: {total_enlaces}
- Errores 404 (páginas no encontradas): {codigo_404}
- Errores 403 (acceso prohibido): {codigo_403}
- Errores 400 (bad request): {codigo_400}
- Redirecciones 301 (permanentes): {codigo_301}
- Redirecciones 302 (temporales): {codigo_302}

PÁGINAS CON MÁS PROBLEMAS:
{top_urls}

ESTRUCTURA REQUERIDA:

**DIAGNÓSTICO**
Evaluación directa del estado del sitio en 2-3 líneas máximo.

**PROBLEMAS IDENTIFICADOS**
Lista los problemas en orden de severidad (usa checkboxes):
- [ ] Problema 1
- [ ] Problema 2
- [ ] Problema 3

**PLAN DE ACCIÓN (Por Orden de Prioridad)**
Acciones específicas y concretas ordenadas por prioridad (usa numeración):

1. **Prioridad Crítica**
   - [ ] Acción específica 1
   - [ ] Acción específica 2

2. **Prioridad Alta**
   - [ ] Acción específica 1
   - [ ] Acción específica 2

3. **Prioridad Media**
   - [ ] Acción específica 1
   - [ ] Acción específica 2

**IMPACTO EN SEO**
Breve explicación (2-3 bullets) de cómo esto afecta el posicionamiento.

IMPORTANTE: 
- Sé conciso y directo
- NO menciones herramientas de rastreo
- NO incluyas tiempos estimados
- Usa formato checklist para acciones
- Enfócate en QUÉ hacer, no en CUÁNDO hacerlo"""

        # Llamar a la API de Claude
        client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
        
    except Exception as e:
        return f"❌ Error al generar análisis: {str(e)}\n\nVerifica que tu API key esté configurada correctamente en Streamlit Secrets."

# Configuración de la página
st.set_page_config(
    page_title="Informe SEO - Análisis de Enlaces",
    page_icon="🔍",
    layout="wide"
)

# ==================== TÍTULO ====================
st.markdown("""
<div style="text-align: center;">
    <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; display: inline-block; margin-bottom: 20px;">
        <img src="https://imagizer.imageshack.com/img922/1260/r88PYU.png" 
             style="height: 80px; display: block;">
    </div>
    <h1 style="margin: 0; text-align: center;">Informe de Enlaces Problemáticos - Análisis SEO Técnico</h1>
    <p style="color: #666; font-size: 18px; margin: 10px 0 0 0; text-align: center;">Identificación y diagnóstico de errores 404, redirecciones y problemas de acceso</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ==================== CARGA DE ARCHIVO ====================
uploaded_file = st.file_uploader("📁 Sube tu archivo CSV de Screaming Frog", type=['csv'])

# Si no hay archivo, mostrar demo
if uploaded_file is None:
    st.info("👆 Sube un archivo CSV para comenzar. Mientras tanto, aquí hay un ejemplo con datos de demostración:")
    
    # DATOS DE DEMOSTRACIÓN
    demo_data = {
        'Fuente': ['https://ejemplo.com/pagina1', 'https://ejemplo.com/pagina2', 'https://ejemplo.com/pagina3'] * 10,
        'Destino': ['https://ejemplo.com/roto1', 'https://ejemplo.com/roto2', 'https://ejemplo.com/redirect1'] * 10,
        'Ancla': ['Click aquí', 'Ver más', 'Conoce más'] * 10,
        'Código de estado': [404, 404, 301] * 10
    }
    df = pd.DataFrame(demo_data)
    st.warning("⚠️ Estos son datos de ejemplo. Sube tu CSV para ver tu informe real.")
else:
    # Cargar el CSV real
    df = pd.read_csv(uploaded_file, sep=';', encoding='utf-8-sig')
    st.success(f"✅ Archivo cargado correctamente: {len(df)} enlaces encontrados")

# ==================== SECCIÓN 1: RESUMEN EJECUTIVO ====================
st.header("1. Resumen Ejecutivo")

col1, col2, col3, col4 = st.columns(4)

# Contar por código de estado
resumen = df['Código de estado'].value_counts()

with col1:
    st.metric("Total de Enlaces", f"{len(df):,}")

with col2:
    total_404 = resumen.get(404, 0)
    st.metric("🔴 Errores 404", total_404)

with col3:
    total_403 = resumen.get(403, 0)
    st.metric("🚫 Errores 403", total_403)

with col4:
    total_redirects = resumen.get(301, 0) + resumen.get(302, 0)
    st.metric("↪️ Redirecciones", total_redirects)

st.markdown("---")

# ==================== SECCIÓN 2: DISTRIBUCIÓN POR CÓDIGO ====================
st.header("📈 2. Distribución de Códigos de Estado")

# Crear tarjetas visuales para cada código
st.subheader("Resumen Visual")

# Obtener datos de cada código
codigo_301 = resumen.get(301, 0)
codigo_302 = resumen.get(302, 0)
codigo_400 = resumen.get(400, 0)
codigo_403 = resumen.get(403, 0)
codigo_404 = resumen.get(404, 0)

total = len(df)

# Crear 5 columnas para las tarjetas en una sola línea
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div style="background-color: #FFA500; padding: 12px 8px; border-radius: 8px; text-align: center;">
        <h4 style="color: white; margin: 0; font-size: 13px;">301</h4>
        <h1 style="color: white; font-size: 42px; margin: 5px 0; font-weight: bold;">{codigo_301}</h1>
        <p style="color: white; margin: 0; font-size: 16px;">{(codigo_301/total*100):.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background-color: #FFD700; padding: 12px 8px; border-radius: 8px; text-align: center;">
        <h4 style="color: #333; margin: 0; font-size: 13px;">302</h4>
        <h1 style="color: #333; font-size: 42px; margin: 5px 0; font-weight: bold;">{codigo_302}</h1>
        <p style="color: #333; margin: 0; font-size: 16px;">{(codigo_302/total*100):.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="background-color: #FF6347; padding: 12px 8px; border-radius: 8px; text-align: center;">
        <h4 style="color: white; margin: 0; font-size: 13px;">400</h4>
        <h1 style="color: white; font-size: 42px; margin: 5px 0; font-weight: bold;">{codigo_400}</h1>
        <p style="color: white; margin: 0; font-size: 16px;">{(codigo_400/total*100):.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background-color: #FF8C00; padding: 12px 8px; border-radius: 8px; text-align: center;">
        <h4 style="color: white; margin: 0; font-size: 13px;">403</h4>
        <h1 style="color: white; font-size: 42px; margin: 5px 0; font-weight: bold;">{codigo_403}</h1>
        <p style="color: white; margin: 0; font-size: 16px;">{(codigo_403/total*100):.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div style="background-color: #DC143C; padding: 12px 8px; border-radius: 8px; text-align: center;">
        <h4 style="color: white; margin: 0; font-size: 13px;">404</h4>
        <h1 style="color: white; font-size: 42px; margin: 5px 0; font-weight: bold;">{codigo_404}</h1>
        <p style="color: white; margin: 0; font-size: 16px;">{(codigo_404/total*100):.1f}%</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== SECCIÓN IA: ANÁLISIS INTELIGENTE ====================
st.markdown("<h2 style='text-align: center;'>🤖 Análisis Inteligente con IA</h2>", unsafe_allow_html=True)

# Centrar el botón
col1, col2, col3 = st.columns([2, 1, 2])

with col2:
    if "ANTHROPIC_API_KEY" in st.secrets:
        if st.button("🚀 Generar Análisis", type="primary", use_container_width=True):
            with st.spinner("Analizando..."):
                analysis = generate_ai_analysis(df, resumen)
                st.session_state['ai_analysis'] = analysis

# Mostrar análisis si existe
if "ANTHROPIC_API_KEY" in st.secrets:
    if 'ai_analysis' in st.session_state:
        st.markdown("---")
        st.subheader("📋 Análisis Generado")
        
        # Mostrar el análisis con markdown
        st.markdown(st.session_state['ai_analysis'])
        
        # Opción para descargar el texto
        st.download_button(
            label="📄 Descargar Análisis como TXT",
            data=st.session_state['ai_analysis'],
            file_name="analisis_seo_ia.txt",
            mime="text/plain"
        )
else:
    st.info("💡 El análisis con IA estará disponible cuando configures tu API key de Anthropic en Streamlit Secrets.")
    st.write("**Agrega tu API key en:** Settings → Secrets")
    st.code('ANTHROPIC_API_KEY = "tu_key_aquí"', language="toml")

st.markdown("---")

# Tabla detallada
st.subheader("Tabla Detallada")

resumen_df = pd.DataFrame({
    'Código': resumen.index,
    'Cantidad': resumen.values,
    'Porcentaje': (resumen.values / len(df) * 100).round(1)
})
resumen_df['Porcentaje'] = resumen_df['Porcentaje'].astype(str) + '%'

st.dataframe(resumen_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ==================== SECCIÓN 3: ANÁLISIS DETALLADO DE 404 ====================
st.header("🔴 3. Detalle de Errores 404 (Enlaces Rotos)")

df_404 = df[df['Código de estado'] == 404]

if len(df_404) > 0:
    st.write(f"**Se encontraron {len(df_404)} enlaces rotos que deben ser corregidos:**")
    
    # Tabla de 404s
    tabla_404 = df_404[['Fuente', 'Destino', 'Ancla']].copy()
    tabla_404.columns = ['Fuente', 'Destino', 'Ancla']
    
    st.dataframe(tabla_404, use_container_width=True, hide_index=True)
else:
    st.success("✅ ¡Excelente! No se encontraron enlaces rotos (404)")

st.markdown("---")

# ==================== SECCIÓN 4: ANÁLISIS DE REDIRECCIONES ====================
st.header("↪️ 4. Análisis de Redirecciones (301/302)")

df_redirects = df[df['Código de estado'].isin([301, 302])]

if len(df_redirects) > 0:
    st.write(f"**Se encontraron {len(df_redirects)} redirecciones:**")
    
    # Mostrar solo las primeras 10
    tabla_redirects = df_redirects[['Fuente', 'Destino', 'Código de estado']].head(10).copy()
    tabla_redirects.columns = ['Fuente', 'Destino', 'Código de estado']
    
    st.dataframe(tabla_redirects, use_container_width=True, hide_index=True)
    
    if len(df_redirects) > 10:
        st.info(f"ℹ️ Mostrando las primeras 10 de {len(df_redirects)} redirecciones totales")
else:
    st.success("✅ No se encontraron redirecciones")

st.markdown("---")

# ==================== SECCIÓN 5: OTROS ERRORES ====================
st.header("⚠️ 5. Otros Errores Críticos (400, 403)")

df_otros = df[df['Código de estado'].isin([400, 403])]

if len(df_otros) > 0:
    st.write(f"**Se encontraron {len(df_otros)} errores críticos:**")
    
    tabla_otros = df_otros[['Fuente', 'Destino', 'Código de estado', 'Tipo']].head(10).copy()
    tabla_otros.columns = ['Fuente', 'Destino', 'Código de estado', 'Tipo']
    
    st.dataframe(tabla_otros, use_container_width=True, hide_index=True)
    
    if len(df_otros) > 10:
        st.info(f"ℹ️ Mostrando los primeros 10 de {len(df_otros)} errores totales")
else:
    st.success("✅ No se encontraron errores 400 o 403")

st.markdown("---")

# ==================== PIE DE PÁGINA ====================
st.markdown("### Códigos a Solucionar por Orden de Prioridad:")
st.markdown("""
**🔴 PRIORIDAD CRÍTICA (Solucionar Inmediatamente):**
- **404 - Not Found**: Enlaces rotos que generan error al usuario. Corregir o redirigir las URLs.
- **403 - Forbidden**: Recursos bloqueados sin permisos de acceso. Verificar configuración del servidor.
- **400 - Bad Request**: Solicitudes mal formadas. Revisar estructura de las URLs.

**🟡 PRIORIDAD MEDIA (Revisar y Optimizar):**
- **301 - Moved Permanently**: Redirecciones permanentes. Evaluar si son necesarias (afectan velocidad).
- **302 - Found**: Redirecciones temporales. Verificar si deberían ser permanentes (301).
""")

st.markdown("---")
st.caption("🔍 Generado con Streamlit | Datos de Screaming Frog")