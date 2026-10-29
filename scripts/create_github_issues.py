#!/usr/bin/env python3
"""
Portafolio + Blog — Script de Automatización de GitHub Issues y Milestones.

Basado en el Product Backlog oficial:
  - docs/backlog.md

Publica o actualiza el catálogo completo de 18 tareas atómicas organizadas en 5 Sprints:
  - Sprint 1 (26 Oct - 01 Nov 2026): T-01 a T-04 (Fundamentos, Sistema de Diseño & Layouts Base)
  - Sprint 2 (02 Nov - 08 Nov 2026): T-05 a T-08 (Portafolio Personal & Optimización de Imágenes)
  - Sprint 3 (09 Nov - 15 Nov 2026): T-09 a T-12 (Blog Técnico, Content Collections & Rutas Dinámicas)
  - Sprint 4 (16 Nov - 22 Nov 2026): T-13 a T-16 (Isla Interactiva, Funciones de Servidor, Tailwind CSS & SEO 90+)
  - Sprint 5 (23 Nov - 29 Nov 2026): T-17 a T-18 (Despliegue Público, Diapositivas & Sustentación)

Uso:
  python3 scripts/create_github_issues.py [--dry-run] [--repo OWNER/REPO] [--sprint SPRINT_NUM] [--update] [--no-project] [--assignee USUARIO] [--move-status "En progreso"]
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from typing import Any, Dict, List, Optional, Tuple


# ── Configuración de Milestones (5 Semanas Oficiales) ─────────────────────────
MILESTONES = [
    {
        "title": "Sprint 1: Fundamentos, Sistema de Diseño & Layouts Base",
        "description": "Configuración base, variables CSS dark/light, fuente local Atkinson, Header/Footer y BaseLayout con View Transitions (26 Oct - 01 Nov 2026).",
        "due_date": "2026-11-01T23:59:59Z",
    },
    {
        "title": "Sprint 2: Portafolio Personal & Optimización de Imágenes",
        "description": "Componente ProjectCard con slots, página Inicio (Hero + Habilidades), Proyectos con <Image /> y Sobre Mí con descarga de CV (02 Nov - 08 Nov 2026).",
        "due_date": "2026-11-08T23:59:59Z",
    },
    {
        "title": "Sprint 3: Blog Técnico, Content Collections & Rutas Dinámicas",
        "description": "Content Collections con Zod, 5+ artículos, rutas dinámicas [...slug].astro, listado paginado con paginate() y páginas de tags (09 Nov - 15 Nov 2026).",
        "due_date": "2026-11-15T23:59:59Z",
    },
    {
        "title": "Sprint 4: Isla Interactiva, Funciones de Servidor & SEO 90+",
        "description": "Isla interactiva con client:*, formulario de contacto con Server Action o API POST y validación Zod, metadatos SEO y Lighthouse >= 90 (16 Nov - 22 Nov 2026).",
        "due_date": "2026-11-22T23:59:59Z",
    },
    {
        "title": "Sprint 5: Despliegue Público, Diapositivas & Sustentación",
        "description": "Compilación estática limpia, despliegue en producción con URL pública y elaboración de diapositivas de sustentación del proyecto (23 Nov - 29 Nov 2026).",
        "due_date": "2026-11-29T23:59:59Z",
    },
]

# ── Configuración de Labels (Etiquetas por Sprint, Prioridad, Tipo y Estado) ──
LABELS = [
    {"name": "sprint:1", "color": "0E8A16", "description": "Tareas del Sprint 1 (Semana 1)"},
    {"name": "sprint:2", "color": "FBCA04", "description": "Tareas del Sprint 2 (Semana 2)"},
    {"name": "sprint:3", "color": "D93F0B", "description": "Tareas del Sprint 3 (Semana 3)"},
    {"name": "sprint:4", "color": "B60205", "description": "Tareas del Sprint 4 (Semana 4)"},
    {"name": "sprint:5", "color": "5319E7", "description": "Tareas del Sprint 5 (Semana 5)"},
    {"name": "priority: critical", "color": "B60205", "description": "Bloqueante: Base estructural o arquitectura indispensable"},
    {"name": "priority: high", "color": "D93F0B", "description": "Requisito Mínimo del Curso: Esencial para la consigna"},
    {"name": "priority: medium", "color": "FBCA04", "description": "Funcionalidad complementaria o mejora UX"},
    {"name": "priority: low", "color": "0E8A16", "description": "Pulido visual, animaciones opcionales o extras"},
    {"name": "type: structure", "color": "1D76DB", "description": "Configuración, layouts y arquitectura de carpetas"},
    {"name": "type: style", "color": "D4C5F9", "description": "Sistema de diseño, CSS tokens, dark/light y fuentes"},
    {"name": "type: feature", "color": "0052CC", "description": "Componentes de portafolio, blog y rutas dinámicas"},
    {"name": "type: server", "color": "E99695", "description": "Funciones de servidor, endpoints API y validaciones Zod"},
    {"name": "type: presentation", "color": "BFD4F2", "description": "Diapositivas, sustentación y despliegue público"},
    {"name": "status: backlog", "color": "EDEDED", "description": "Tarea definida y lista para ser abordada"},
    {"name": "status: in-progress", "color": "FEF2C0", "description": "Trabajo activo en rama de feature"},
    {"name": "status: in-review", "color": "D8F8C8", "description": "PR abierto o validación de criterios cumplidos"},
]

# ── Catálogo de las 18 Tareas Atómicas del Backlog Oficial ─────────────────────
ISSUES: List[Dict[str, Any]] = [
    # ══════════════════════════════════════════════════════════════════════════
    # SPRINT 1 (26 Oct - 01 Nov 2026): Fundamentos, Sistema de Diseño & Layouts Base
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "T-01",
        "sprint_num": 1,
        "title": "[T-01] Gobernanza, Configuración del Repositorio y Entorno Documental",
        "milestone": "Sprint 1: Fundamentos, Sistema de Diseño & Layouts Base",
        "labels": ["sprint:1", "priority: critical", "type: structure", "status: backlog"],
        "body": """## Descripción
