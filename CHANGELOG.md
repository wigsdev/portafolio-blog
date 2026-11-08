# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning (SemVer 2.0.0)](https://semver.org/lang/es/).

---

## [Unreleased]

### Planificado
- **Sprint 4:** Migración progresiva del sistema de diseño a Tailwind CSS (`T-15`).

---

## [0.7.0] - 2026-11-08

### Añadido
- **Página Sobre Mí (`T-08`):** Creación de `src/pages/sobre-mi.astro` utilizando `BaseLayout.astro`, con biografía profesional, enfoque en arquitectura de software con Astro/TypeScript e integración de IA.
- **Certificaciones Internacionales (`T-08`):** Sección dedicada a credenciales oficiales de Oracle Cloud Infrastructure (OCI Certified AI Foundations Associate), Cisco Networking Academy (Hacker Ético & CTF) e IBM SkillsBuild (Python & Data Analytics).
- **Formación Continua y Base Académica (`T-08`):** Sección con enlaces a Nómada Bootcamp (Full Stack), Oracle Next Education / Alura y la Universidad Nacional Agraria de la Selva (UNAS).
- **Acciones y Descarga Directa de CV (`T-08`):** Incorporación del documento `public/cv.pdf`, botón primario de visualización/descarga segura (`.btn .btn--primary`) y botón secundario de contacto (`.btn .btn--secondary`).
- **Estilos CSS Modulares (`T-08`):** Clases `.sobre-mi-lista`, `.bootcamp-link` y `.sobre-mi-actions` añadidas a `src/styles/global.css` manteniendo la estructura semántica por capas.

### Eliminado
- **Plantilla Placeholder en Inglés (`T-08`):** Eliminación de `src/pages/about.astro` para consolidar la ruta `/sobre-mi/` como estándar canónico del sitio.

---

## [0.6.0] - 2026-11-07

### Añadido
- **Módulo de Datos Centralizado (`T-07`):** Creación de `src/data/projects.ts` como Fuente Única de Verdad (SSOT) tipada con `ImageMetadata`, eliminando duplicación de datos entre vistas.
- **Página de Catálogo de Proyectos (`T-07`):** Creación de `src/pages/proyectos.astro` con renderizado de los 6 proyectos reales usando `ProjectCard.astro`, metadatos SEO y eyebrow `"PROYECTOS PERSONALES"`.
- **Estrategia LCP de Imágenes (`T-07`):** Carga `eager` para las 3 primeras tarjetas del catálogo y `lazy` para el resto.
- **Sección de Contacto GitHub (`T-07`):** Sección `.proyectos-github` con llamada a la acción hacia el perfil de GitHub.
- **Optimización DRY en Portada (`T-07`):** Refactorización de `src/pages/index.astro` para consumir directamente los proyectos destacados desde `src/data/projects.ts`.

---

## [0.5.0] - 2026-11-06

### Añadido
- **Página de Inicio (`T-06`):** Maquetación de `src/pages/index.astro` con Hero profesional, propuesta de valor técnica y botones principales de llamada a la acción (`/proyectos/` y `/contacto/`).
- **Sección de Proyectos Destacados (`T-06`):** Integración de cabecera flex (`.seccion-header`) con enlace al catálogo completo y grilla de 3 proyectos representativos utilizando `ProjectCard.astro`.
- **Estilos de Portada y Botones (`T-06`):** Implementación del sistema de botones reutilizables (`.btn`, `.btn--primary`, `.btn--secondary`), espaciado fluido del hero y grilla adaptable `.proyectos-grid` en `src/styles/global.css`.
- **Documentación de Especificaciones Técnicas:** Formalización de specs en `.reference/specs/` (`T-03`, `T-04`, `T-05` y `T-06`).

---

## [0.4.0] - 2026-11-03

### Añadido
- **Componente Reutilizable ProjectCard (`T-05`):** Creación de `src/components/ProjectCard.astro` con tipado estricto (`ImageMetadata`), renderizado de `<Image />` de `astro:assets` (`640x360`) con `alt` descriptivo y soporte para `<slot />` condicional (`Astro.slots.has("default")`).
- **Componente Atómico Badge (`T-05`):** Creación de `src/components/Badge.astro` para los chips de tecnologías con soporte para modo claro y oscuro.
- **Assets de Proyectos (`T-05`):** Incorporación de catálogo de ilustraciones vectoriales en `src/assets/projects/` (Pomodoro, Markdown-PDF, OmniSpec, Gestor de Biblioteca, Salesforce Admin y Dashboard de Clima).

