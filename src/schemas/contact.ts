import { z, type infer as zInfer } from 'astro/zod';

export const contactSchema = z.object({
  nombre: z
    .string({ message: 'El nombre es obligatorio' })
    .trim()
    .min(2, 'El nombre debe tener al menos 2 caracteres')
    .max(100, 'El nombre no puede exceder 100 caracteres'),
  email: z
    .string({ error: 'El correo electrónico es obligatorio' })
    .trim()
    .pipe(z.email({ error: 'Ingresa un correo electrónico válido' })),
  asunto: z
    .string({ message: 'El asunto es obligatorio' })
    .trim()
    .min(3, 'El asunto debe tener al menos 3 caracteres')
    .max(150, 'El asunto no puede exceder 150 caracteres'),
  mensaje: z
    .string({ message: 'El mensaje es obligatorio' })
    .trim()
    .min(10, 'El mensaje debe tener al menos 10 caracteres')
    .max(2000, 'El mensaje no puede exceder 2000 caracteres'),
});

export type ContactFormData = zInfer<typeof contactSchema>;
