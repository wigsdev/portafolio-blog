# 🚀 Portafolio Personal & Blog

<div align="center">

![Astro](https://img.shields.io/badge/Astro-7.4-FF5D01?style=for-the-badge&logo=astro&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![pnpm](https://img.shields.io/badge/pnpm-9.x-F69220?style=for-the-badge&logo=pnpm&logoColor=white)
![SemVer](https://img.shields.io/badge/SemVer-2.0.0-informational?style=for-the-badge)
![Zero-JS](https://img.shields.io/badge/Architecture-Zero--JS-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

</div>

Sitio web profesional de alto rendimiento desarrollado con **Astro 7.4 (Astro 5 Core)**, **TypeScript** y **Arquitectura de Islas**. Diseñado para maximizar los **Core Web Vitals**, entregar cero JavaScript por defecto (_Zero-JS_) y ofrecer una experiencia fluida mediante **View Transitions**.

Desarrollado y mantenido por **Wilmer Gulcochía ([@wigsdev](https://github.com/wigsdev))**.

---

## 🛠️ Stack Tecnológico

| Capa                         | Tecnologías                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Núcleo & SSG**             | [Astro 7.4](https://astro.build) (Astro 5 Core Engine) con Vite 8                                                        |
| **Lenguaje**                 | JavaScript (ESM) & TypeScript estricto                                                                                   |
| **Estilos & Tipografía**     | CSS Scoped · CSS Tokens (Modo Claro/Oscuro) · Fuente local _Atkinson_ con Astro Font Provider API                        |
| **Contenido Tipado**         | Content Collections (`astro:content` con `loader: glob`) validadas con **Zod** · Soporte Markdown y MDX (`@astrojs/mdx`) |
| **Multimedia & Rendimiento** | Optimización de imágenes con `<Image />` y motor `sharp`                                                                 |
| **Navegación & SPA**         | View Transitions nativas con `<ClientRouter />`                                                                          |
| **Interactividad**           | Arquitectura de Islas con directivas `client:*`                                                                          |
| **Servidor & APIs**          | Endpoints de servidor y validación de formularios                                                                        |
| **SEO & Sindicación**        | Metadatos OpenGraph, Twitter Cards, `@astrojs/sitemap` y feed RSS (`@astrojs/rss`)                                       |

---

## 📁 Estructura del Proyecto

```text
portafolio-blog/
├── docs/                       # Gobernanza, Backlog oficial y Workflow de desarrollo
│   ├── backlog.md              # Catálogo de 17 tareas en 5 Sprints
│   └── workflow.md             # Git Flow unipersonal, Conventional Commits y DoD
├── scripts/                    # Utilidades de automatización
│   └── create_github_issues.py # Sincronización de Milestones y tareas con GitHub CLI
├── public/                     # Assets estáticos directos (favicon, cv.pdf)
├── src/
│   ├── assets/                 # Imágenes procesadas con sharp y fuentes locales
│   ├── components/             # Componentes reutilizables de UI (Header, Footer, Cards)
│   ├── content/                # Colecciones de contenido Markdown/MDX
│   │   └── blog/               # Artículos técnicos publicados
│   ├── layouts/                # BaseLayout con View Transitions y layouts de lectura
│   ├── pages/                  # Enrutamiento basado en archivos y rutas dinámicas
│   └── styles/                 # Variables semánticas globales y resets CSS
├── astro.config.mjs            # Configuración de integraciones, sitemap y fuentes
├── package.json
└── tsconfig.json
```

---

## 🧞 Comandos de Desarrollo

Todos los comandos se ejecutan con **`pnpm`**:

| Comando                                             | Propósito                                              |
| --------------------------------------------------- | ------------------------------------------------------ |
| `pnpm install`                                      | Instala las dependencias del proyecto                  |
| `pnpm astro dev --background`                       | Inicia el servidor de desarrollo en segundo plano      |
| `pnpm astro dev status`                             | Verifica el estado del servidor en background          |
| `pnpm astro dev logs`                               | Muestra los registros del servidor en tiempo real      |
| `pnpm astro dev stop`                               | Detiene el servidor en desarrollo                      |
| `pnpm build`                                        | Compila el sitio estático para producción en `./dist/` |
| `pnpm preview`                                      | Previsualiza localmente el build de producción         |
| `python3 scripts/create_github_issues.py --dry-run` | Simula la creación de issues en GitHub                 |

---

## 📋 Gestión Ágil del Proyecto

El desarrollo se organiza en **5 Sprints** con fechas reales (26 de octubre al 29 de noviembre de 2026):

- **Sprint 1:** Fundamentos, Sistema de Diseño & Layouts Base (Tareas T-01 a T-04).
- **Sprint 2:** Portafolio Personal & Optimización de Imágenes (Tareas T-05 a T-08).
- **Sprint 3:** Blog Técnico, Content Collections & Rutas Dinámicas (Tareas T-09 a T-12).
- **Sprint 4:** Isla Interactiva, Funciones de Servidor, Migración Tailwind & SEO 90+ (Tareas T-13 a T-16).
- **Sprint 5:** Despliegue en Producción & Presentación del Proyecto (Tareas T-17 a T-18).

Consulta el detalle completo en [**`docs/backlog.md`**](docs/backlog.md) y las normas de contribución en [**`docs/workflow.md`**](docs/workflow.md).

---

## 🏷️ Versionado Semántico (SemVer) & Historial de Cambios

Este proyecto se rige estrictamente por la especificación [SemVer 2.0.0](https://semver.org/lang/es/):

```text
MAJOR.MINOR.PATCH
```

- **MAJOR (vX.0.0):** Cambios de arquitectura o modificaciones que rompen compatibilidad retroactiva.
- **MINOR (v0.X.0):** Nuevas funcionalidades, páginas, módulos o endpoints compatibles hacia atrás.
- **PATCH (v0.0.X):** Correcciones de errores, ajustes de estilos o parches de dependencias compatibles.

Todo el historial de versiones, adiciones y correcciones se documenta activamente en [**`CHANGELOG.md`**](CHANGELOG.md) siguiendo la guía de [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## 👤 Autor

**Wilmer Gulcochía**

- **GitHub:** [@wigsdev](https://github.com/wigsdev)
- **LinkedIn:** [wigsdev](https://linkedin.com/in/wigsdev/)
- **Correo:** [karlwgs1989@gmail.com](mailto:karlwgs1989@gmail.com)
