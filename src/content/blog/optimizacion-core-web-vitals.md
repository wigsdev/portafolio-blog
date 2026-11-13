---
title: 'Maximizando Core Web Vitals: De LCP a CLS en Sitios Estáticos'
description: 'Guía técnica para auditar y optimizar las métricas clave de Google: Largest Contentful Paint, Cumulative Layout Shift e Interaction to Next Paint.'
pubDate: 'Oct 25 2026'
heroImage: '../../assets/blog-web-vitals.webp'
tags: ['web-performance', 'astro']
---

Los Core Web Vitals de Google no son solo métricas de posicionamiento SEO; representan estándares cuantificables de la calidad de experiencia de usuario en la web real. Lograr puntuaciones superiores a 90 o 95 puntos en Google Lighthouse requiere decisiones técnicas intencionales en el código.

A continuación, analizamos las tres métricas principales y cómo optimizarlas en Astro.

## 1. Largest Contentful Paint (LCP) < 2.5s

El LCP mide cuánto tarda en renderizarse el bloque de contenido visible más grande en la pantalla (usualmente una imagen hero o un título H1).

### Estrategias de Optimización:
* **Pre-renderizado Estático (SSG):** El HTML se genera durante la compilación, logrando un *Time to First Byte* (TTFB) inferior a 100 ms servido desde un CDN.
* **Carga Eager para el Elemento LCP:** El componente `<Image />` de Astro permite asignar `loading="eager"` y `fetchpriority="high"` a la imagen principal, forzando al navegador a solicitarla de inmediato en lugar de retrasarla.
* **Formatos Modernos:** Convertir assets automáticamente a WebP y AVIF con compresión adaptativa reduce el peso de la imagen en más de un 60%.

## 2. Cumulative Layout Shift (CLS) < 0.1

El CLS mide la estabilidad visual de la página. Si un usuario intenta hacer clic en un enlace y un elemento salta repentinamente, la experiencia se degrada.

```html
<!-- Incorrecto: sin dimensiones explícitas (causa CLS al cargar) -->
<img src="/imagen.jpg" alt="Ejemplo" />

<!-- Correcto: dimensiones declaradas o inferidas con astro:assets -->
<Image src={miImagen} alt="Ejemplo" width={720} height={360} />
```

Declarar `width` y `height` permite al navegador reservar el espacio exacto mediante la propiedad CSS `aspect-ratio` antes de que la imagen termine de descargarse.

## 3. Interaction to Next Paint (INP) < 200ms

El INP reemplazó a First Input Delay (FID) para medir la latencia de respuesta ante cualquier interacción del usuario durante toda su sesión en la página.

Al aplicar la filosofía **Zero-JS** de Astro, el hilo principal del navegador permanece completamente libre de bucles de hidratación masivos, garantizando que los clics, botones y menús respondan de forma instantánea.

## Conclusión

El rendimiento web de élite no es producto de trucos de última hora, sino de una **arquitectura fundamentada en el minimalismo**: entregar HTML limpio, optimizar imágenes desde la raíz y evitar JavaScript innecesario.