---

## [0.3.0] - 2026-11-03

### Añadido
- **Layout Base Unificado (`T-04`):** Creación de `src/layouts/BaseLayout.astro` con integración de `<BaseHead />`, `<Header />`, `<Footer />` y gestión de slots.
- **Navegación Fluida con View Transitions (`T-04`):** Integración de `<ClientRouter />` de `astro:transitions` y script en línea preventivo de FOUC para persistencia y sincronización de tema con `astro:after-swap`.
- **Metadatos y SEO por Defecto (`T-04`):** Soporte de props opcionales (`pageTitle`, `description`, `mainClass`, `eyebrow`) con fallbacks a `SITE_TITLE` y `SITE_DESCRIPTION`.
- **Estilos de Estructura de Contenido (`T-04`):** Reglas para `main` (sticky footer con `flex: 1`) y tipografía `.page-eyebrow` en `src/styles/global.css`.
- **Adopción en Inicio (`T-04`):** Actualización de `src/pages/index.astro` para consumir `BaseLayout` con metadatos descriptivos.

---

## [0.2.0] - 2026-11-01

### Añadido
- **Componentes de Encabezado y Navegación (`T-03`):** Creación de `Header.astro`, `Navigation.astro` y `Logo.astro` con soporte para menú móvil responsive, accesibilidad por teclado y enlaces ordenados (Inicio, Sobre mí, Blog, Proyectos, Contacto).
- **Componentes del Pie de Página (`T-03`):** Creación de `Footer.astro`, `Social.astro` y `ThemeToggle.astro` con selector de tema Dark/Light persistente en `localStorage`, enlaces a redes con tooltips accesibles y año dinámico.
- **Estilos de UI Base en CSS (`T-03`):** Estilos para el sticky header, menú hamburguesa con transición cruzada, botones de redes sociales e iconos del selector de tema en `src/styles/global.css`.
- **Assets de Identidad y Redes:** Incorporación de `logo.png` y catálogo de iconos vectoriales SVG en `public/icons/social/`.

---

## [0.1.1] - 2026-10-29

### Añadido
- **Tokens CSS Semánticos (`T-02`):** Implementación de la paleta carmín/carbón en `src/styles/global.css` con variables completas para `:root` (`--color-brand: #d0354f`, `#faf8f8`) y `html.dark` (`--color-brand: #ff526d`, `#141416`).
- **Tipografía Local con Font API (`T-02`):** Aplicación de `--font-atkinson` en `body` vinculada a fuentes locales WOFF de Astro.
- **Grillas Responsivas Fluidas (`T-02`):** Definición de `.proyectos-grid` y `.articulos-grid` con `clamp()` y `minmax()` para adaptación sin media queries forzadas.
- **Infraestructura de Testing:** Configuración de Vitest (`vitest.config.ts`, script `pnpm test`) y pruebas unitarias de validación de tokens y constantes en `tests/unit/`.


---

## [0.1.0] - 2026-10-29

### Añadido
- **Gobernanza y Workflow:** Creación de `docs/workflow.md` con especificaciones de Git Flow unipersonal, Conventional Commits y Definition of Done (DoD).
- **Product Backlog:** Creación de `docs/backlog.md` con 18 tareas atómicas divididas en 5 Sprints con fechas reales (26 oct - 29 nov 2026).
- **Automatización de GitHub:** Script en Python `scripts/create_github_issues.py` con soporte para creación y sincronización de Milestones, Labels e Issues con GitHub CLI.
- **Directivas para Agentes:** Actualización de `AGENTS.md` con reglas estrictas de package manager (`pnpm`), aislamiento de `.reference/`, ramas de feature y verificación DoD.
- **Documentación Principal:** Actualización integral de `README.md` con stack tecnológico, badges oficiales, estructura del proyecto y directivas SemVer.

### Configurado
- Configuración de `.gitignore` para aislar `.reference/`, `dist/`, `.astro/` y dependencias.