Configurar la base de control de versiones y el ecosistema documental inicial. Asegurar que `.gitignore` aísle `.reference/`, verificar scripts de desarrollo con `pnpm`, y documentar las reglas de Git Flow unipersonal y Conventional Commits.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-01` |
| **Sprint** | Sprint 1 (26 Oct – 01 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: structure` |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `.gitignore`, `package.json`, `docs/backlog.md`, `docs/workflow.md`, `README.md` |
| **Commit Sugerido** | `chore(repo): configurar entorno documental, gitignore y flujo de trabajo` |

## Criterios de Aceptación (DoD)
- [ ] `.gitignore` excluye correctamente `.reference/`, `node_modules/`, `dist/` y `.astro/`.
- [ ] `docs/workflow.md` documenta la convención de ramas, commits y DoD.
- [ ] `README.md` actualizado con descripción del proyecto personal, stack e instrucciones de ejecución.
- [ ] Servidor de desarrollo validado en modo background (`pnpm astro dev --background`).
""",
    },
    {
        "id": "T-02",
        "sprint_num": 1,
        "title": "[T-02] Sistema de Tokens CSS, Soporte Dark/Light y Fuente con Font API",
        "milestone": "Sprint 1: Fundamentos, Sistema de Diseño & Layouts Base",
        "labels": ["sprint:1", "priority: critical", "type: style", "status: backlog"],
        "body": """## Descripción
Definir las variables globales CSS en `src/styles/global.css` adaptadas del portafolio de referencia (paleta de colores moderna para modo claro y modo oscuro, espaciados y sombras). Conectar la fuente local *Atkinson* (`--font-atkinson`) configurada en `astro.config.mjs` vía `fontProviders.local()` para cumplir con el Requisito R2.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-02` |
| **Sprint** | Sprint 1 (26 Oct – 01 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: style` |
| **Requisito Oficial** | R2 (Estilos scoped/globales y Font API) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `astro.config.mjs`, `src/styles/global.css`, `src/assets/fonts/*` |
| **Commit Sugerido** | `style(design): implementar tokens CSS globales, tema dark/light y fuente atkinson` |

## Criterios de Aceptación (DoD)
- [ ] Paleta semántica de variables CSS (`--color-bg`, `--color-text`, `--color-brand`, `--color-surface`) disponible para modos claro y oscuro.
- [ ] La fuente local *Atkinson* se aplica fluidamente en toda la aplicación mediante la variable `--font-atkinson`.
- [ ] Estilos globales con reset moderno y tipografía base accesible.
""",
    },
    {
        "id": "T-03",
        "sprint_num": 1,
        "title": "[T-03] Componentes de Navegación y UI Base (Header, Footer, ThemeToggle)",
        "milestone": "Sprint 1: Fundamentos, Sistema de Diseño & Layouts Base",
        "labels": ["sprint:1", "priority: high", "type: structure", "status: backlog"],
        "body": """## Descripción
