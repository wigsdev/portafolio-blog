# 🎨 Especificación del Sistema de Diseño y Tokens UI

Este documento establece el contrato visual, la paleta de tokens CSS semánticos, la tipografía fluida y las directrices de interfaz de usuario para el **Portafolio Personal & Blog** de **Wilmer Gulcochía (@wigsdev)**.

---

## 1. Principios de Diseño UI/UX

1. **Rendimiento Extremo (Zero-JS UI):**
   - Todos los componentes visuales (Header, Footer, Cards, Grids) se renderizan mediante HTML y CSS estático puro sin dependencias externas de librerías CSS pesadas.
2. **Accesibilidad Universal (WCAG 2.1 Nivel AA):**
   - Ratios de contraste de texto superiores a `4.5:1` para texto normal y `3:1` para texto grande en ambos modos.
   - Enfoque visual visible (`outline` de 2px con `outline-offset`) para usuarios de teclado.
3. **Tipografía Hiperlegible:**
   - Tipografía principal basada en la fuente local **Atkinson Hyperlegible** (`--font-atkinson`), diseñada específicamente para facilitar la lectura y evitar la fatiga visual.
4. **Soporte Nativo de Temas (Claro y Oscuro):**
   - Paleta de colores curada que preserva la calidez del modo claro y la profundidad libre de deslumbramiento del modo oscuro (`#141416`).
   - Sincronización instantánea con `localStorage` y persistencia con View Transitions (`astro:after-swap`).

---

## 2. Paleta de Tokens CSS Semánticos

Los tokens están organizados bajo un enfoque semántico en `:root` y modificados dinámicamente mediante la clase `html.dark`.

| Token CSS                 |   Modo Claro (Default)   |   Modo Oscuro (`.dark`)    | Uso Principal                                                   |
| ------------------------- | :----------------------: | :------------------------: | --------------------------------------------------------------- |
| `--color-brand`           |        `#d0354f`         |         `#ff526d`          | Color principal de acento, enlaces activos y botones primarios  |
| `--color-brand-hover`     |        `#aa3747`         |         `#ff758c`          | Estado hover/focus de botones y elementos interactivos          |
| `--color-brand-dark`      |        `#412227`         |         `#3a151e`          | Contrastes profundos y sombras sutiles                          |
| `--color-brand-soft`      |        `#fce7ec`         | `rgba(255, 82, 109, 0.16)` | Fondos de chips, tags activos y destacados sutiles              |
| `--color-background`      |        `#faf8f8`         |         `#141416`          | Fondo del lienzo principal del documento (`body`)               |
| `--color-surface`         |        `#ffffff`         |         `#1e1e22`          | Fondo de tarjetas (`ProjectCard`, `BlogCard`), modales y header |
| `--color-surface-muted`   |        `#f3ecee`         |         `#27272c`          | Fondos de preview de imágenes, cajas de código y badges         |
| `--color-text`            |        `#292429`         |         `#f0edf0`          | Color primario para títulos y párrafos                          |
| `--color-text-muted`      |        `#6b5a5e`         |         `#d1d1d1`          | Texto secundario, fechas, metadatos y subtítulos                |
| `--color-text-inverse`    |        `#ffffff`         |         `#ffffff`          | Texto sobre fondos con `--color-brand`                          |
| `--color-border`          |        `#e4dadd`         |         `#33333a`          | Bordes sutiles de tarjetas, separadores y header                |
| `--color-github`          |        `#1f2328`         |         `#e6edf3`          | Botones y enlaces hacia repositorios de GitHub                  |
| `--color-github-hover-bg` |        `#f3f4f6`         |         `#2d333b`          | Fondo en hover para botones de GitHub                           |
| `--color-shadow-brand`    | `rgba(65, 34, 39, 0.12)` |   `rgba(0, 0, 0, 0.45)`    | Sombra sutil de elevación en tarjetas                           |

---

## 3. Tipografía y Escala Fluida

### 3.1 Familia Tipográfica

- **Fuente Principal:** `var(--font-atkinson), system-ui, -apple-system, sans-serif`
- **Fuente Monospace:** `ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, monospace` (bloques de código y snippets).

### 3.2 Escala Tipográfica Adaptable con `clamp()`

Para garantizar proporciones perfectas entre dispositivos móviles y pantallas grandes sin saltos bruscos:

