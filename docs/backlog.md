# Portafolio + Blog Personal — Product Backlog

## 📌 Información del Proyecto

| Campo | Valor |
|---|---|
| **Proyecto** | Portafolio Personal & Blog Técnico Integrador |
| **Repositorio** | `wigsdev/portafolio-blog` |
| **Desarrollador** | Wilmer Gulcochía (@wigsdev) |
| **Rol** | Full-Stack Web Developer |
| **Duración** | 5 semanas (26 de octubre de 2026 – 29 de noviembre de 2026) |
| **Stack Tecnológico** | Astro 7.4 (Astro 5 Core) · JavaScript / TypeScript · CSS Scoped / Modern CSS · Content Collections (Zod) · sharp (`<Image />`) · View Transitions (`<ClientRouter />`) · Islas interactivas (`client:*`) |
| **Convenciones** | Conventional Commits · GitHub Flow con ramas cortas · Mobile First · WCAG AA · DoD Estricto |
| **Automatización** | `scripts/create_github_issues.py` (sincronización de hitos y tareas en GitHub) |

---

## ⚙️ Sistema de Gestión y Flujo de Trabajo

### Estrategia de Ramas (GitHub Flow Unipersonal)
Al ser un proyecto personal orientado a portafolio y evaluación profesional:
- **Rama principal (`main`):** Siempre estable, testeable y lista para despliegue en producción.
- **Ramas de funcionalidad (`feat/T-XX-nombre` o `fix/T-XX-nombre`):** Se crea una rama por cada tarea. Al finalizar, se abre un Pull Request hacia `main` que cierra la Issue automáticamente (usando la palabra clave `Closes #XX`).
- **Merge:** Consolidación mediante **Squash and Merge** para mantener un historial de commits limpio, lineal y atómico en `main`.

### Estados de las Tareas
| Estado | Label en GitHub | Color | Significado |
|---|---|---|---|
| 🔲 Backlog | `status: backlog` | `#EDEDED` | Tarea definida y lista para ser abordada |
| 🔨 En Progreso | `status: in-progress` | `#FEF2C0` | Trabajo activo en rama de feature |
| 🔍 En Revisión / QA | `status: in-review` | `#D8F8C8` | PR abierto o validación de criterios cumplidos |
| ✅ Done | — (Issue Cerrado) | — | PR mergeado a `main` y criterios verificados |

### Prioridades
| Label | Color Hex | Significado |
|---|---|---|
| `priority: critical` | 🔴 `#B60205` | Bloqueante: Arquitectura base, layouts o configuración indispensable |
| `priority: high` | 🟠 `#D93F0B` | Requisito Mínimo del Curso: Esencial para la consigna y la rúbrica |
| `priority: medium` | 🟡 `#FBCA04` | Funcionalidad complementaria o mejora de experiencia de usuario |
| `priority: low` | 🟢 `#0E8A16` | Pulido visual, animaciones opcionales o extras |

### Tipos de Tarea
| Label | Significado |
|---|---|
| `type: structure` | Configuración, tooling, layouts y arquitectura de carpetas |
| `type: style` | Sistema de diseño, tokens CSS, dark/light mode y tipografía |
| `type: feature` | Componentes de portafolio, rutas dinámicas y blog |
| `type: server` | Funciones de servidor, endpoints API y validaciones Zod |
| `type: presentation` | Diapositivas, preparación de sustentación y despliegue |

### Definition of Done (DoD) General
Una tarea se considera **Done** cuando:
1. Todos los criterios de aceptación específicos están cumplidos y verificados al 100%.
2. Cero errores de compilación (`pnpm build`) y cero advertencias críticas en consola.
3. Accesibilidad semántica básica verificada (etiquetas `alt` en imágenes, contraste adecuado, navegación por teclado).
4. Commits atómicos siguiendo la convención Conventional Commits (`feat:`, `fix:`, `docs:`, `style:`).
5. Rama mergeada a `main` e Issue correspondiente cerrada en GitHub.

---

## 🗓️ Cronograma General por Sprints

