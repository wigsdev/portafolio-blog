# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning (SemVer 2.0.0)](https://semver.org/lang/es/).

---

## [Unreleased]

### Planificado
- **Sprint 1:** Tokens CSS globales, modo oscuro/claro y conexión con la fuente *Atkinson* (`T-02`).
- **Sprint 1:** Componentes de navegación y UI base: Header, Footer y ThemeToggle (`T-03`).
- **Sprint 1:** BaseLayout unificado con View Transitions (`<ClientRouter />`) (`T-04`).
- **Sprint 4:** Migración progresiva del sistema de diseño a Tailwind CSS (`T-15`).

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

