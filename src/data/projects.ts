import type { ImageMetadata } from "astro";

import pomodoroImage from "../assets/projects/pomodoro.svg";
import markdownPdfImage from "../assets/projects/markdown-pdf.svg";
import omnispecImage from "../assets/projects/omnispec.svg";
import libraryImage from "../assets/projects/library.svg";
import salesforceImage from "../assets/projects/salesforce-learning.svg";
import weatherImage from "../assets/projects/weather-dashboard.svg";

export interface Proyecto {
  nombre: string;
  imagen: ImageMetadata;
  imagenAlt: string;
  descripcion: string;
  tecnologias: string[];
  demoUrl?: string;
  githubUrl: string;
  destacado?: boolean;
}

export const proyectos: Proyecto[] = [
  {
    nombre: "Pomodoro",
    imagen: pomodoroImage,
    imagenAlt:
      "Ilustración de un temporizador Pomodoro con un tomate y una sesión de 25 minutos.",
    descripcion:
      "Aplicación web para organizar sesiones de concentración y descansos mediante la técnica Pomodoro.",
    tecnologias: ["TypeScript", "JavaScript", "CSS"],
    githubUrl: "https://github.com/wigsdev/POMODORO-APP",
  },
  {
    nombre: "Markdown - Pdf",
    imagen: markdownPdfImage,
    imagenAlt:
      "Ilustración de un editor Markdown junto a una vista previa de un documento PDF.",
    descripcion:
      "Herramienta web para convertir documentos Markdown a PDF con tablas, resaltado de sintaxis y diagramas Mermaid.",
    tecnologias: ["JavaScript", "Python", "CSS"],
    githubUrl: "https://github.com/wigsdev/markdown-pdf",
  },
  {
    nombre: "OmniSpec IA",
    imagen: omnispecImage,
    imagenAlt:
      "Ilustración de un panel de ingeniería con revisiones de especificaciones y auditorías de repositorios.",
    descripcion:
      "Plataforma web para generar especificaciones, auditar repositorios y crear pull requests con supervisión humana.",
    tecnologias: ["Python", "JavaScript", "Dockerfile"],
    demoUrl: "https://d140eqoid6qg8h.cloudfront.net/",
    githubUrl: "https://github.com/wigsdev/omnispec-ai",
  },
  {
    nombre: "Gestor de Biblioteca Digital",
    imagen: libraryImage,
    imagenAlt:
      "Ilustración del catálogo de una biblioteca digital con búsqueda y colecciones de libros.",
    descripcion:
      "Aplicación web para gestionar en tiempo real el catálogo de una biblioteca digital.",
    tecnologias: ["CSS", "JavaScript", "HTML"],
    demoUrl: "https://wigsdev.github.io/gestor-biblioteca-digital/",
    githubUrl: "https://github.com/wigsdev/gestor-biblioteca-digital",
    destacado: true,
  },
  {
    nombre: "Salesforce Admin Learning Platform",
    imagen: salesforceImage,
    imagenAlt:
      "Ilustración de una plataforma de aprendizaje con módulos y progreso del curso de administración.",
    descripcion:
      "Plataforma web para aprender y gestionar los contenidos del curso Salesforce Administrator.",
    tecnologias: ["HTML", "Python", "CSS"],
    demoUrl: "https://admin-salesforce.onrender.com/login",
    githubUrl: "https://github.com/wigsdev/salesforce_admin",
    destacado: true,
  },
  {
    nombre: "Weather Dashboard",
    imagen: weatherImage,
    imagenAlt:
      "Ilustración de un panel meteorológico con condiciones actuales y pronóstico por hora.",
    descripcion:
      "Dashboard web para consultar condiciones meteorológicas actualizadas en tiempo real.",
    tecnologias: ["JavaScript", "CSS", "HTML"],
    demoUrl: "https://wigsdev.github.io/dashboard-clima/",
    githubUrl: "https://github.com/wigsdev/dashboard-clima",
    destacado: true,
  },
];