| Sprint / Semana | Fechas Reales | Hito Principal | Requisitos Oficiales Cubiertos |
|---|:---:|---|:---:|
| **Sprint 1 (Semana 1)** | 26 Oct – 01 Nov 2026 | Fundamentos, Sistema de Diseño & Layouts Base | R1, R2, R7 |
| **Sprint 2 (Semana 2)** | 02 Nov – 08 Nov 2026 | Portafolio Personal & Optimización de Imágenes | R1, R5 |
| **Sprint 3 (Semana 3)** | 09 Nov – 15 Nov 2026 | Blog Técnico, Content Collections & Rutas Dinámicas | R3, R4 |
| **Sprint 4 (Semana 4)** | 16 Nov – 22 Nov 2026 | Isla Interactiva, Servidor, Sobre Mí, Tailwind, Refactorización & SEO 90+ | R2, R6, R8, R9 |
| **Sprint 5 (Semana 5)** | 23 Nov – 29 Nov 2026 | Despliegue Público, Diapositivas & Sustentación | R10 |

---

## 📋 Catálogo Granular de Tareas (Orden Lógico de Inicio a Fin)

---

### SPRINT 1 — Fundamentos, Sistema de Diseño & Layouts Base (26 Oct – 01 Nov 2026)

#### T-01 — Gobernanza, Configuración del Repositorio y Entorno Documental
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: structure` |
| **Dependencias** | Ninguna |
| **Complejidad** | Baja (1 día) |
| **Archivos afectados** | `.gitignore`, `package.json`, `docs/backlog.md`, `docs/workflow.md`, `README.md` |

**Descripción y Contexto Técnico:**  
Configurar la base de control de versiones y el ecosistema documental inicial. Asegurar que `.gitignore` aísle `.reference/`, verificar scripts de desarrollo con `pnpm`, y redactar `docs/workflow.md` con las reglas de Git Flow unipersonal y Conventional Commits.

**Criterios de Aceptación:**
- [x] `.gitignore` excluye correctamente `.reference/`, `node_modules/`, `dist/` y `.astro/`.
- [x] `docs/workflow.md` documenta la convención de ramas, commits y DoD.
- [x] `README.md` actualizado con descripción del proyecto personal, stack e instrucciones de ejecución.
- [x] Servidor de desarrollo validado en modo background (`pnpm astro dev --background`).

---

#### T-02 — Sistema de Tokens CSS, Soporte Dark/Light y Fuente con Font API
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: style` |
| **Dependencias** | T-01 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `astro.config.mjs`, `src/styles/global.css`, `src/assets/fonts/*` |

**Descripción y Contexto Técnico:**  
Definir las variables globales CSS en `src/styles/global.css` adaptadas del portafolio de referencia (paleta de colores moderna para modo claro y modo oscuro, espaciados y sombras). Conectar la fuente local *Atkinson* (`--font-atkinson`) configurada en `astro.config.mjs` vía `fontProviders.local()` para cumplir con el Requisito R2.

**Criterios de Aceptación:**
- [ ] Paleta semántica de variables CSS (`--color-bg`, `--color-text`, `--color-brand`, `--color-surface`) disponible para modos claro y oscuro.
- [ ] La fuente local *Atkinson* se aplica fluidamente en toda la aplicación mediante la variable `--font-atkinson`.
- [ ] Estilos globales con reset moderno y tipografía base accesible.

---

#### T-03 — Componentes de Navegación y UI Base (Header, Footer, ThemeToggle)
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: structure` |
| **Dependencias** | T-02 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/components/Header.astro`, `src/components/Navigation.astro`, `src/components/Footer.astro`, `src/components/Social.astro`, `src/components/ThemeToggle.astro` |

**Descripción y Contexto Técnico:**  
Crear la estructura reutilizable de encabezado y pie de página. Integrar `ThemeToggle.astro` con script sincronizado a los eventos de Astro (`astro:after-swap` y `astro:page-load`) para alternar el tema sin parpadeos, y enlaces de navegación hacia Inicio, Proyectos, Blog y Contacto.

