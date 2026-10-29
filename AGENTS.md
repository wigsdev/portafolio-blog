## Development

When starting the dev server, use background mode:

```bash
pnpm astro dev --background
```

Manage the background server with `pnpm astro dev stop`, `pnpm astro dev status`, and `pnpm astro dev logs`.

## Governance & Development Rules

1. **Package Manager:**
   - Use `pnpm` exclusively (`pnpm install`, `pnpm build`, `pnpm astro ...`). Do not use `npm` or `yarn`.

2. **Reference Directory Isolation:**
   - The `.reference/` directory contains local reference materials and is ignored in Git. NEVER include it in commits or edit its contents as part of project tasks.

3. **Branching & Git Flow (Solo Developer):**
   - Do not commit directly to `main`.
   - Always work in dedicated feature branches: `feat/T-XX-description` or `fix/T-XX-description`.
   - Follow **Conventional Commits** format (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `chore:`).
   - Reference the associated task/issue in the commit message or PR (e.g., `(T-01)` or `Closes #1`).

4. **Architecture & Zero-JS Philosophy:**
   - Deliver zero JavaScript to the browser by default.
   - Interactive UI components must use explicit `client:*` directives on islands only when strictly necessary.
   - For images, always use `<Image />` or `<Picture />` from `astro:assets` with required `alt` and explicit dimensions to safeguard Core Web Vitals.
   - Preserve local font Atkinson (`--font-atkinson`) and semantic color tokens for dark/light themes.

5. **Semantic Versioning & Changelog Protocol:**
   - The project starts at `0.1.0` and reaches `1.0.0` upon production deployment.
   - Upon completing each task, evaluate the impact of changes: increment `MINOR` (`0.X.0`) for new features/modules/pages, or `PATCH` (`0.X.Y`) for fixes/styles/refactoring.
   - Synchronize `package.json` version and document all changes in `CHANGELOG.md` following Keep a Changelog standards.

6. **Definition of Done (DoD) & Strict Commit Authorization:**
   - Before completing any task, execute `pnpm build` to ensure clean static output without TypeScript or compiler errors.
   - **MANDATORY RULE:** NEVER execute `git commit` or push automatically. Always present the changes and changelog update to the USER, put yourself on hold, and commit ONLY after receiving explicit approval ("visto bueno").

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
