// @ts-check

import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import { defineConfig, fontProviders, sharpImageService } from "astro/config";

import preact from "@astrojs/preact";
import node from "@astrojs/node";
import vercel from "@astrojs/vercel";

import tailwindcss from "@tailwindcss/vite";

const siteUrl =
  process.env.SITE_URL ||
  (process.env.VERCEL_PROJECT_PRODUCTION_URL
    ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
    : "https://portafolio-blog-seven.vercel.app");

// https://astro.build/config
export default defineConfig({
  site: siteUrl,
  adapter: process.env.VERCEL
    ? vercel()
    : node({
        mode: "standalone",
      }),
  integrations: [mdx(), sitemap(), preact()],
  build: {
    inlineStylesheets: "always",
  },
  image: {
    service: sharpImageService(),
  },

  fonts: [
    {
      provider: fontProviders.local(),
      name: "Atkinson",
      cssVariable: "--font-atkinson",
      fallbacks: ["sans-serif"],
      options: {
        variants: [
          {
            src: ["./src/assets/fonts/atkinson-regular.woff"],
            weight: 400,
            style: "normal",
            display: "swap",
          },
          {
            src: ["./src/assets/fonts/atkinson-bold.woff"],
            weight: 700,
            style: "normal",
            display: "swap",
          },
        ],
      },
    },
  ],

  vite: {
    plugins: [tailwindcss()],
  },
});