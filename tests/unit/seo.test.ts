import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('Auditoría SEO: Robots y Sitemap', () => {
	it('debe existir public/robots.txt y referenciar el sitemap oficial', () => {
		const robotsPath = path.resolve(process.cwd(), 'public/robots.txt');
		expect(fs.existsSync(robotsPath)).toBe(true);

		const content = fs.readFileSync(robotsPath, 'utf-8');
		expect(content).toContain('User-agent: *');
		expect(content).toContain('Allow: /');
		expect(content).toContain('Sitemap: https://wigsdev.netlify.app/sitemap-index.xml');
	});

	it('debe contener la configuración canónica en astro.config.mjs', () => {
		const configPath = path.resolve(process.cwd(), 'astro.config.mjs');
		const configContent = fs.readFileSync(configPath, 'utf-8');
		expect(configContent).toContain('site: "https://wigsdev.netlify.app"');
	});
});
