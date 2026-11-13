---
title: "Guía de Sintaxis Markdown y Estándares de Redacción Técnica"
description: "Referencia exhaustiva de sintaxis Markdown, formateo de bloques de código, tablas y buenas prácticas editoriales para blogs de ingeniería."
pubDate: "Jul 25 2024"
heroImage: '../../assets/blog-markdown-guia.webp'
tags: ["astro", "web-performance"]
---

La documentación clara y bien formateada es una de las habilidades más distintivas de un ingeniero de software senior. Esta guía sirve como referencia de estilo y prueba de renderizado para todos los elementos tipográficos soportados en nuestro blog técnico.

## 1. Jerarquía de Encabezados

Los encabezados estructuran el documento para lectores humanos y motores de búsqueda (SEO). Solo debe existir un único `H1` por página (el título del artículo), por lo que las secciones internas comienzan en `H2`:

- `## Encabezado H2 (Sección Principal)`
- `### Encabezado H3 (Subsección)`
- `#### Encabezado H4 (Detalle específico)`

## 2. Bloques de Código con Resaltado de Sintaxis

El motor de Astro utiliza internamente Shiki para resaltar código en tiempo de compilación, entregando HTML coloreado con CSS puro **sin cargar librerías de resaltado pesadas en el navegador del cliente**:

```typescript
// Interfaces y contratos tipados en TypeScript
export interface BlogPost {
  title: string;
  pubDate: Date;
  tags: string[];
  readingTimeMinutes: number;
}

export function formatReadingTime(words: number): number {
  const WORDS_PER_MINUTE = 200;
  return Math.ceil(words / WORDS_PER_MINUTE);
}
```

```css
/* Tokens de diseño semánticos */
:root {
  --color-brand: #d0354f;
  --font-atkinson: system-ui, sans-serif;
}
```

## 3. Citas en Bloque (_Blockquotes_) y Notas

> La simplicidad es un prerrequisito para la confiabilidad.  
> — _Edsger W. Dijkstra_

Las citas permiten enfatizar ideas clave, advertencias arquitectónicas o principios metodológicos.

## 4. Tablas de Comparación Técnica

Las tablas en Markdown permiten condensar información comparativa de forma limpia y legible:

| Característica                   | Astro (SSG + Islas)                  | SPA Tradicional (React/Vue)      |
| :------------------------------- | :----------------------------------- | :------------------------------- |
| **JS en Cliente por Defecto**    | **0 KB (Zero-JS)**                   | 150 KB – 500 KB+                 |
| **First Contentful Paint (FCP)** | Instantáneo (< 0.8s)                 | Retardado por descarga de bundle |
| **Estrategia de Hidratación**    | Parcial e independiente (`client:*`) | Hidratación completa del DOM     |
| **SEO y Metadatos**              | Renderizado nativo en build          | Requiere SSR o prerender         |

## Conclusión

Adoptar estándares claros de formato en Markdown no solo embellece los artículos, sino que **facilita la asimilación del conocimiento y profesionaliza la imagen técnica del autor.**
