# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning (SemVer 2.0.0)](https://semver.org/lang/es/).

---

## [Unreleased]

### Planificado
- **Sprint 1:** BaseLayout unificado con View Transitions (`<ClientRouter />`) (`T-04`).
- **Sprint 4:** Migración progresiva del sistema de diseño a Tailwind CSS (`T-15`).

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