**Criterios de Aceptación:**
- [ ] `Header.astro` muestra el logo personal de Wilmer y el menú de navegación adaptable.
- [ ] `ThemeToggle.astro` cambia entre modo oscuro y claro persistiendo en `localStorage`.
- [ ] `Footer.astro` incluye enlaces a redes sociales (GitHub, LinkedIn, Email) y año dinámico.
- [ ] Menú accesible con navegación por teclado y contraste adecuado.

---

#### T-04 — Layout Base Unificado con View Transitions y Metadatos SEO
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: structure` |
| **Dependencias** | T-03 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/layouts/BaseLayout.astro`, `src/components/BaseHead.astro` |

**Descripción y Contexto Técnico:**  
Construir `src/layouts/BaseLayout.astro` reutilizable con props tipadas (`pageTitle`, `description`, `eyebrow`, `mainClass`) y slots semánticos. Incorporar `<ClientRouter />` (`astro:transitions`) para navegación SPA suave sin recarga completa de página, cumpliendo los Requisitos R1 y R7.

**Criterios de Aceptación:**
- [ ] `BaseLayout.astro` encapsula `<BaseHead />`, `<Header />`, `<main>`, `<slot />` y `<Footer />`.
- [ ] `<ClientRouter />` opera correctamente y las transiciones entre páginas no provocan reseteo del tema oscuro/claro.
- [ ] Soporte para `props` y `slot` verificado con TypeScript.

---

### SPRINT 2 — Portafolio Personal & Optimización de Imágenes (02 Nov – 08 Nov 2026)

#### T-05 — Componente Reutilizable ProjectCard con Props, Slots y `<Image />`
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-04 |
| **Complejidad** | Media (1 día) |
| **Archivos afectados** | `src/components/ProjectCard.astro`, `src/components/Badge.astro` |

**Descripción y Contexto Técnico:**  
Desarrollar el componente `ProjectCard.astro` para representar proyectos. Debe tipar sus props con TypeScript (usando `ImageMetadata`), optimizar la imagen con el componente `<Image />` de `astro:assets` (`loading="eager"` para los primeros y `"lazy"` para el resto), chips de tecnologías y un `<slot />` opcional para notas o métricas destacadas (Requisitos R1 y R5).

**Criterios de Aceptación:**
- [ ] Props estrictamente tipadas con TypeScript (`nombre`, `descripcion`, `tecnologias`, `imagen`, `demoUrl`, `githubUrl`).
- [ ] Uso exclusivo de `<Image />` de `astro:assets` con dimensiones explícitas y atributo `alt`.
- [ ] Implementación de `<slot />` para contenido extra personalizado.

---

#### T-06 — Página de Inicio (Hero, Perfil Profesional y Proyectos Destacados)
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-05 |
| **Complejidad** | Media (2 días) |
| **Archivos afectados** | `src/pages/index.astro` |

**Descripción y Contexto Técnico:**  
Maquetar la página de inicio principal (`/`) integrando la identidad de Wilmer Gulcochía (`PERFIL.md`): propuesta de valor como desarrollador Frontend & Web con Astro/TypeScript e IA, badges de stack técnico, llamada a la acción y un carrusel o grid con los proyectos más representativos.

**Criterios de Aceptación:**
- [ ] Hero section con presentación clara, roles y enlaces a contacto y proyectos.
- [ ] Sección de tecnologías clave y enfoque técnico.
- [ ] Sección de proyectos destacados reutilizando `ProjectCard.astro`.
- [ ] Enlace directo a los últimos artículos del blog.

---

