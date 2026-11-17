export interface Credencial {
  emisor: string;
  periodo: string;
  titulo: string;
  descripcion: string;
  pie: string;
  urlVerificacion?: string;
}

/**
 * Certificaciones técnicas validadas
 */
export const certificaciones: Credencial[] = [
  {
    emisor: "Oracle University",
    periodo: "2026 – 2028",
    titulo: "OCI Certified AI Foundations Associate",
    descripcion:
      "Fundamentos de Inteligencia Artificial, Machine Learning y servicios de IA generativa en la nube empresarial de Oracle.",
    pie: "ID: 331382997OCI26AICFA",
  },
  {
    emisor: "IBM SkillsBuild & Guayerd",
    periodo: "2026",
    titulo: "Fundamentos de Inteligencia Artificial",
    descripcion:
      "Principios de sistemas inteligentes, procesamiento de lenguaje natural (PLN), arquitecturas neuronales y ética en IA.",
    pie: "257 horas cátedra y práctica",
  },
  {
    emisor: "IBM SkillsBuild & Guayerd",
    periodo: "2024",
    titulo: "Fundamentos de Data Analytics",
    descripcion:
      "Ciclo de vida del dato, limpieza y transformación de datasets, modelado analítico y visualización para toma de decisiones.",
    pie: "255 horas cátedra y práctica",
  },
];

/**
 * Programas de formación continua, bootcamps y grado académico
 * Ordenados cronológicamente del más reciente al más antiguo
 */
export const formaciones: Credencial[] = [
  {
    emisor: "Nómada Bootcamp",
    periodo: "2026 – En curso",
    titulo: "Bootcamp Full Stack Developer",
    descripcion:
      "Programa profesional intensivo en desarrollo web full-stack, ingeniería de software, arquitecturas frontend modernas y servicios backend integrados.",
    pie: "En formación activa • Bootcamp profesional",
  },
  {
    emisor: "ONE AI FOR TECH",
    periodo: "2026",
    titulo: "Inteligencia Artificial, RAG & Agentes",
    descripcion:
      "Ingeniería de agentes autónomos, flujos RAG avanzados con bases vectoriales, orquestación de LLMs y servicios cloud de Inteligencia Artificial.",
    pie: "509 horas académicas",
  },
  {
    emisor: "ONE Grupo 9 (G9)",
    periodo: "2025 – 2026",
    titulo: "Backend Java & Spring Framework",
    descripcion:
      "Arquitectura backend empresarial, POO, persistencia con Spring Data JPA, APIs RESTful con Spring Boot 3 e integración de IA mediante Spring AI.",
    pie: "426 horas académicas",
  },
  {
    emisor: "ONE Grupo 4 (G4)",
    periodo: "2022 – 2023",
    titulo: "Front-End & Especialización React",
    descripcion:
      "Desarrollo web moderno con JavaScript, manipulación avanzada de DOM, consumo de APIs REST y construcción de interfaces interactivas con React.",
    pie: "408 horas académicas",
  },
  {
    emisor: "UNAS",
    periodo: "Grado Académico",
    titulo: "Bachiller en Ciencias",
    descripcion:
      "Formación científica de base por la Universidad Nacional Agraria de la Selva, orientada a la investigación, modelado analítico y resolución rigurosa de problemas complejos.",
    pie: "Registrado en SUNEDU",
  },
];
