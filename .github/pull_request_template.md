## 📋 Descripción del Cambio

<!-- Resume brevemente los cambios introducidos por este PR y el motivo de la implementación -->

## 🔗 Tarea / Issue Vinculada

- **Issue:** Closes #<!-- Ej: Closes #1 -->
- **ID Tarea Backlog:** `[T-XX]` <!-- Ej: [T-01] -->
- **Sprint:** Sprint <!-- Ej: Sprint 1 -->

## 🏷️ Tipo de Cambio

- [ ] `feat:` Nueva funcionalidad o página
- [ ] `fix:` Corrección de error o bug
- [ ] `docs:` Documentación, especificaciones o guías
- [ ] `style:` Sistema de diseño, variables CSS o tokens
- [ ] `refactor:` Refactorización de componentes sin cambio funcional
- [ ] `chore:` Configuración del entorno, scripts, dependencias o gobernanza

## 🎯 Criterios de Aceptación (DoD) Cumplidos

<!-- Copia y marca los criterios de aceptación específicos definidos en la Issue -->

- [x] Criterio 1
- [x] Criterio 2
- [x] Criterio 3

## 🧪 Verificaciones Técnicas Obligatorias (DoD Global)

- [x] `pnpm build` compila limpiamente en estático (`dist/`) sin errores de TypeScript ni advertencias.
- [x] Filosofía Zero-JS preservada (islas interactivas con directiva `client:*` solo donde es indispensable).
- [x] Uso de `<Image />` o `<Picture />` de `astro:assets` con `alt` descriptivo y dimensiones explícitas.
- [x] Registro en `CHANGELOG.md` bajo el estándar Keep a Changelog y sincronización en `package.json`.
