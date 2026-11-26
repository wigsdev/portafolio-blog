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
  post: PostItem;
}

export default function BlogCardItem({ post }: Props) {
  return (
    <article class="group flex flex-col bg-surface border border-border rounded-xl overflow-hidden transition-all duration-180 ease-in-out hover:-translate-y-1 hover:shadow-[0_8px_20px_var(--color-shadow-brand)] hover:border-brand motion-reduce:transition-none motion-reduce:hover:translate-none">
      {post.heroImage && (
        <a
          href={`/blog/${post.id}/`}
          class="block overflow-hidden aspect-video bg-surface-muted"
          tabIndex={-1}
          aria-hidden="true"
        >
          <img
            src={post.heroImage}
            alt={post.title}
            class="w-full h-full object-cover transition-transform duration-240 ease-in-out group-hover:scale-[1.03] motion-reduce:group-hover:scale-100"
            loading="lazy"
          />
        </a>
      )}
      <div class="flex flex-col flex-1 p-5">
        {post.tags.length > 0 && (
          <div class="flex flex-wrap gap-1.5 mb-3">
            {post.tags.map((t) => (
              <a
                key={t}
                href={`/blog/tags/${t}/`}
                class="no-underline"
                title={`Ver artículos con la etiqueta ${t}`}
              >
                <span class="inline-flex items-center px-2 py-1 border border-text-muted rounded-full text-text-muted bg-surface text-xs font-semibold leading-none">
                  {t}
                </span>
              </a>
            ))}
          </div>
        )}
        <h3 class="text-[1.2rem] font-bold leading-[1.35] m-0 mb-2">
          <a
            href={`/blog/${post.id}/`}
            class="text-text no-underline transition-colors duration-150 hover:text-brand"
          >
            {post.title}
          </a>
        </h3>
        <p class="text-sm text-text-muted leading-normal m-0 mb-5 line-clamp-3">
          {post.description}
        </p>
        <footer class="flex items-center justify-between flex-wrap gap-2 text-xs text-text-muted mt-auto pt-3 border-t border-border">
          <div class="inline-flex items-center gap-1.5">
            <img
              src="/foto.jpg"
              alt="Wilmer Gulcochía"
              width="20"
              height="20"
              class="w-5 h-5 rounded-full object-cover shrink-0"
              loading="lazy"
            />
            <span class="font-semibold text-text">Wilmer Gulcochía</span>
          </div>
          <div class="inline-flex items-center gap-1.5">
            <time dateTime={post.pubDate}>{post.formattedDate}</time>
            <span class="text-text-muted opacity-60" aria-hidden="true">
              ·
            </span>
            <span class="inline-flex items-center gap-1">
              <span
                class="inline-block w-3.25 h-3.25 bg-current [mask:var(--icon)_no-repeat_center/contain] [-webkit-mask:var(--icon)_no-repeat_center/contain]"
                style={{ "--icon": "url('/icons/ui/clock.svg')" }}
                aria-hidden="true"
              ></span>
              {post.readingTime} min
            </span>
          </div>
        </footer>
      </div>
    </article>
  );
}