```css
/* Escala de texto fluida */
--text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.8125rem); /* 12px - 13px */
--text-sm: clamp(0.875rem, 0.83rem + 0.22vw, 0.9375rem); /* 14px - 15px */
--text-base: clamp(1rem, 0.95rem + 0.25vw, 1.0625rem); /* 16px - 17px */
--text-lg: clamp(1.125rem, 1.05rem + 0.38vw, 1.25rem); /* 18px - 20px */
--text-xl: clamp(1.25rem, 1.15rem + 0.5vw, 1.5rem); /* 20px - 24px */
--text-2xl: clamp(1.5rem, 1.35rem + 0.75vw, 1.875rem); /* 24px - 30px */
--text-3xl: clamp(1.875rem, 1.65rem + 1.13vw, 2.25rem); /* 30px - 36px */
--text-4xl: clamp(2.25rem, 1.95rem + 1.5vw, 3rem); /* 36px - 48px */
```

---

## 4. Breakpoints y Contenedores

- **Enfoque:** _Mobile-First_ progresivo.
- **Contenedor Central:**
  - Móvil / Tablet: `max-width: 60rem` (960px) con padding horizontal `clamp(1rem, 4vw, 2rem)`.
  - Pantallas Grandes (`min-width: 90rem` / 1440px): `max-width: 72rem` (1152px).

| Breakpoint |      Medida      | Dispositivos Clave                         |
| ---------- | :--------------: | ------------------------------------------ |
| `sm`       | `40rem` (640px)  | Teléfonos grandes en horizontal y phablets |
| `md`       | `48rem` (768px)  | Tablets y pantallas medianas               |
| `lg`       | `64rem` (1024px) | Laptops y monitores de escritorio estándar |
| `xl`       | `80rem` (1280px) | Pantallas amplias y monitores Full HD      |

---

## 5. Modelos Visuales de Arquitectura (Wireframes ASCII)

### 5.1 Encabezado y Navegación (`Header.astro`)

```text
+-------------------------------------------------------------------------+
| [Logo] Wilmer Gulcochía             [Inicio] [Proyectos] [Blog] [Sobre Mí] [Contacto] [☀️/🌙] |
+-------------------------------------------------------------------------+
```

### 5.2 Portada Principal (`index.astro`)

```text
+-------------------------------------------------------------------------+
| [Hero Section]                                                          |
|   Hola, soy Wilmer Gulcochía 👋                                         |
|   Desarrollador Frontend & Web | Astro · TypeScript · IA Aplicada       |
|   [Ver Proyectos] [Descargar CV] [Escríbeme]                            |
+-------------------------------------------------------------------------+
| [Badges de Stack Tecnológico]                                           |
|   Astro · TypeScript · React · CSS Moderno · Node.js · APIs de IA       |
+-------------------------------------------------------------------------+
| [Proyectos Destacados (Grid 2 cols)]                                    |
|   +--------------------------+  +--------------------------+            |
|   | [Img 16:9] Pomodoro      |  | [Img 16:9] OmniSpec IA   |            |
|   | Chips: TS · JS · CSS     |  | Chips: Python · JS · AI   |            |
|   | [Demo] [GitHub]          |  | [Demo] [GitHub]          |            |
|   +--------------------------+  +--------------------------+            |
+-------------------------------------------------------------------------+
| [Últimas Publicaciones del Blog (3 posts)]                              |
|   • Fecha · Título del Artículo · Tags                                  |
+-------------------------------------------------------------------------+
```

### 5.3 Tarjeta de Proyecto (`ProjectCard.astro`)

```text
+-------------------------------------------------------------+
|  +-------------------------------------------------------+  |
|  |           Vista Previa con <Image /> (16:9)           |  |
|  +-------------------------------------------------------+  |
|  [TypeScript] [JavaScript] [CSS]  <-- Chips de Tecnología   |
|                                                             |
|  Título del Proyecto                                        |
|  Descripción concisa del proyecto y su valor técnico...     |
|                                                             |
|  [Slot Opcional: Métricas o notas destacadas]               |
|                                                             |
|  [ Demo ]                             [ Repositorio GitHub ]|
+-------------------------------------------------------------+
```

---

## 6. Convenciones de Microinteracciones y Estados

1. **Botones e Interactividad:**
   - `transition: background-color 200ms ease, color 200ms ease, border-color 200ms ease;`
   - Estado `:hover`: Desplazamiento sutil o cambio de luminosidad.
   - Estado `:focus-visible`: Borde destacado con `--color-brand-hover` y `outline-offset: 3px` para teclado.
2. **View Transitions (`<ClientRouter />`):**
   - Transición global de fundido suave (`fade`).
   - Las imágenes de proyectos o posts pueden utilizar `transition:name` para transformarse suavemente entre la vista de lista y la vista de detalle.
