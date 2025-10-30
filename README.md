# SEO Link Analyzer

Herramienta de análisis automatizado para identificar y diagnosticar enlaces problemáticos en sitios web.

## Funcionalidades

- Análisis de errores 404, redirecciones y problemas de acceso
- Visualización de métricas clave
- Generación de análisis y recomendaciones mediante inteligencia artificial
- Exportación de resultados

## Cómo usar la aplicación

### 1. Preparar el archivo CSV

El archivo debe contener las siguientes columnas:
- **Fuente**: URL de la página que contiene el enlace
- **Destino**: URL hacia donde apunta el enlace
- **Código de estado**: Código HTTP del enlace (301, 302, 400, 403, 404)
- **Ancla**: Texto del enlace
- **Tipo**: Tipo de recurso (Hipervínculo, Imagen, etc.)

Formato requerido:
- Delimitador: punto y coma (`;`)
- Codificación: UTF-8

### 2. Cargar el archivo

1. Acceder a la aplicación
2. Hacer clic en "Sube tu archivo CSV"
3. Seleccionar el archivo desde el explorador

### 3. Revisar el informe

El sistema genera automáticamente:

**Resumen Ejecutivo**  
Métricas principales del análisis

**Análisis Inteligente con IA**  
Diagnóstico, problemas críticos y plan de acción priorizados

**Distribución de Códigos**  
Visualización de la cantidad de enlaces por tipo de error

**Detalle de Errores 404**  
Lista completa de enlaces rotos

**Análisis de Redirecciones**  
Redirecciones 301 y 302 encontradas

**Otros Errores Críticos**  
Errores 400 y 403 identificados

### 4. Exportar resultados

El análisis generado por IA puede descargarse en formato TXT utilizando el botón "Descargar Análisis como TXT".

## Interpretación de códigos

**Prioridad Crítica:**
- **404**: Página no encontrada - Enlaces rotos que deben corregirse
- **403**: Acceso prohibido - Recursos bloqueados
- **400**: Solicitud incorrecta - URLs mal formadas

**Prioridad Media:**
- **301**: Redirección permanente - Revisar si son necesarias
- **302**: Redirección temporal - Evaluar si deberían ser permanentes

## Soporte

Para consultas o reportar problemas, contactar a los administradores de la aplicación:

<camila.aldana@thecollectiveagency.com>
<netzer.pita@thecollectiveagency.com>
