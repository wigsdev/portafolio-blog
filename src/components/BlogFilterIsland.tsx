import { useState, useMemo, useRef, useEffect } from "preact/hooks";
import type { ComponentChildren } from "preact";
import BlogCardItem, { type PostItem } from "./BlogCardItem";

// Re-exportamos PostItem para mantener compatibilidad con las páginas de Astro
export type { PostItem };

interface Props {
  posts: PostItem[];
  tags: string[];
  initialPosts?: string[];
  children?: ComponentChildren;
}

export default function BlogFilterIsland({
  posts,
  tags,
  initialPosts,
  children,
}: Props) {
  const [selectedTag, setSelectedTag] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [isSearchFocused, setIsSearchFocused] = useState<boolean>(false);

  // Estados de visibilidad de las flechas según la posición del scroll
  const [canScrollLeft, setCanScrollLeft] = useState<boolean>(false);
  const [canScrollRight, setCanScrollRight] = useState<boolean>(false);

  // Referencia al contenedor de scroll horizontal de tags
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  // Comprobar si se puede hacer scroll hacia la izquierda o derecha
  const updateScrollButtons = () => {
    const el = scrollContainerRef.current;
    if (!el) return;

    const atStart = el.scrollLeft <= 4;
    const atEnd = el.scrollLeft + el.clientWidth >= el.scrollWidth - 4;

    setCanScrollLeft(!atStart);
    setCanScrollRight(!atEnd && el.scrollWidth > el.clientWidth);
  };

  // Escuchar eventos de scroll y resize de ventana
  useEffect(() => {
    updateScrollButtons();
    const el = scrollContainerRef.current;
    if (el) {
      el.addEventListener("scroll", updateScrollButtons, { passive: true });
    }
    window.addEventListener("resize", updateScrollButtons);

    return () => {
      if (el) el.removeEventListener("scroll", updateScrollButtons);
      window.removeEventListener("resize", updateScrollButtons);
    };
  }, [tags]);

  // Función para desplazar horizontalmente con las flechas
  const scrollTags = (direction: "left" | "right") => {
    if (scrollContainerRef.current) {
      const scrollAmount = direction === "left" ? -180 : 180;
      scrollContainerRef.current.scrollBy({
        left: scrollAmount,
        behavior: "smooth",
      });
    }
  };

  // Filtrado instantáneo en memoria
  const filteredPosts = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();
    const isFiltered = selectedTag !== "all" || query.length > 0;

    // Si NO hay filtro activo y nos pasaron initialPosts, mostramos los de la página actual
    if (!isFiltered && initialPosts && initialPosts.length > 0) {
      return posts.filter((p) => initialPosts.includes(p.id));
    }
    // Si el usuario BUSCA o FILTRA, buscamos sobre el 100% del catálogo
    return posts.filter((post) => {
      const matchesTag =
        selectedTag === "all" || post.tags.includes(selectedTag);

      if (!matchesTag) return false;

      if (!query) return true;
      const inTitle = post.title.toLowerCase().includes(query);
      const inDesc = post.description.toLowerCase().includes(query);
      return inTitle || inDesc;
    });
  }, [posts, selectedTag, searchQuery]);

  const isExpanded = isSearchFocused || searchQuery.length > 0;

  const searchPlaceholder =
    selectedTag === "all" ? "Buscar" : `Buscar en ${selectedTag}`;

  return (
    <div class="w-full my-8">
      {/* Barra de Controles */}
      <div class="flex items-center gap-3 p-2 bg-surface border border-border rounded-full transition-[border-color] duration-200 max-md:flex-col-reverse max-md:items-stretch max-md:rounded-2xl">
        {/* Modo normal: Chip "Todos" fijo + lista de chips deslizables */}
        {!isExpanded && (
          <div class="flex items-center gap-1.5 flex-1 min-w-0 overflow-hidden">
            <button
              type="button"
              class={`shrink-0 inline-flex items-center px-3.5 py-1.5 rounded-full border text-sm font-semibold cursor-pointer whitespace-nowrap transition-all duration-150 ${
                selectedTag === "all"
                  ? "bg-brand text-text-inverse border-brand hover:bg-brand-hover hover:text-text-inverse"
                  : "border-transparent bg-transparent text-text-muted hover:text-text hover:bg-surface-muted"
              }`}
              onClick={() => setSelectedTag("all")}
            >
              Todos
            </button>

            {/* Flecha izquierda condicional */}
            {canScrollLeft && (
              <button
                type="button"
                class="inline-flex items-center justify-center w-7 h-7 rounded-full border border-border bg-surface-muted text-text-muted cursor-pointer shrink-0 transition-all duration-150 hover:text-brand hover:border-brand hover:bg-surface"
                onClick={() => scrollTags("left")}
                aria-label="Desplazar etiquetas a la izquierda"
              >
                <span
                  class="inline-block w-3.5 h-3.5 bg-current [mask:var(--icon)_no-repeat_center/contain] [-webkit-mask:var(--icon)_no-repeat_center/contain]"
                  style={{ "--icon": "url('/icons/ui/chevron-left.svg')" }}
                  aria-hidden="true"
                ></span>
              </button>
            )}

            {/* Contenedor de chips deslizables (scroll táctil nativo + flechas) */}
            <div
              class="flex items-center gap-1.5 overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden scroll-smooth p-0.5 select-none"
              ref={scrollContainerRef}
            >
              {tags.map((tag) => (
                <button
                  type="button"
                  key={tag}
                  class={`inline-flex items-center px-3.5 py-1.5 rounded-full border text-sm font-semibold cursor-pointer whitespace-nowrap transition-all duration-150 ${
                    selectedTag === tag
                      ? "bg-brand text-text-inverse border-brand hover:bg-brand-hover hover:text-text-inverse"
                      : "border-transparent bg-transparent text-text-muted hover:text-text hover:bg-surface-muted"
                  }`}
                  onClick={() => setSelectedTag(tag)}
                >
                  {tag}
                </button>
              ))}
            </div>

            {/* Flecha derecha condicional */}
            {canScrollRight && (
              <button
                type="button"
                class="inline-flex items-center justify-center w-7 h-7 rounded-full border border-border bg-surface-muted text-text-muted cursor-pointer shrink-0 transition-all duration-150 hover:text-brand hover:border-brand hover:bg-surface"
                onClick={() => scrollTags("right")}
                aria-label="Desplazar etiquetas a la derecha"
              >
                <span
                  class="inline-block w-3.5 h-3.5 bg-current [mask:var(--icon)_no-repeat_center/contain] [-webkit-mask:var(--icon)_no-repeat_center/contain]"
                  style={{ "--icon": "url('/icons/ui/chevron-right.svg')" }}
                  aria-hidden="true"
                ></span>
              </button>
            )}
          </div>
        )}

        {/* Modo expandido: solo chip activo */}
        {isExpanded && (
          <div class="shrink-0 pl-1">
            <span class="inline-flex items-center px-3.5 py-1.5 rounded-full border border-brand bg-brand text-text-inverse text-sm font-semibold whitespace-nowrap">
              {selectedTag === "all" ? "Todos" : selectedTag}
            </span>
          </div>
        )}

        {/* Buscador expansible */}
        <div
          class={`inline-flex items-center gap-2 py-1.5 px-3.5 bg-surface-muted border rounded-full transition-all duration-250 shrink-0 max-md:w-full max-md:min-w-0 ${
            isExpanded
              ? "flex-1 min-w-0 border-brand shadow-[0_0_0_2px_var(--color-shadow-brand)]"
              : "min-w-42 border-border focus-within:flex-1 focus-within:min-w-0 focus-within:border-brand focus-within:shadow-[0_0_0_2px_var(--color-shadow-brand)]"
          }`}
        >
          <span
            class="inline-block w-3.75 h-3.75 text-text-muted shrink-0 bg-current [mask:var(--icon)_no-repeat_center/contain] [-webkit-mask:var(--icon)_no-repeat_center/contain]"
            style={{ "--icon": "url('/icons/ui/search.svg')" }}
            aria-hidden="true"
          ></span>
          <input
            type="search"
            class="w-full border-none bg-transparent text-text text-sm outline-none placeholder:text-text-muted"
            placeholder={searchPlaceholder}
            value={searchQuery}
            onInput={(e) =>
              setSearchQuery((e.target as HTMLInputElement).value)
            }
            onFocus={() => setIsSearchFocused(true)}
            onBlur={() => setIsSearchFocused(false)}
            aria-label={searchPlaceholder}
          />
          {searchQuery && (
            <button
              type="button"
              class="border-none bg-transparent text-text-muted cursor-pointer text-xs p-0 px-1 hover:text-brand"
              onClick={() => setSearchQuery("")}
              aria-label="Limpiar búsqueda"
            >
              ✕
            </button>
          )}
        </div>
      </div>

      {/* Contador de resultados */}
      {(selectedTag !== "all" || searchQuery) && (
        <div class="flex items-center justify-between pt-3 px-2 text-sm text-text-muted">
          <span>
            {filteredPosts.length === 1
              ? "1 artículo encontrado"
              : `${filteredPosts.length} artículos encontrados`}
            {selectedTag !== "all" && (
              <>
                {" "}
                en <strong>{selectedTag}</strong>
              </>
            )}
          </span>
          <button
            type="button"
            class="bg-transparent border-none text-brand text-sm font-semibold cursor-pointer underline underline-offset-2 hover:text-brand-hover"
            onClick={() => {
              setSelectedTag("all");
              setSearchQuery("");
            }}
          >
            Restablecer filtros
          </button>
        </div>
      )}

      {/* Grilla Reactiva de Resultados (Consumiendo BlogCardItem unificado) */}
      {filteredPosts.length > 0 ? (
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
          {filteredPosts.map((post) => (
            <BlogCardItem key={post.id} post={post} />
          ))}
        </div>
      ) : (
        <div class="text-center py-16 px-4 text-text-muted">
          <p class="mb-6 text-[1.1rem]">
            No se encontraron artículos que coincidan con tu búsqueda.
          </p>
          <button
            type="button"
            class="inline-flex items-center justify-center px-5 py-2.5 rounded-lg border border-border bg-surface text-text font-semibold cursor-pointer transition-colors hover:bg-surface-muted hover:border-text-muted"
            onClick={() => {
              setSelectedTag("all");
              setSearchQuery("");
            }}
          >
            Ver todos los artículos
          </button>
        </div>
      )}

      {/* Paginación estática de Astro: solo se renderiza si NO hay filtros ni búsqueda activos */}
      {selectedTag === "all" && !searchQuery.trim() && children}
    </div>
  );
}