Crear la estructura reutilizable de encabezado y pie de página. Integrar `ThemeToggle.astro` con script sincronizado a los eventos de Astro (`astro:after-swap` y `astro:page-load`) para alternar el tema sin parpadeos, y enlaces de navegación hacia Inicio, Proyectos, Blog y Contacto.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-03` |
| **Sprint** | Sprint 1 (26 Oct – 01 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: structure` |
| **Requisito Oficial** | R1 (Componentes reutilizables) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/components/Header.astro`, `src/components/Navigation.astro`, `src/components/Footer.astro`, `src/components/Social.astro`, `src/components/ThemeToggle.astro` |
| **Commit Sugerido** | `feat(ui): crear componentes header, footer, navigation y themetoggle con soporte after-swap` |

## Criterios de Aceptación (DoD)
- [ ] `Header.astro` muestra el logo personal de Wilmer y el menú de navegación adaptable.
- [ ] `ThemeToggle.astro` cambia entre modo oscuro y claro persistiendo en `localStorage`.
- [ ] `Footer.astro` incluye enlaces a redes sociales (GitHub, LinkedIn, Email) y año dinámico.
- [ ] Menú accesible con navegación por teclado y contraste adecuado.
""",
    },
    {
        "id": "T-04",
        "sprint_num": 1,
        "title": "[T-04] Layout Base Unificado con View Transitions y Metadatos SEO",
        "milestone": "Sprint 1: Fundamentos, Sistema de Diseño & Layouts Base",
        "labels": ["sprint:1", "priority: critical", "type: structure", "status: backlog"],
        "body": """## Descripción
Construir `src/layouts/BaseLayout.astro` reutilizable con props tipadas (`pageTitle`, `description`, `eyebrow`, `mainClass`) y slots semánticos. Incorporar `<ClientRouter />` (`astro:transitions`) para navegación SPA suave sin recarga completa de página, cumpliendo los Requisitos R1 y R7.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-04` |
| **Sprint** | Sprint 1 (26 Oct – 01 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: structure` |
| **Requisito Oficial** | R1 (Layout base reutilizable) y R7 (View Transitions) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/layouts/BaseLayout.astro`, `src/components/BaseHead.astro` |
| **Commit Sugerido** | `feat(layout): implementar BaseLayout unificado con ClientRouter para View Transitions` |

## Criterios de Aceptación (DoD)
- [ ] `BaseLayout.astro` encapsula `<BaseHead />`, `<Header />`, `<main>`, `<slot />` y `<Footer />`.
- [ ] `<ClientRouter />` opera correctamente y las transiciones entre páginas no provocan reseteo del tema oscuro/claro.
- [ ] Soporte para `props` y `slot` verificado con TypeScript.
""",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPRINT 2 (02 Nov - 08 Nov 2026): Portafolio Personal & Optimización de Imágenes
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "T-05",
        "sprint_num": 2,
        "title": "[T-05] Componente Reutilizable ProjectCard con Props, Slots y <Image />",
        "milestone": "Sprint 2: Portafolio Personal & Optimización de Imágenes",
        "labels": ["sprint:2", "priority: high", "type: feature", "status: backlog"],
        "body": """## Descripción
Desarrollar el componente `ProjectCard.astro` para representar proyectos. Debe tipar sus props con TypeScript (usando `ImageMetadata`), optimizar la imagen con el componente `<Image />` de `astro:assets` (`loading=\"eager\"` para los primeros y `\"lazy\"` para el resto), chips de tecnologías y un `<slot />` opcional para notas o métricas destacadas (Requisitos R1 y R5).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-05` |
| **Sprint** | Sprint 2 (02 Nov – 08 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R1 (Componente reutilizable) y R5 (Imágenes optimizadas) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/components/ProjectCard.astro`, `src/components/Badge.astro` |
| **Commit Sugerido** | `feat(components): crear ProjectCard con Image de astro:assets, tipado estricto y slot` |

## Criterios de Aceptación (DoD)
- [ ] Props estrictamente tipadas con TypeScript (`nombre`, `descripcion`, `tecnologias`, `imagen`, `demoUrl`, `githubUrl`).
- [ ] Uso exclusivo de `<Image />` de `astro:assets` con dimensiones explícitas y atributo `alt`.
- [ ] Implementación de `<slot />` para contenido extra personalizado.
""",
    },
    {
        "id": "T-06",
        "sprint_num": 2,
        "title": "[T-06] Página de Inicio (Hero, Perfil Profesional y Proyectos Destacados)",
        "milestone": "Sprint 2: Portafolio Personal & Optimización de Imágenes",
        "labels": ["sprint:2", "priority: high", "type: feature", "status: backlog"],
        "body": """## Descripción
Maquetar la página de inicio principal (`/`) integrando la identidad de Wilmer Gulcochía (`PERFIL.md`): propuesta de valor como desarrollador Frontend & Web con Astro/TypeScript e IA, badges de stack técnico, llamada a la acción y un grid con proyectos representativos.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-06` |
| **Sprint** | Sprint 2 (02 Nov – 08 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/index.astro` |
| **Commit Sugerido** | `feat(pages): maquetar index con hero profesional, stack tecnológico y proyectos destacados` |

## Criterios de Aceptación (DoD)
- [ ] Hero section con presentación clara, roles y enlaces a contacto y proyectos.
- [ ] Sección de tecnologías clave y enfoque técnico.
- [ ] Sección de proyectos destacados reutilizando `ProjectCard.astro`.
- [ ] Enlace directo a los últimos artículos del blog.
""",
    },
    {
        "id": "T-07",
        "sprint_num": 2,
        "title": "[T-07] Página de Proyectos con Catálogo Completo y Assets Optimizados",
        "milestone": "Sprint 2: Portafolio Personal & Optimización de Imágenes",
        "labels": ["sprint:2", "priority: high", "type: feature", "status: backlog"],
        "body": """## Descripción
Migrar los 6 proyectos reales desde `.reference/portafolio-astro` (Pomodoro, Markdown-PDF, OmniSpec IA, Gestor de Biblioteca, Salesforce Admin, Weather Dashboard) con sus imágenes a `src/assets/projects/`. Crear la página `/proyectos` que itere el catálogo con `map()`.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-07` |
| **Sprint** | Sprint 2 (02 Nov – 08 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R5 (Imágenes optimizadas en catálogo) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/proyectos.astro`, `src/assets/projects/*` |
| **Commit Sugerido** | `feat(pages): publicar catalogo de proyectos con 6 casos reales y assets optimizados` |

## Criterios de Aceptación (DoD)
- [ ] Los 6 proyectos renderizan sin errores con descripciones precisas, tags y enlaces a GitHub y demos.
- [ ] Todas las imágenes se procesan con `sharp` y el componente `<Image />`.
- [ ] Grid adaptable a móviles, tablets y monitores de escritorio.
""",
    },
    {
        "id": "T-08",
        "sprint_num": 2,
        "title": "[T-08] Página Sobre Mí, Trayectoria y Descarga de CV en PDF",
        "milestone": "Sprint 2: Portafolio Personal & Optimización de Imágenes",
        "labels": ["sprint:2", "priority: medium", "type: feature", "status: backlog"],
        "body": """## Descripción
Crear la página `/sobre-mi` con la historia profesional de Wilmer, enfoque de arquitectura de software, certificaciones internacionales (Oracle OCI AI, Cisco Ethical Hacker, IBM Data Science) y botón de descarga directa de CV en PDF alojado en `public/`.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-08` |
| **Sprint** | Sprint 2 (02 Nov – 08 Nov 2026) |
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: feature` |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/sobre-mi.astro`, `public/cv.pdf` |
| **Commit Sugerido** | `feat(pages): crear pagina sobre-mi con credenciales tecnicas y enlace a cv en pdf` |

## Criterios de Aceptación (DoD)
- [ ] Contenido estructurado de formación, certificaciones y experiencia.
- [ ] Enlace de descarga funcional hacia `/cv.pdf` ubicado en `public/`.
- [ ] Enlaces a redes y plataformas técnicas (CodePen, GitHub, LinkedIn).
""",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPRINT 3 (09 Nov - 15 Nov 2026): Blog Técnico, Content Collections & Rutas Dinámicas
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "T-09",
        "sprint_num": 3,
        "title": "[T-09] Configuración de Colección de Contenido con Zod y Entradas Reales",
        "milestone": "Sprint 3: Blog Técnico, Content Collections & Rutas Dinámicas",
        "labels": ["sprint:3", "priority: critical", "type: feature", "status: backlog"],
        "body": """## Descripción
Configurar la colección `blog` en `src/content.config.ts` utilizando la nueva API de Astro 5 (`loader: glob`) con validación Zod estricta: `title`, `description`, `pubDate`, `updatedDate`, `heroImage`, y el campo de array `tags: z.array(z.string()).default([])`. Contar con al menos 5 artículos técnicos reales con temática de desarrollo moderno (Requisito R3).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-09` |
| **Sprint** | Sprint 3 (09 Nov – 15 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R3 (Colección de contenido con Zod y >= 5 entradas) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/content.config.ts`, `src/content/blog/*` |
| **Commit Sugerido** | `feat(content): configurar coleccion blog con zod loader y 5 articulos con tags` |

## Criterios de Aceptación (DoD)
- [ ] Esquema Zod validando tipos de datos obligatorios y opcionales.
- [ ] Mínimo 5 artículos `.md` y `.mdx` en `src/content/blog/` pasando la validación sin errores de build.
- [ ] Cada artículo contiene etiquetas (`tags`) coherentes para la taxonomía.
""",
    },
    {
        "id": "T-10",
        "sprint_num": 3,
        "title": "[T-10] Plantilla de Lectura de Artículo con Layout y Renderizado Markdown/MDX",
        "milestone": "Sprint 3: Blog Técnico, Content Collections & Rutas Dinámicas",
        "labels": ["sprint:3", "priority: high", "type: feature", "status: backlog"],
        "body": """## Descripción
Adaptar el layout de lectura de post `src/layouts/BlogPost.astro` y la página dinámica `src/pages/blog/[...slug].astro`. Debe mostrar imagen de cabecera (`<Image />`), fecha con `FormattedDate.astro`, tiempo de lectura estimado, etiquetas que enlazan a sus páginas de tags y cuerpo del post con soporte de sintaxis resaltada y componentes MDX.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-10` |
| **Sprint** | Sprint 3 (09 Nov – 15 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R3 (Renderizado de colecciones) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/layouts/BlogPost.astro`, `src/pages/blog/[...slug].astro` |
| **Commit Sugerido** | `feat(blog): implementar plantilla de lectura BlogPost con soporte MDX y render de astro:content` |

## Criterios de Aceptación (DoD)
- [ ] Renderizado dinámico de artículos con `render(post)` de `astro:content`.
- [ ] Presentación tipográfica legible y adaptable (`prose`).
- [ ] Lista de tags clickeables que redirigen a `/blog/tags/[tag]`.
""",
    },
    {
        "id": "T-11",
        "sprint_num": 3,
        "title": "[T-11] Listado Paginado del Blog con paginate() y getStaticPaths()",
        "milestone": "Sprint 3: Blog Técnico, Content Collections & Rutas Dinámicas",
        "labels": ["sprint:3", "priority: critical", "type: feature", "status: backlog"],
        "body": """## Descripción
Implementar la ruta `src/pages/blog/[...page].astro` empleando la función `paginate()` dentro de `getStaticPaths()` para cumplir con el Requisito R4. Componente `Pagination.astro` con enlaces a página anterior/siguiente y números de página.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-11` |
| **Sprint** | Sprint 3 (09 Nov – 15 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R4 (Listado paginado con getStaticPaths) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/blog/[...page].astro`, `src/components/BlogCard.astro`, `src/components/Pagination.astro` |
| **Commit Sugerido** | `feat(blog): implementar listado paginado con paginate() de getStaticPaths` |

## Criterios de Aceptación (DoD)
- [ ] `getStaticPaths()` utiliza `paginate()` configurando un límite por página (ej. 3 o 4 posts).
- [ ] Rutas generadas correctamente (`/blog/`, `/blog/2`, etc.).
- [ ] Controles de paginación accesibles y deshabilitados cuando no hay página previa/siguiente.
""",
    },
    {
        "id": "T-12",
        "sprint_num": 3,
        "title": "[T-12] Rutas Dinámicas de Taxonomía por Etiquetas (/blog/tags/[tag])",
        "milestone": "Sprint 3: Blog Técnico, Content Collections & Rutas Dinámicas",
        "labels": ["sprint:3", "priority: high", "type: feature", "status: backlog"],
        "body": """## Descripción
Inspirándose en la estructura actualizada de `.reference/tutorial-blog`, crear la página `src/pages/blog/tags/[tag].astro` con `getStaticPaths()` consumiendo `getCollection('blog')` para filtrar posts por etiqueta, y la página índice `src/pages/blog/tags/index.astro` con la nube completa de etiquetas (Requisito R4).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-12` |
| **Sprint** | Sprint 3 (09 Nov – 15 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R4 (Rutas dinámicas con getStaticPaths) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/blog/tags/[tag].astro`, `src/pages/blog/tags/index.astro` |
| **Commit Sugerido** | `feat(blog): agregar rutas dinamicas por tag y nube de etiquetas con getStaticPaths` |

## Criterios de Aceptación (DoD)
- [ ] `getStaticPaths()` extrae los tags únicos de toda la colección y filtra los posts asociados.
- [ ] `/blog/tags/[tag]` renderiza únicamente los artículos asociados al tag consultado.
- [ ] Nube de etiquetas en `/blog/tags/` con conteo de artículos por tag.
""",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPRINT 4 (16 Nov - 22 Nov 2026): Isla Interactiva, Funciones de Servidor & SEO 90+
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "T-13",
        "sprint_num": 4,
        "title": "[T-13] Componente de Isla Interactiva con Directiva client:*",
        "milestone": "Sprint 4: Isla Interactiva, Funciones de Servidor & SEO 90+",
        "labels": ["sprint:4", "priority: critical", "type: feature", "status: backlog"],
        "body": """## Descripción
Implementar una isla interactiva de framework UI (Preact o React) con hidratación parcial mediante directiva `client:load` o `client:visible` para cumplir con el Requisito R6. Puede ser un filtro dinámico instantáneo de proyectos por tecnología o un buscador en vivo de artículos del blog.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-13` |
| **Sprint** | Sprint 4 (16 Nov – 22 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: feature` |
| **Requisito Oficial** | R6 (Isla interactiva con client:*) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/components/InteractiveFilter.jsx` (o `.tsx`), página receptora (`proyectos.astro` o `blog/index.astro`) |
| **Commit Sugerido** | `feat(islands): integrar isla interactiva con directiva client:load para filtrado en vivo` |

## Criterios de Aceptación (DoD)
- [ ] Componente interactivo utilizando hooks de estado (`useState`).
- [ ] Inclusión en página con directiva `client:load` o `client:visible`.
- [ ] El resto de la página permanece con 0 KB de JavaScript.
""",
    },
    {
        "id": "T-14",
        "sprint_num": 4,
        "title": "[T-14] Formulario de Contacto con Función de Servidor y Validación Zod",
        "milestone": "Sprint 4: Isla Interactiva, Funciones de Servidor & SEO 90+",
        "labels": ["sprint:4", "priority: critical", "type: server", "status: backlog"],
        "body": """## Descripción
Desarrollar la página `/contacto` integrando un formulario funcional que envíe datos a una función de servidor: Astro Action o Endpoint API POST (`/api/contact`) con validación de datos en servidor mediante esquema Zod (`nombre`, `email`, `mensaje`), retornando respuestas estructuradas de éxito o error (Requisito R8).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-14` |
| **Sprint** | Sprint 4 (16 Nov – 22 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: server` |
| **Requisito Oficial** | R8 (Función de servidor: Formulario con Action o Endpoint y validación) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/contacto.astro`, `src/pages/api/contact.ts` (o `src/actions/index.ts`) |
| **Commit Sugerido** | `feat(server): implementar endpoint POST /api/contact con validacion de esquema Zod` |

## Criterios de Aceptación (DoD)
- [ ] Formulario con campos de nombre, email, asunto y mensaje, con accesibilidad de labels e inputs.
- [ ] Endpoint o Action que procesa la petición y valida con Zod en servidor.
- [ ] Mensajes claros de validación (campos requeridos, formato de correo) y feedback de confirmación al usuario.
""",
    },
    {
        "id": "T-15",
        "sprint_num": 4,
        "title": "[T-15] Migración Progresiva del Sistema de Diseño a Tailwind CSS",
        "milestone": "Sprint 4: Isla Interactiva, Funciones de Servidor & SEO 90+",
        "labels": ["sprint:4", "priority: medium", "type: style", "status: backlog"],
        "body": """## Descripción
Instalar y configurar la integración oficial de Tailwind CSS en Astro. Migrar progresivamente los componentes centrales (Header, ProjectCard, BlogCard) y utilidades de espaciado a clases de Tailwind, manteniendo la compatibilidad con las variables semánticas de color dark/light y la fuente local *Atkinson*, evaluando el impacto en el bundle generado (Requisito R2).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-15` |
| **Sprint** | Sprint 4 (16 Nov – 22 Nov 2026) |
| **Prioridad** | `priority: medium` |
| **Tipo** | `type: style` |
| **Requisito Oficial** | R2 (Estilos con Tailwind CSS y Font API) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `astro.config.mjs`, `package.json`, `tailwind.config.mjs`, componentes clave |
| **Commit Sugerido** | `refactor(style): integrar tailwind css y migrar componentes manteniendo tokens y fuentes` |

## Criterios de Aceptación (DoD)
- [ ] Integración de Tailwind instalada y configurada en `astro.config.mjs`.
- [ ] Variables CSS de `docs/diseno.md` mapeadas en la configuración de tema de Tailwind.
- [ ] Componentes clave refactorizados a utilidades de Tailwind conservando fidelidad visual y responsive.
- [ ] `pnpm build` compila con purga JIT limpia y sin errores de estilos.
""",
    },
    {
        "id": "T-16",
        "sprint_num": 4,
        "title": "[T-16] Auditoría SEO, Sitemap, Feed RSS y Meta Lighthouse >= 90",
        "milestone": "Sprint 4: Isla Interactiva, Funciones de Servidor & SEO 90+",
        "labels": ["sprint:4", "priority: high", "type: structure", "status: backlog"],
        "body": """## Descripción
Configurar `@astrojs/sitemap` y el feed RSS en `/rss.xml`. Verificar etiquetas OpenGraph, Twitter cards y canonicals en todas las páginas. Ejecutar auditoría Lighthouse y optimizar Core Web Vitals (LCP, CLS, INP) para garantizar un puntaje >= 90 en Rendimiento, Accesibilidad y SEO (Requisito R9).

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-16` |
| **Sprint** | Sprint 4 (16 Nov – 22 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: structure` |
| **Requisito Oficial** | R9 (SEO, sitemap y Lighthouse >= 90) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `src/pages/rss.xml.js`, `astro.config.mjs`, componentes de metadatos |
| **Commit Sugerido** | `chore(seo): configurar sitemap, rss feed y optimizar core web vitals para lighthouse 90+` |

## Criterios de Aceptación (DoD)
- [ ] `sitemap-index.xml` y `rss.xml` generados correctamente en el build de producción.
- [ ] Meta tags OpenGraph y Twitter en todas las páginas.
- [ ] Puntaje de Lighthouse >= 90 verificado en Rendimiento y Accesibilidad.
""",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SPRINT 5 (23 Nov - 29 Nov 2026): Despliegue Público, Diapositivas & Sustentación
    # ══════════════════════════════════════════════════════════════════════════
    {
        "id": "T-17",
        "sprint_num": 5,
        "title": "[T-17] Compilación Limpia y Despliegue en Producción con URL Pública",
        "milestone": "Sprint 5: Despliegue Público, Diapositivas & Sustentación",
        "labels": ["sprint:5", "priority: critical", "type: presentation", "status: backlog"],
        "body": """## Descripción
Validar que `pnpm build` compile sin ningún error ni advertencias en estático. Desplegar en plataforma de hosting con SSL activo y URL pública accesible (Vercel, Netlify o Cloudflare Pages), cumpliendo el Requisito R10.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-17` |
| **Sprint** | Sprint 5 (23 Nov – 29 Nov 2026) |
| **Prioridad** | `priority: critical` |
| **Tipo** | `type: presentation` |
| **Requisito Oficial** | R10 (Sitio desplegado públicamente y repositorio) |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `astro.config.mjs`, `package.json`, configuraciones de hosting |
| **Commit Sugerido** | `chore(deploy): verificar build estatico y desplegar sitio en produccion con url publica` |

## Criterios de Aceptación (DoD)
- [ ] `pnpm build` exitoso con salida estática en `dist/`.
- [ ] Sitio desplegado y navegable en URL pública en producción.
- [ ] Todas las rutas, imágenes optimizadas y el formulario de servidor funcionan correctamente en la URL pública.
""",
    },
    {
        "id": "T-18",
        "sprint_num": 5,
        "title": "[T-18] Diapositivas de Presentación y Guía de Sustentación del Proyecto",
        "milestone": "Sprint 5: Despliegue Público, Diapositivas & Sustentación",
        "labels": ["sprint:5", "priority: high", "type: presentation", "status: backlog"],
        "body": """## Descripción
Elaborar la presentación ejecutiva del proyecto final para la sesión de sustentación. Redactar las diapositivas en Markdown y generar la versión HTML interactiva con Reveal.js o similar, documentando arquitectura, cumplimiento de los 10 requisitos de la consigna y demo en vivo.

## Metadata
| Campo | Valor |
|---|---|
| **ID Tarea** | `T-18` |
| **Sprint** | Sprint 5 (23 Nov – 29 Nov 2026) |
| **Prioridad** | `priority: high` |
| **Tipo** | `type: presentation` |
| **Asignado a** | Wilmer (@wigsdev) |
| **Archivos afectados** | `docs/diapositivas-presentacion.md`, `docs/diapositivas-presentacion.html`, `docs/guia-demostracion.md` |
| **Commit Sugerido** | `docs(presentation): crear diapositivas html y guia de sustentacion para presentacion final` |

## Criterios de Aceptación (DoD)
- [ ] `docs/diapositivas-presentacion.html` interactiva y lista para proyectar.
- [ ] Cobertura de arquitectura de islas, Zero-JS, View Transitions, colecciones, servidor y migración a Tailwind.
- [ ] Guía paso a paso de demostración para la sustentación final.
""",
    },
]


# ── Funciones de Utilidad y Ejecución con GitHub CLI ──────────────────────────

def run_command(cmd: List[str]) -> subprocess.CompletedProcess:
    """Ejecuta un comando en el sistema y retorna su resultado."""
    return subprocess.run(cmd, capture_output=True, text=True, check=True)


def check_gh_installed() -> bool:
    """Verifica si GitHub CLI ('gh') está disponible en el PATH."""
    try:
        run_command(["gh", "--version"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_gh_auth() -> bool:
    """Verifica si el usuario ha iniciado sesión en GitHub CLI."""
    try:
        res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        return res.returncode == 0
    except FileNotFoundError:
        return False


def detect_git_repo() -> Optional[str]:
    """Intenta detectar el OWNER/REPO a partir de git remote origin."""
    try:
        res = run_command(["git", "remote", "get-url", "origin"])
        url = res.stdout.strip()
        # Formatos comunes: git@github.com:OWNER/REPO.git o https://github.com/OWNER/REPO.git
        if "github.com" in url:
            part = url.split("github.com")[-1].lstrip(":/")
            if part.endswith(".git"):
                part = part[:-4]
            return part
    except Exception:
        pass
    return None


def ensure_milestones(repo: str, dry_run: bool = False) -> None:
    """Crea los milestones en el repositorio de GitHub si no existen usando la API REST de GitHub."""
    print(f"\n📌 Verificando Milestones (Sprints) en {repo}...")
    existing_titles = set()
    if not dry_run:
        try:
            res = run_command(["gh", "api", f"repos/{repo}/milestones", "--paginate", "--jq", ".[].title"])
            existing_titles = set(res.stdout.strip().splitlines())
        except subprocess.CalledProcessError as e:
            err = e.stderr.strip() if e.stderr else str(e)
            print(f"⚠️ Error al listar milestones: {err}")

    for m in MILESTONES:
        if m["title"] in existing_titles:
            print(f"  ✓ Milestone existente: {m['title']}")
        else:
            if dry_run:
                print(f"  [DRY-RUN] Se crearía milestone: {m['title']}")
            else:
                try:
                    payload = {
                        "title": m["title"],
                        "description": m["description"],
                    }
                    if "due_date" in m:
                        payload["due_on"] = m["due_date"]

                    cmd = [
                        "gh", "api", f"repos/{repo}/milestones",
                        "-X", "POST",
                        "-f", f"title={payload['title']}",
                        "-f", f"description={payload['description']}",
                    ]
                    if "due_on" in payload:
                        cmd.extend(["-f", f"due_on={payload['due_on']}"])

                    run_command(cmd)
                    print(f"  ✓ Creado milestone: {m['title']}")
                except subprocess.CalledProcessError as e:
                    err = e.stderr.strip() if e.stderr else str(e)
                    print(f"  ⚠️ Error creando milestone '{m['title']}': {err}")


def ensure_labels(repo: str, dry_run: bool = False) -> None:
    """Crea o actualiza las etiquetas necesarias en GitHub."""
    print(f"\n🏷️ Verificando Labels en {repo}...")
    existing_labels = set()
    if not dry_run:
        try:
            res = run_command(["gh", "label", "list", "--repo", repo, "--json", "name", "--limit", "100"])
            labels_data = json.loads(res.stdout)
            existing_labels = {l["name"].lower() for l in labels_data}
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Error al listar labels: {e.stderr.strip()}")

    for lbl in LABELS:
        name_lower = lbl["name"].lower()
        if name_lower in existing_labels:
            print(f"  ✓ Label existente: {lbl['name']}")
        else:
            if dry_run:
                print(f"  [DRY-RUN] Se crearía label: {lbl['name']} (Color: #{lbl['color']})")
            else:
                try:
                    run_command([
                        "gh", "label", "create", lbl["name"],
                        "--repo", repo,
                        "--color", lbl["color"],
                        "--description", lbl.get("description", "")
                    ])
                    print(f"  ✓ Creada label: {lbl['name']}")
                except subprocess.CalledProcessError as e:
                    print(f"  ⚠️ Error creando label '{lbl['name']}': {e.stderr.strip()}")


def ensure_project(owner: str, title: str, dry_run: bool = False) -> Optional[int]:
    """Crea o localiza un GitHub Project (Project v2) en la cuenta del usuario."""
    print(f"\n📊 Verificando GitHub Project '{title}' para el propietario '{owner}'...")
    if dry_run:
        print(f"  [DRY-RUN] Se crearía o vincularía el GitHub Project: '{title}' (owner: {owner})")
        return 1

    try:
        res = run_command(["gh", "project", "list", "--owner", owner, "--format", "json"])
        data = json.loads(res.stdout)
        projects = data.get("projects", [])
        for p in projects:
            if p.get("title") == title:
                print(f"  ✓ Proyecto existente encontrado: #{p['number']} - '{title}'")
                return p["number"]

        # Si no existe, crearlo
        create_res = run_command(["gh", "project", "create", "--owner", owner, "--title", title, "--format", "json"])
        created = json.loads(create_res.stdout)
        p_num = created.get("number")
        print(f"  ✓ Nuevo GitHub Project creado: #{p_num} - '{title}'")
        return p_num
    except subprocess.CalledProcessError as e:
        err = e.stderr.strip() if e.stderr else str(e)
        print(f"  ⚠️ No se pudo gestionar el GitHub Project automáticamente: {err}")
        print("     Consejo: Si el error es de permisos, ejecuta: 'gh auth refresh -s project'")
        return None
    except Exception as e:
        print(f"  ⚠️ Advertencia al verificar project: {e}")
        return None


def add_issue_to_project(owner: str, project_num: int, issue_url: str, dry_run: bool = False) -> None:
    """Añade una issue creada a un GitHub Project."""
    if dry_run:
        print(f"    ↳ [DRY-RUN] Se añadiría al Project #{project_num}")
        return

    try:
        run_command(["gh", "project", "item-add", str(project_num), "--owner", owner, "--url", issue_url])
        print(f"    ↳ ✓ Añadida al Project #{project_num}")
    except subprocess.CalledProcessError as e:
        msg = e.stderr.strip() if e.stderr else str(e)
        if "already" in msg.lower():
            print(f"    ↳ ℹ️ Ya vinculada al Project #{project_num}")
        else:
            print(f"    ↳ ⚠️ Advertencia al vincular al Project #{project_num}: {msg}")


def move_project_items_to_status(owner: str, project_num: int, target_status_name: str = "En progreso", dry_run: bool = False) -> None:
    """Mueve todas las tarjetas del Project Board a la columna especificada (por defecto 'En progreso')."""
    print(f"\n📋 Moviendo tarjetas del Project Board #{project_num} a la columna '{target_status_name}'...")
    if dry_run:
        print(f"  [DRY-RUN] Se consultarían los ítems del Project #{project_num} y se moverían a '{target_status_name}'")
        return

    try:
        # 1. Obtener el ID de nodo global del proyecto (PVT_...)
        view_raw = run_command(["gh", "project", "view", str(project_num), "--owner", owner, "--format", "json"])
        view_data = json.loads(view_raw.stdout)
        project_id = view_data.get("id")

        if not project_id:
            print("  ⚠️ No se pudo obtener el ID global del proyecto.")
            return

        # 2. Obtenemos los campos del proyecto para localizar el campo Status
        fields_raw = run_command(["gh", "project", "field-list", str(project_num), "--owner", owner, "--format", "json"])
        fields_data = json.loads(fields_raw.stdout)

        status_field = next((f for f in fields_data.get("fields", []) if f.get("name") in ["Status", "Estado"]), None)
        if not status_field:
            print("  ⚠️ No se encontró el campo 'Status' o 'Estado' en el Project Board.")
            return

        status_field_id = status_field.get("id")
        options = status_field.get("options", [])

        # Buscar la opción que coincida con target_status_name
        target_opt = next((o for o in options if target_status_name.lower() in o.get("name", "").lower() or o.get("name", "").lower() in target_status_name.lower()), None)

        if not target_opt:
            available = [o.get("name") for o in options]
            print(f"  ⚠️ No se encontró la columna '{target_status_name}'. Opciones disponibles: {available}")
            return

        target_opt_id = target_opt["id"]
        col_name = target_opt.get("name")
        print(f"  ✓ Columna detectada: '{col_name}' (ID de opción: {target_opt_id})")

        # 3. Listar ítems del proyecto
        items_raw = run_command(["gh", "project", "item-list", str(project_num), "--owner", owner, "--format", "json"])
        items_data = json.loads(items_raw.stdout)
        items = items_data.get("items", [])

        print(f"  🚀 Moviendo {len(items)} tarjetas a '{col_name}'...")
        updated_count = 0
        for item in items:
            item_id = item["id"]
            content = item.get("content", {})
            title = content.get("title") or item.get("title") or item_id
            try:
                run_command([
                    "gh", "project", "item-edit",
                    "--id", item_id,
                    "--field-id", status_field_id,
                    "--single-select-option-id", target_opt_id,
                    "--project-id", project_id
                ])
                print(f"    ✓ {title} -> {col_name}")
                updated_count += 1
            except subprocess.CalledProcessError as e:
                err = e.stderr.strip() if e.stderr else str(e)
                print(f"    ⚠️ Error al mover '{title}': {err}")

        print(f"  ✨ {updated_count}/{len(items)} tarjetas ahora están en la columna '{col_name}'.")

    except Exception as e:
        print(f"  ⚠️ Error al gestionar tarjetas en el Project Board: {e}")


def get_existing_issues(repo: str) -> Dict[str, Dict[str, Any]]:
    """Obtiene issues existentes indexadas por su prefijo [ID]."""
    try:
        res = run_command([
            "gh", "issue", "list",
            "--repo", repo,
            "--state", "all",
            "--limit", "100",
            "--json", "number,title,state,body"
        ])
        issues_data = json.loads(res.stdout)
        mapping = {}
        for item in issues_data:
            title = item.get("title", "")
            if title.startswith("[") and "]" in title:
                tag = title[1:title.index("]")].strip()
                mapping[tag] = item
        return mapping
    except subprocess.CalledProcessError as e:
        print(f"⚠️ No se pudieron obtener las issues existentes: {e.stderr.strip()}")
        return {}


def create_or_update_issues(
    repo: str,
    dry_run: bool = False,
    update: bool = False,
    sprint_filter: Optional[int] = None,
    assignee: Optional[str] = "@me",
    project_num: Optional[int] = None,
    owner: str = "wigsdev"
) -> None:
    """Crea o actualiza las tareas en GitHub Issues y las asocia al Project Board."""
    target_issues = ISSUES
    if sprint_filter is not None:
        target_issues = [i for i in ISSUES if i.get("sprint_num") == sprint_filter]
        print(f"\n🎯 Filtrando únicamente tareas del Sprint {sprint_filter} ({len(target_issues)} tareas)")

    print(f"\n🚀 Procesando {len(target_issues)} tareas para {repo}...")
    if assignee:
        print(f"👤 Autoasignando tareas a: {assignee}")
    existing = get_existing_issues(repo) if not dry_run else {}

    processed = 0
    for issue in target_issues:
        task_id = issue["id"]
        if task_id in existing:
            num = existing[task_id]["number"]
            state = existing[task_id]["state"]
            if update:
                if dry_run:
                    print(f"  [DRY-RUN] Se actualizaría {task_id} (#{num}) (asignada a: {assignee or 'sin cambios'})")
                    if project_num:
                        add_issue_to_project(owner, project_num, f"https://github.com/{repo}/issues/{num}", dry_run=True)
                else:
                    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".md", encoding="utf-8") as f:
                        f.write(issue["body"])
                        temp_body = f.name
                    try:
                        cmd = [
                            "gh", "issue", "edit", str(num),
                            "--repo", repo,
                            "--title", issue["title"],
                            "--body-file", temp_body,
                            "--milestone", issue["milestone"],
                        ]
                        if assignee:
                            cmd.extend(["--add-assignee", assignee])
                        for lbl in issue["labels"]:
                            cmd.extend(["--add-label", lbl])
                        run_command(cmd)
                        print(f"  ✓ {task_id} (#{num}) actualizada con éxito")
                        if project_num:
                            add_issue_to_project(owner, project_num, f"https://github.com/{repo}/issues/{num}", dry_run=False)
                    except subprocess.CalledProcessError as e:
                        print(f"  ⚠️ Error actualizando #{num}: {e.stderr.strip()}")
                    finally:
                        if os.path.exists(temp_body):
                            os.remove(temp_body)
            else:
                print(f"  ℹ️ {task_id} ya existe como #{num} ({state})")
            processed += 1
            continue

        if dry_run:
            print(f"  [DRY-RUN] Se crearía issue: {task_id} -> {issue['title']} (Asignado: {assignee}, Milestone: {issue['milestone']})")
            if project_num:
                add_issue_to_project(owner, project_num, f"https://github.com/{repo}/issues/dry-run", dry_run=True)
            processed += 1
        else:
            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".md", encoding="utf-8") as f:
                f.write(issue["body"])
                temp_body = f.name
            try:
                cmd = [
                    "gh", "issue", "create",
                    "--repo", repo,
                    "--title", issue["title"],
                    "--body-file", temp_body,
                    "--milestone", issue["milestone"],
                ]
                if assignee:
                    cmd.extend(["--assignee", assignee])
                for lbl in issue["labels"]:
                    cmd.extend(["--label", lbl])
                res = run_command(cmd)
                issue_url = res.stdout.strip()
                print(f"  ✓ {task_id} creada: {issue_url}")
                if project_num:
                    add_issue_to_project(owner, project_num, issue_url, dry_run=False)
                processed += 1
            except subprocess.CalledProcessError as e:
                print(f"  ❌ Error creando {task_id}: {e.stderr.strip()}")
            finally:
                if os.path.exists(temp_body):
                    os.remove(temp_body)

    print(f"\n✨ Finalizado: {processed}/{len(target_issues)} tareas procesadas.")


def main():
    parser = argparse.ArgumentParser(
        description="Automatización de creación y sincronización de GitHub Issues, Milestones y Project Board para Portafolio + Blog."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula la ejecución en pantalla sin crear ni modificar nada en GitHub.",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Actualiza título, cuerpo, asignación y metadatos de las issues existentes en GitHub.",
    )
    parser.add_argument(
        "--sprint",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="Filtra y publica únicamente las tareas de un sprint específico (1 a 5).",
    )
    parser.add_argument(
        "--repo",
        type=str,
        default=None,
        help="Repositorio destino OWNER/REPO (por defecto detecta git remote origin o usa 'wigsdev/portafolio-blog').",
    )
    parser.add_argument(
        "--assignee",
        type=str,
        default="@me",
        help="Usuario de GitHub a quien asignar las tareas (por defecto '@me').",
    )
    parser.add_argument(
        "--no-project",
        action="store_true",
        help="Omite la creación o vinculación con GitHub Project Board.",
    )
    parser.add_argument(
        "--project-title",
        type=str,
        default="Portafolio + Blog — Sprint Board",
        help="Título del GitHub Project Board a crear o vincular.",
    )
    parser.add_argument(
        "--move-status",
        type=str,
        default="En progreso",
        help="Mueve todas las tarjetas del Project Board a la columna especificada (por defecto 'En progreso'). Pasa '' o 'none' para omitir.",
    )
    args = parser.parse_args()

    repo = args.repo or detect_git_repo() or "wigsdev/portafolio-blog"
    owner = repo.split("/")[0] if "/" in repo else "wigsdev"

    print("════════════════════════════════════════════════════════════════")
    print("   🚀 Portafolio + Blog — Sincronización de Tareas en GitHub   ")
    print("════════════════════════════════════════════════════════════════")

    if not check_gh_installed():
        print("❌ Error: GitHub CLI ('gh') no está instalado en tu sistema.")
        print("   Por favor instálalo o ejecuta el script en un entorno con 'gh'.")
        sys.exit(1)

    if not args.dry_run and not check_gh_auth():
        print("⚠️ Advertencia: No has iniciado sesión en GitHub CLI ('gh auth login').")
        print("   Inicia sesión con 'gh auth login' antes de sincronizar en modo real.")
        sys.exit(1)

    print(f"🎯 Repositorio destino: {repo}")
    print(f"👤 Asignado por defecto: {args.assignee}")
    if args.dry_run:
        print("🔍 Modo: SIMULACIÓN (DRY-RUN) — No se enviarán cambios a GitHub.")

    project_num = None
    if not args.no_project:
        project_num = ensure_project(owner=owner, title=args.project_title, dry_run=args.dry_run)

    ensure_milestones(repo=repo, dry_run=args.dry_run)
    ensure_labels(repo=repo, dry_run=args.dry_run)
    create_or_update_issues(
        repo=repo,
        dry_run=args.dry_run,
        update=args.update,
        sprint_filter=args.sprint,
        assignee=args.assignee,
        project_num=project_num,
        owner=owner
    )

    if project_num:
        print(f"\n📋 Tablero Kanban configurado en GitHub Projects (#{project_num}).")
        if args.move_status and args.move_status.lower() != "none":
            move_project_items_to_status(
                owner=owner,
                project_num=project_num,
                target_status_name=args.move_status,
                dry_run=args.dry_run
            )


if __name__ == "__main__":
    main()
