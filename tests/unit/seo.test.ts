import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

describe("Auditoría SEO: Robots, Sitemap y Dominio Canónico", () => {
  it("debe generar robots.txt dinámicamente desde Astro.site en src/pages/robots.txt.ts", () => {
    const robotsEndpointPath = path.resolve(
      process.cwd(),
      "src/pages/robots.txt.ts",
    );
    expect(fs.existsSync(robotsEndpointPath)).toBe(true);

    const content = fs.readFileSync(robotsEndpointPath, "utf-8");
    expect(content).toContain("User-agent: *");
    expect(content).toContain("Allow: /");
    expect(content).toContain("sitemap-index.xml");
  });

  it("debe definir site canónico para Vercel en astro.config.mjs", () => {
    const configPath = path.resolve(process.cwd(), "astro.config.mjs");
    const configContent = fs.readFileSync(configPath, "utf-8");
    expect(configContent).toContain("VERCEL_PROJECT_PRODUCTION_URL");
    expect(configContent).toContain(".vercel.app");
  });
});
