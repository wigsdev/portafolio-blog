import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('T-02: Sistema de Tokens CSS y Soporte Dark/Light', () => {
	const globalCssPath = path.resolve(process.cwd(), 'src/styles/global.css');
	const globalCssContent = fs.readFileSync(globalCssPath, 'utf-8');

	it('debe definir las variables semánticas de color en :root (Modo Claro)', () => {
		expect(globalCssContent).toContain('--color-brand: #d0354f;');
		expect(globalCssContent).toContain('--color-brand-hover: #aa3747;');
		expect(globalCssContent).toContain('--color-background: #faf8f8;');
		expect(globalCssContent).toContain('--color-surface: #ffffff;');
		expect(globalCssContent).toContain('--color-border: #e4dadd;');
		expect(globalCssContent).toContain('--color-text: #292429;');
		expect(globalCssContent).toContain('--color-text-muted: #6b5a5e;');
	});

	it('debe definir las variables semánticas en html.dark (Modo Oscuro)', () => {
		expect(globalCssContent).toContain('html.dark');
		expect(globalCssContent).toContain('--color-brand: #ff526d;');
		expect(globalCssContent).toContain('--color-brand-hover: #ff758c;');
		expect(globalCssContent).toContain('--color-background: #141416;');
		expect(globalCssContent).toContain('--color-surface: #1e1e22;');
		expect(globalCssContent).toContain('--color-border: #33333a;');
		expect(globalCssContent).toContain('--color-text: #f0edf0;');
		expect(globalCssContent).toContain('--color-text-muted: #D1D1D1;');
	});

	it('debe aplicar la fuente local Atkinson y contenedor fluido en el body', () => {
		expect(globalCssContent).toContain('--font-atkinson');
		expect(globalCssContent).toContain('max-width: 60rem');
		expect(globalCssContent).toContain('clamp(');
	});
});

