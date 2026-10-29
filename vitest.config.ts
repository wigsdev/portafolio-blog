/// <reference types="vitest/config" />
import { getViteConfig } from 'astro/config';
import 'vitest/config';

export default getViteConfig({
	test: {
		include: ['tests/**/*.{test,spec}.{ts,js}'],
		environment: 'node',
	},
});