#### T-07 — Página de Proyectos con Catálogo Completo y Assets Optimizados
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-05, T-06 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/pages/proyectos.astro`, `src/assets/projects/*` |

**Descripción y Contexto Técnico:**  
Migrar los 6 proyectos reales desde `.reference/portafolio-astro` (Pomodoro, Markdown-PDF, OmniSpec IA, Gestor de Biblioteca, Salesforce Admin, Weather Dashboard) con sus imágenes a `src/assets/projects/`. Crear la página `/proyectos` que itere el catálogo con `map()`.

**Criterios de Aceptación:**
- [ ] Los 6 proyectos renderizan sin errores con descripciones precisas, tags y enlaces a GitHub y demos.
- [ ] Todas las imágenes se procesan con `sharp` y el componente `<Image />`.
- [ ] Grid adaptable a móviles, tablets y monitores de escritorio.

---

#### T-08 — Página Sobre Mí, Trayectoria y Descarga de CV en PDF
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-04 |
| **Complejidad** | Baja (1 día) |
| **Archivos afectados** | `src/pages/sobre-mi.astro`, `public/cv.pdf` |

**Descripción y Contexto Técnico:**  
Crear la página `/sobre-mi` con la historia profesional de Wilmer, enfoque de arquitectura de software, certificaciones internacionales (Oracle OCI AI, Cisco Ethical Hacker, IBM Data Science) y botón de descarga directa de CV en PDF alojado en `public/`.

**Criterios de Aceptación:**
- [ ] Contenido estructurado de formación, certificaciones y experiencia.
- [ ] Enlace de descarga funcional hacia `/cv.pdf` ubicado en `public/`.
- [ ] Enlaces a redes y plataformas técnicas (CodePen, GitHub, LinkedIn).

---

### SPRINT 3 — Blog Técnico, Content Collections & Rutas Dinámicas (09 Nov – 15 Nov 2026)

#### T-09 — Configuración de Colección de Contenido con Zod y Entradas Reales
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-04 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/content.config.ts`, `src/content/blog/*` |

**Descripción y Contexto Técnico:**  
Configurar la colección `blog` en `src/content.config.ts` utilizando la nueva API de Astro 5 (`loader: glob`) con validación Zod estricta: `title`, `description`, `pubDate`, `updatedDate`, `heroImage`, y el campo de array `tags: z.array(z.string()).default([])`. Contar con al menos 5 artículos técnicos reales con temática de desarrollo moderno (Requisito R3).

**Criterios de Aceptación:**
- [ ] Esquema Zod validando tipos de datos obligatorios y opcionales.
- [ ] Mínimo 5 artículos `.md` y `.mdx` en `src/content/blog/` pasando la validación sin errores de build.
- [ ] Cada artículo contiene etiquetas (`tags`) coherentes para la taxonomía.

---

#### T-10 — Plantilla de Lectura de Artículo con Layout y Renderizado Markdown/MDX
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-09 |
| **Complejidad** | Media (1 día) |
| **Archivos afectados** | `src/layouts/BlogPost.astro`, `src/pages/blog/[...slug].astro` |

**Descripción y Contexto Técnico:**  
Adaptar el layout de lectura de post `src/layouts/BlogPost.astro` y la página dinámica `src/pages/blog/[...slug].astro`. Debe mostrar imagen de cabecera (`<Image />`), fecha con `FormattedDate.astro`, tiempo de lectura estimado, etiquetas que enlazan a sus páginas de tags y cuerpo del post con soporte de sintaxis resaltada y componentes MDX.

**Criterios de Aceptación:**
- [ ] Renderizado dinámico de artículos con `render(post)` de `astro:content`.
- [ ] Presentación tipográfica legible y adaptable (`prose`).
- [ ] Lista de tags clickeables que redirigen a `/blog/tags/[tag]`.

---

#### T-11 — Listado Paginado del Blog con `paginate()` y `getStaticPaths()`
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-10 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/pages/blog/[...page].astro`, `src/components/BlogCard.astro`, `src/components/Pagination.astro` |

**Descripción y Contexto Técnico:**  
Implementar la ruta `src/pages/blog/[...page].astro` empleando la función `paginate()` dentro de `getStaticPaths()` para cumplir con el Requisito R4. Componente `Pagination.astro` con enlaces a página anterior/siguiente y números de página.

**Criterios de Aceptación:**
- [ ] `getStaticPaths()` utiliza `paginate()` configurando un límite por página (ej. 3 o 4 posts).
- [ ] Rutas generadas correctamente (`/blog/`, `/blog/2`, etc.).
- [ ] Controles de paginación accesibles y deshabilitados cuando no hay página previa/siguiente.

---

#### T-12 — Rutas Dinámicas de Taxonomía por Etiquetas (`/blog/tags/[tag]`)
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-11 |
| **Complejidad** | Media (1 día) |
| **Archivos afectados** | `src/pages/blog/tags/[tag].astro`, `src/pages/blog/tags/index.astro` |

**Descripción y Contexto Técnico:**  
Inspirándose en `.reference/tutorial-blog`, crear la página `src/pages/blog/tags/[tag].astro` con `getStaticPaths()` consumiendo `getCollection('blog')` para filtrar posts por etiqueta, y la página índice `src/pages/blog/tags/index.astro` con la nube completa de etiquetas (Requisito R4).

**Criterios de Aceptación:**
- [ ] `getStaticPaths()` extrae los tags únicos de toda la colección y filtra los posts asociados.
- [ ] `/blog/tags/[tag]` renderiza únicamente los artículos asociados al tag consultado.
- [ ] Nube de etiquetas en `/blog/tags/` con conteo de artículos por tag.

---

### SPRINT 4 — Isla Interactiva, Funciones de Servidor & SEO 90+ (16 Nov – 22 Nov 2026)

#### T-13 — Componente de Isla Interactiva con Directiva `client:*`
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-07, T-11 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/components/InteractiveFilter.jsx` (o `.tsx`), página receptora (`proyectos.astro` o `blog/index.astro`) |

**Descripción y Contexto Técnico:**  
Implementar una isla interactiva de framework UI (Preact o React) con hidratación parcial mediante directiva `client:load` o `client:visible` para cumplir con el Requisito R6. Puede ser un filtro dinámico instantáneo de proyectos por tecnología o un buscador en vivo de artículos del blog.

**Criterios de Aceptación:**
- [ ] Componente interactivo utilizando hooks de estado (`useState`).
- [ ] Inclusión en página con directiva `client:load` o `client:visible`.
- [ ] El resto de la página permanece con 0 KB de JavaScript.

---

#### T-14 — Formulario de Contacto con Función de Servidor y Validación Zod
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: server` |
| **Dependencias** | T-04 |
| **Complejidad** | Media (2 días) |
| **Archivos afectados** | `src/pages/contacto.astro`, `src/pages/api/contact.ts` (o `src/actions/index.ts`) |

**Descripción y Contexto Técnico:**  
Desarrollar la página `/contacto` integrando un formulario funcional que envíe datos a una función de servidor: Astro Action o Endpoint API POST (`/api/contact`) con validación de datos en servidor mediante esquema Zod (`nombre`, `email`, `mensaje`), retornando respuestas estructuradas de éxito o error (Requisito R8).

**Criterios de Aceptación:**
- [ ] Formulario con campos de nombre, email, asunto y mensaje, con accesibilidad de labels e inputs.
- [ ] Endpoint o Action que procesa la petición y valida con Zod en servidor.
- [ ] Mensajes claros de validación (campos requeridos, formato de correo) y feedback de confirmación al usuario.

---

#### T-15 — Rediseño Visual y Arquitectura de Contenidos de la Página Sobre Mí (/sobre-mi)
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-08 |
| **Complejidad** | Media (2 días) |
| **Archivos afectados** | `src/pages/sobre-mi.astro`, `src/styles/global.css`, `public/foto.jpg`, `public/cv.pdf` |

**Descripción y Contexto Técnico:**  
Rediseñar integralmente la página `/sobre-mi` elevando su estándar visual y jerarquía editorial: ficha asimétrica con retrato optimizado, badge pulsante de disponibilidad, ubicación geográfica con icono vectorial, capa de datos tipada `src/data/credentials.ts`, componente `CredentialCard.astro` y CV descargable bajo formato ATS.

**Criterios de Aceptación:**
- [x] Bio con tarjeta de perfil enriquecida (`foto.jpg`), badge de disponibilidad y ubicación.
- [x] Certificaciones y formación continua en tarjetas modulares accesibles (`CredentialCard.astro`).
- [x] Descarga de CV actualizado bajo metodología Harvard / ATS.
- [x] Arquitectura 100% Zero-JS preservada.

---

#### T-16 — Migración Progresiva del Sistema de Diseño a Tailwind CSS
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: style` |
| **Dependencias** | T-02, T-03, T-05 |
| **Complejidad** | Alta (3 días) |
| **Archivos afectados** | `astro.config.mjs`, `src/styles/global.css`, componentes UI y páginas principales |

**Descripción y Contexto Técnico:**  
Integrar Tailwind CSS v4 con `@tailwindcss/vite`, mapear variables semánticas (`@theme`), habilitar variante `@custom-variant dark`, migrar todos los componentes y páginas purgando bloques `<style>` locales, extraer SVGs externos a `public/icons/ui/` y sanear `global.css` preservando cero regresión visual y tipografía Atkinson (Requisito R2).

**Criterios de Aceptación:**
- [x] Motor Tailwind v4 integrado sin preflight disruptivo.
- [x] Tokens dark/light y fuente Atkinson mapeados y operativos.
- [x] Átomos, navegación, blog y páginas principales migrados a clases utilitarias.
- [x] 100% de SVGs desacoplados a `public/icons/ui/` con máscaras CSS.
- [x] `global.css` depurado y 9/9 tests pasando en Vitest.

---

#### T-17 — Refactorización y Unificación de Componentes de Blog (BlogFilterIsland y BlogCardItem)
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: feature` |
| **Dependencias** | T-13, T-16 |
| **Complejidad** | Media (1 día) |
| **Archivos afectados** | `src/components/BlogCardItem.tsx`, `src/components/BlogFilterIsland.tsx`, `src/components/BlogCard.astro` |

**Descripción y Contexto Técnico:**  
Refactorizar y unificar los componentes del catálogo del blog para eliminar la duplicación de código de la tarjeta (Principio DRY). Desacoplar la tarjeta a un componente común reutilizable en Preact/Astro (`BlogCardItem.tsx`) y purgar la sobreingeniería de arrastre manual con mouse (Drag-to-Scroll) en `BlogFilterIsland.tsx`, reduciendo el componente a menos de 200 líneas y aligerando el bundle de JavaScript cliente.

**Criterios de Aceptación:**
- [x] Componente unificado `BlogCardItem.tsx` creado y renderizando con fidelidad 1:1 tanto en Astro (SSR estático) como en Preact (CSR dinámico).
- [x] Tarjeta clonada eliminada de `BlogFilterIsland.tsx` (cero duplicación de código).
- [x] Lógica de arrastre manual por mouse eliminada; navegación táctil nativa y botones `<` / `>` funcionando correctamente.
- [x] Cero regresiones visuales en modo claro y modo oscuro.
- [x] Todas las pruebas unitarias pasando (`pnpm test`) y compilación limpia (`pnpm build`).

---

#### T-18 — Auditoría SEO, Sitemap, Feed RSS y Meta Lighthouse ≥ 90
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: structure` |
| **Dependencias** | T-13, T-14, T-16, T-17 |
| **Complejidad** | Media (1 a 2 días) |
| **Archivos afectados** | `src/pages/rss.xml.js`, `astro.config.mjs`, componentes de metadatos |

**Descripción y Contexto Técnico:**  
Configurar `@astrojs/sitemap` y el feed RSS en `/rss.xml`. Verificar etiquetas OpenGraph, Twitter cards y canonicals en todas las páginas. Ejecutar auditoría Lighthouse y optimizar Core Web Vitals (LCP, CLS, INP) para garantizar un puntaje ≥ 90 en Rendimiento, Accesibilidad y SEO (Requisito R9).

**Criterios de Aceptación:**
- [x] `sitemap-index.xml` y `rss.xml` generados correctamente en el build de producción.
- [x] Meta tags OpenGraph y Twitter en todas las páginas.
- [x] Puntaje de Lighthouse ≥ 90 verificado en Rendimiento y Accesibilidad.

---

#### T-18.1 — Subsanación de Observaciones Lighthouse: Contraste WCAG AA, Imágenes y CSS Crítico
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: style` |
| **Dependencias** | T-18 |
| **Complejidad** | Baja (1 día) |
| **Archivos afectados** | `src/styles/global.css`, `src/components/Navigation.astro`, `src/components/ProjectCard.astro`, `src/components/Logo.astro`, `src/components/BlogCard.astro`, `src/layouts/BlogPost.astro`, `src/pages/sobre-mi.astro`, `astro.config.mjs`, `tests/unit/tokens.test.ts` |

**Descripción y Contexto Técnico:**  
Subsanar los hallazgos técnicos detectados durante la auditoría Lighthouse Mobile (`Slow 4G`) de la tarea padre `T-18` (#16): corregir el ratio de contraste WCAG 2.1 AA en botones primarios bajo modo oscuro (`--color-text-inverse: #141416`), desambiguar el propósito accesible de enlaces repetidos en tarjetas de proyectos (`aria-label`), migrar imágenes residuales de componentes `.astro` al pipeline `<Image />` de `astro:assets` y eliminar el bloqueo de renderizado inicial incrustando las hojas de estilo en compilación (`inlineStylesheets: "always"`).

**Criterios de Aceptación:**
- [x] Cero alertas de `color-contrast` en Lighthouse Mobile tanto en modo oscuro como en modo claro.
- [x] Cero alertas de `identical-links-same-purpose` en las tarjetas de proyectos.
- [x] `Logo.astro` y avatares estáticos procesados con Sharp (`<Image />`) en formato WebP con dimensiones exactas.
- [x] Cero peticiones externas de CSS bloqueando el renderizado inicial (`Render-blocking requests`).
- [x] Puntaje de Lighthouse Mobile verificado: **Accessibility 100**, **Best Practices 100**, **SEO 100** y **Performance ≥ 98**.
- [x] Suite `pnpm test` pasando al 100% y compilación `pnpm build` limpia.

---

### SPRINT 5 — Despliegue Público, Diapositivas & Sustentación (23 Nov – 29 Nov 2026)

#### T-19 — Compilación Limpia y Despliegue en Producción con URL Pública
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: presentation` |
| **Dependencias** | T-18, T-18.1 |
| **Complejidad** | Baja (1 día) |
| **Archivos afectados** | `astro.config.mjs`, `package.json`, configuraciones de hosting |

**Descripción y Contexto Técnico:**  
Validar que `pnpm build` compile sin ningún error ni advertencias en estático. Desplegar en plataforma de hosting con SSL activo y URL pública accesible (Netlify, Vercel o Cloudflare Pages), cumpliendo el Requisito R10.

**Criterios de Aceptación:**
- [ ] `pnpm build` exitoso con salida estática en `dist/`.
- [ ] Sitio desplegado y navegable en URL pública en producción.
- [ ] Todas las rutas, imágenes optimizadas y el formulario de servidor funcionan correctamente en la URL pública.

---

#### T-20 — Diapositivas de Presentación y Guía de Sustentación del Proyecto
| Campo | Valor |
|---|---|
| **Prioridad** | `priority: high` |
| **Tipo** | `type: presentation` |
| **Dependencias** | T-19 |
| **Complejidad** | Media (2 a 3 días) |
| **Archivos afectados** | `docs/diapositivas-presentacion.md`, `docs/diapositivas-presentacion.html`, `docs/guia-demostracion.md` |

**Descripción y Contexto Técnico:**  
Elaborar la presentación ejecutiva del proyecto final para la sesión de sustentación. Redactar las diapositivas en Markdown y generar la versión HTML interactiva con Reveal.js o similar, documentando arquitectura, cumplimiento de los 10 requisitos de la consigna y demo en vivo.

**Criterios de Aceptación:**
- [ ] `docs/diapositivas-presentacion.html` interactiva y lista para proyectar.
- [ ] Cobertura de arquitectura de islas, Zero-JS, View Transitions, colecciones, servidor y migración a Tailwind.
- [ ] Guía paso a paso de demostración para la sustentación final.
