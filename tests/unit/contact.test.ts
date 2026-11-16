import { describe, it, expect } from 'vitest';
import { contactSchema } from '../../src/schemas/contact';

describe('Contact Form Zod Schema Validation', () => {
  it('valida correctamente un conjunto de datos válido y recorta espacios en blanco', () => {
    const validData = {
      nombre: '  Wilmer Gulcochía  ',
      email: 'wigsdev@example.com',
      asunto: '  Propuesta de Colaboración Técnica  ',
      mensaje: 'Hola Wilmer, me interesa conversar contigo sobre una oportunidad técnica en frontend.',
    };

    const result = contactSchema.safeParse(validData);
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.nombre).toBe('Wilmer Gulcochía');
      expect(result.data.asunto).toBe('Propuesta de Colaboración Técnica');
      expect(result.data.email).toBe('wigsdev@example.com');
    }
  });

  it('rechaza nombres menores a 2 caracteres o vacíos', () => {
    const invalidData = {
      nombre: 'W',
      email: 'wigsdev@example.com',
      asunto: 'Consulta técnica',
      mensaje: 'Mensaje con longitud suficiente para superar el mínimo requerido.',
    };

    const result = contactSchema.safeParse(invalidData);
    expect(result.success).toBe(false);
    if (!result.success) {
      const errors = result.error.flatten().fieldErrors;
      expect(errors.nombre).toBeDefined();
      expect(errors.nombre?.[0]).toBe('El nombre debe tener al menos 2 caracteres');
    }
  });

  it('rechaza correos con formato inválido', () => {
    const invalidData = {
      nombre: 'Wilmer',
      email: 'correo-invalido-sin-arroba',
      asunto: 'Consulta técnica',
      mensaje: 'Mensaje con longitud suficiente para superar el mínimo requerido.',
    };

    const result = contactSchema.safeParse(invalidData);
    expect(result.success).toBe(false);
    if (!result.success) {
      const errors = result.error.flatten().fieldErrors;
      expect(errors.email).toBeDefined();
      expect(errors.email?.[0]).toBe('Ingresa un correo electrónico válido');
    }
  });

  it('rechaza mensajes con menos de 10 caracteres', () => {
    const invalidData = {
      nombre: 'Wilmer',
      email: 'wigsdev@example.com',
      asunto: 'Consulta técnica',
      mensaje: 'Muy corto',
    };

    const result = contactSchema.safeParse(invalidData);
    expect(result.success).toBe(false);
    if (!result.success) {
      const errors = result.error.flatten().fieldErrors;
      expect(errors.mensaje).toBeDefined();
      expect(errors.mensaje?.[0]).toBe('El mensaje debe tener al menos 10 caracteres');
    }
  });

  it('rechaza objetos vacíos o campos faltantes con mensajes claros', () => {
    const emptyData = {};

    const result = contactSchema.safeParse(emptyData);
    expect(result.success).toBe(false);
    if (!result.success) {
      const errors = result.error.flatten().fieldErrors;
      expect(errors.nombre?.[0]).toBe('El nombre es obligatorio');
      expect(errors.email?.[0]).toBe('El correo electrónico es obligatorio');
      expect(errors.asunto?.[0]).toBe('El asunto es obligatorio');
      expect(errors.mensaje?.[0]).toBe('El mensaje es obligatorio');
    }
  });
});