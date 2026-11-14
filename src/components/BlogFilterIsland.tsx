import { useState, useMemo, useRef, useEffect } from "preact/hooks";
import type { ComponentChildren } from "preact";

export interface PostItem {
  id: string;
  title: string;
  description: string;
  pubDate: string;
  formattedDate: string;
  tags: string[];
  readingTime: number;
  heroImage?: string;
}

interface Props {
  posts: PostItem[];
  tags: string[];
  initialPosts?: string[];
  children?: ComponentChildren;
}

export default function BlogFilterIsland({ posts, tags, initialPosts, children }: Props) {
  const [selectedTag, setSelectedTag] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [isSearchFocused, setIsSearchFocused] = useState<boolean>(false);

  // Estados de visibilidad de las flechas según la posición del scroll
  const [canScrollLeft, setCanScrollLeft] = useState<boolean>(false);
  const [canScrollRight, setCanScrollRight] = useState<boolean>(false);

  // Referencia al contenedor de scroll horizontal de tags
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  // Referencias para el soporte Drag-to-Scroll (arrastrar con el mouse)
  const isMouseDownRef = useRef<boolean>(false);
  const startXRef = useRef<number>(0);
  const scrollLeftStartRef = useRef<number>(0);
  const hasDraggedRef = useRef<boolean>(false);

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

  // Manejadores de Drag-to-Scroll con mouse
  const handleMouseDown = (e: MouseEvent) => {
    const el = scrollContainerRef.current;
    if (!el) return;
    isMouseDownRef.current = true;
    hasDraggedRef.current = false;
    startXRef.current = e.pageX - el.offsetLeft;
    scrollLeftStartRef.current = el.scrollLeft;
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (!isMouseDownRef.current || !scrollContainerRef.current) return;
    e.preventDefault();
    const x = e.pageX - scrollContainerRef.current.offsetLeft;
    const walk = (x - startXRef.current) * 1.4; // Multiplicador de velocidad de arrastre
    if (Math.abs(walk) > 4) {
      hasDraggedRef.current = true;
    }
    scrollContainerRef.current.scrollLeft = scrollLeftStartRef.current - walk;
  };

  const handleMouseUpOrLeave = () => {
    isMouseDownRef.current = false;
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
      // 1. Filtro por tag
      const matchesTag =
        selectedTag === "all" || post.tags.includes(selectedTag);

      if (!matchesTag) return false;

      // 2. Filtro por buscador (título o descripción)
      if (!query) return true;
      const inTitle = post.title.toLowerCase().includes(query);
      const inDesc = post.description.toLowerCase().includes(query);
      return inTitle || inDesc;
    });
  }, [posts, selectedTag, searchQuery]);

  // Si el buscador está en foco o tiene texto, se activa el modo expandido (Capturas 2 y 3)
  const isExpanded = isSearchFocused || searchQuery.length > 0;

  // Placeholder dinámico según la etiqueta activa
  const searchPlaceholder =
    selectedTag === "all" ? "Buscar" : `Buscar en ${selectedTag}`;

  return (
    <div class="filter-island">
      {/* Barra de Controles idéntica a UndefinedShell */}
      <div class={`filter-bar ${isExpanded ? "filter-bar--expanded" : ""}`}>
        {/* En modo normal: Chip "Todos" fijo + lista de chips deslizables */}
        {!isExpanded && (
          <div class="filter-tags-wrapper">
            {/* 1. Chip "Todos" fijo fuera del scroll */}
            <button
              type="button"
              class={`filter-pill filter-pill--fixed ${selectedTag === "all" ? "filter-pill--active" : ""}`}
              onClick={() => setSelectedTag("all")}
            >
              Todos
            </button>

            {/* 2. Flecha izquierda condicional (solo visible si scrollLeft > 0) */}
            {canScrollLeft && (
              <button
                type="button"
                class="scroll-arrow-btn scroll-arrow-btn--left"
                onClick={() => scrollTags("left")}
                aria-label="Desplazar etiquetas a la izquierda"
              >
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <polyline points="15 18 9 12 15 6" />
                </svg>
              </button>
            )}

            {/* 3. Contenedor de chips con arrastre (Drag-to-Scroll) */}
            <div
              class="filter-tags-scroll"
              ref={scrollContainerRef}
              onMouseDown={handleMouseDown}
              onMouseMove={handleMouseMove}
              onMouseUp={handleMouseUpOrLeave}
              onMouseLeave={handleMouseUpOrLeave}
            >
              {tags.map((tag) => (
                <button
                  type="button"
                  key={tag}
                  class={`filter-pill ${selectedTag === tag ? "filter-pill--active" : ""}`}
                  onClick={() => {
                    // Evitar clic accidental si el usuario estaba arrastrando la lista
                    if (!hasDraggedRef.current) {
                      setSelectedTag(tag);
                    }
                  }}
                >
                  {tag}
                </button>
              ))}
            </div>

            {/* 4. Flecha derecha condicional (solo visible si falta contenido por mostrar) */}
            {canScrollRight && (
              <button
                type="button"
                class="scroll-arrow-btn scroll-arrow-btn--right"
                onClick={() => scrollTags("right")}
                aria-label="Desplazar etiquetas a la derecha"
              >
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <polyline points="9 18 15 12 9 6" />
                </svg>
              </button>
            )}
          </div>
        )}

        {/* En modo expandido: solo se muestra el chip de la categoría activa fija a la izquierda */}
        {isExpanded && (
          <div class="filter-active-pill-wrapper">
            <span class="filter-pill filter-pill--active">
              {selectedTag === "all" ? "Todos" : selectedTag}
            </span>
          </div>
        )}

        {/* Buscador expansible que toma casi todo el ancho al hacer foco */}
        <div class={`search-box ${isExpanded ? "search-box--expanded" : ""}`}>
          <svg
            class="search-icon"
            width="15"
            height="15"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            aria-hidden="true"
          >
            <circle cx="11" cy="11" r="8" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" />
          </svg>
          <input
            type="search"
            class="search-input"
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
              class="search-clear"
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
        <div class="filter-status">
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
            class="filter-reset-btn"
            onClick={() => {
              setSelectedTag("all");
              setSearchQuery("");
            }}
          >
            Restablecer filtros
          </button>
        </div>
      )}

      {/* Grilla Reactiva de Resultados */}
      {filteredPosts.length > 0 ? (
        <div class="cards-grid filter-results-grid">
          {filteredPosts.map((post) => (
            <article key={post.id} class="blog-card">
              {post.heroImage && (
                <a
                  href={`/blog/${post.id}/`}
                  class="blog-card-image-link"
                  tabIndex={-1}
                  aria-hidden="true"
                >
                  <img
                    src={post.heroImage}
                    alt={post.title}
                    class="blog-card-image"
                    loading="lazy"
                  />
                </a>
              )}
              <div class="blog-card-body">
                {post.tags.length > 0 && (
                  <div class="blog-card-tags">
                    {post.tags.map((t) => (
                      <a
                        key={t}
                        href={`/blog/tags/${t}/`}
                        class="tag-link"
                        title={`Ver artículos con la etiqueta ${t}`}
                      >
                        <span class="badge">
                          <span class="badge-text">{t}</span>
                        </span>
                      </a>
                    ))}
                  </div>
                )}
                <h3 class="blog-card-title">
                  <a href={`/blog/${post.id}/`}>{post.title}</a>
                </h3>
                <p class="blog-card-description">{post.description}</p>
                <footer class="blog-card-footer">
                  <div class="blog-card-author-group">
                    <img
                      src="/foto.jpg"
                      alt="Wilmer Gulcochía"
                      width="20"
                      height="20"
                      class="blog-card-avatar"
                      loading="lazy"
                    />
                    <span class="blog-card-author">Wilmer Gulcochía</span>
                  </div>
                  <div class="blog-card-meta">
                    <time dateTime={post.pubDate}>{post.formattedDate}</time>
                    <span class="blog-card-separator" aria-hidden="true">
                      ·
                    </span>
                    <span class="reading-time">
                      <svg
                        width="13"
                        height="13"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        aria-hidden="true"
                      >
                        <circle cx="12" cy="12" r="10" />
                        <polyline points="12 6 12 12 16 14" />
                      </svg>
                      {post.readingTime} min
                    </span>
                  </div>
                </footer>
              </div>
            </article>
          ))}
        </div>
      ) : (
        <div class="filter-empty">
          <p>No se encontraron artículos que coincidan con tu búsqueda.</p>
          <button
            type="button"
            class="btn btn--secondary"
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
