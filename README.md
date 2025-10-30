# SEO Link Analyzer

Herramienta de análisis automatizado para identificar y diagnosticar enlaces problemáticos en sitios web.

## Códigos de Estado Soportados

La aplicación analiza los siguientes códigos HTTP:

**Errores Críticos:**
- **404** - Página no encontrada
- **403** - Acceso prohibido
- **400** - Solicitud incorrecta
- **500** - Error interno del servidor

**Redirecciones:**
- **301** - Redirección permanente
- **302** - Redirección temporal
- **308** - Redirección permanente (preserva método HTTP)

**Códigos excluidos del análisis:**
- **200** - OK (páginas funcionando correctamente, no requieren acción)
- **0** - Sin respuesta (URLs externas o no rastreadas)

## Preparación del Archivo CSV

### Paso 1: Exportar desde Screaming Frog

1. Realizar el rastreo completo del sitio en Screaming Frog
2. Ir al menú **Exportación en bloque**
3. Seleccionar **Enlaces Internos > Todo**
4. Guardar el archivo CSV exportado

### Paso 2: Filtrar códigos relevantes

Antes de subir el archivo a la aplicación, es necesario excluir los códigos 200 y 0:

**Usando Power Query (Excel):**
1. Cargar el CSV en Power Query
2. Filtrar la columna "Código de estado"
3. Excluir valores 200 y 0
4. Cerrar y cargar los datos filtrados

**Por qué se excluyen estos códigos:**
- **Código 200**: Indica que la página funciona correctamente. No requiere corrección.
- **Código 0**: Corresponde a URLs externas o recursos no rastreados. No son problemas del sitio.

El archivo resultante contendrá únicamente enlaces con problemas que requieren atención.

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
- **Código de estado**: Código HTTP del enlace (301, 302, 308, 400, 403, 404, 500)
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
Redirecciones 301, 302 y 308 encontradas

**Otros Errores Críticos**  
Errores 400, 403 y 500 identificados

### 4. Exportar resultados

El análisis generado por IA puede descargarse en formato TXT utilizando el botón "Descargar Análisis como TXT".

## Interpretación de códigos

**Prioridad Crítica:**
- **404**: Página no encontrada - Enlaces rotos que deben corregirse
- **500**: Error interno del servidor - Revisar logs y configuración del servidor
- **403**: Acceso prohibido - Recursos bloqueados
- **400**: Solicitud incorrecta - URLs mal formadas

**Prioridad Media:**
- **301**: Redirección permanente - Revisar si son necesarias
- **302**: Redirección temporal - Evaluar si deberían ser permanentes
- **308**: Redirección permanente (preserva método HTTP) - Similar a 301

## Soporte

Para consultas o reportar problemas, contactar al administrador del sistema.
- <camila.aldana@thecollectiveagency.com>
- <netzer.pita@thecollectiveagency.com>