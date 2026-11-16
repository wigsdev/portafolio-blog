import { defineAction } from 'astro:actions';
import { contactSchema } from '../schemas/contact';

export const server = {
  contact: defineAction({
    accept: 'form',
    input: contactSchema,
    handler: async (input) => {
      // En producción aquí se integraría el envío vía email (Resend, SendGrid) o webhook
      return {
        success: true,
        nombre: input.nombre,
        message: '¡Gracias por contactarme! He recibido tu mensaje y te responderé lo antes posible.',
      };
    },
  }),
};