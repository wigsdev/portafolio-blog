import { describe, it, expect } from 'vitest';
import { SITE_TITLE, SITE_DESCRIPTION } from '../../src/consts';

describe('Configuración Base y Constantes', () => {
	it('debe tener el título oficial y descripción configurados', () => {
		expect(SITE_TITLE).toBeDefined();
		expect(SITE_TITLE).toContain('Wilmer Gulcochía');
		expect(SITE_DESCRIPTION).toBeDefined();
	});
});

