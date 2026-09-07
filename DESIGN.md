# Sistema de diseño

Todo vive en `assets/css/tokens.css`. **Regla: ningún valor literal fuera de ese archivo**
(salvo `0`, `1px` y porcentajes). Si necesitás un color o un espaciado nuevo, primero
creás el token.

---

## Paleta

Está tomada del deck original (se extrajeron los colores del PDF): negro casi puro,
una escala de grises y **un solo acento azul**. No hay colores secundarios a propósito:
la restricción es lo que le da aire de consultoría seria.

### Neutros

| Token | Valor | Uso |
|---|---|---|
| `--ink-950` | `#0f0f0f` | Fondo de secciones invertidas, texto principal |
| `--ink-600` | `#555555` | Texto secundario |
| `--ink-500` | `#767676` | Texto terciario / eyebrows |
| `--ink-200` | `#e4e4e4` | Bordes |
| `--ink-050` | `#f5f5f5` | Fondo alterno |
| `--ink-025` | `#fcfcfc` | Fondo de página |

### Acento

| Token | Valor | Uso |
|---|---|---|
| `--blue-500` | `#026fd7` | Acento del deck. Botones, dots, valores de métricas |
| `--blue-600` | `#0257a8` | Hover y texto chico (mejor contraste) |
| `--blue-400` | `#4d9bf0` | Acento en modo oscuro |
| `--blue-050` | `#eaf3fd` | Fondo de tags |

Contraste verificado: `#026fd7` sobre `#fcfcfc` = **4.85:1** (AA para texto normal).
`#4d9bf0` sobre `#0f0f0f` = **6.6:1**.

### Tokens semánticos

Nunca uses las primitivas (`--ink-*`, `--blue-*`) directamente en un componente.
Usá los semánticos, que son los que cambian solos en modo oscuro:

`--bg` · `--bg-alt` · `--bg-invert` · `--surface` · `--surface-sunken`
`--text` · `--text-muted` · `--text-subtle` · `--text-on-invert` · `--text-on-accent`
`--accent` · `--accent-hover` · `--accent-text` · `--accent-wash` · `--accent-border`
`--border` · `--border-strong` · `--border-invert`

---

## Tipografía

**System font stack.** Cero requests, cero FOUT, se ve nativa en cada plataforma.
Es la decisión más barata en performance y la que mejor se lee en mobile.

### Cambiar a una webfont

Si más adelante querés una fuente propia (p. ej. Inter o una grotesca):

1. Poné los `.woff2` en `assets/fonts/`.
2. Agregá el `@font-face` arriba de `assets/css/base.css` con `font-display: swap`.
3. Pisá el token: `--font-sans: "TuFuente", -apple-system, …` (dejá el stack de fallback).
4. Precargá solo el peso del `h1`: `<link rel="preload" as="font" type="font/woff2" crossorigin>`.

No subas más de dos pesos. Cada peso son ~25 KB en el camino crítico.

### Escala

Fluida con `clamp()`, mobile-first: el primer valor del clamp es el del celular.

`--fs-2xs` `--fs-xs` `--fs-sm` `--fs-md` `--fs-base` `--fs-lg` `--fs-xl` `--fs-2xl` `--fs-3xl` `--fs-4xl`

El body nunca baja de `1rem` (16px), que es lo que evita el zoom automático de iOS
en inputs y mejora la lectura a distancia de brazo.

---

## Espaciado

Escala de 4px: `--sp-1` (4px) … `--sp-24` (96px).

Para el ritmo vertical de la página usá siempre `--section-py`
(`clamp(3.5rem, 8vw, 6.5rem)`), no valores sueltos.

---

## Breakpoints

Solo tres, todos `min-width` (mobile-first). En `em` para que respeten el zoom del usuario.

| Ancho | Qué cambia |
|---|---|
| `40em` (640px) | Grillas pasan a 2 columnas |
| `48em` (768px) | Tabla antes/después a 2 columnas; desaparece la CTA fija |
| `60em` (960px) | Grillas de 3 y 4 columnas |
| `64em` (1024px) | Aparece el nav de anclas en el header |

---

## Reglas de layout

- **Nada de anchos fijos.** `.container` (68rem) y `.container--narrow` (46rem) para texto.
- **Gutter fluido**: `--gutter` = `clamp(1.25rem, 5vw, 2.5rem)`.
- **Safe areas**: el `body`, el header y la CTA fija usan `env(safe-area-inset-*)`
  para el notch y la home bar del iPhone. El `<meta viewport>` lleva `viewport-fit=cover`.
- **Sin scroll horizontal**: `overflow-x: clip` en el `body`. Si algo se desborda,
  el bug está en el contenido, no en el body — arreglalo ahí.
- **Targets táctiles**: mínimo 44px de alto en todo lo clickeable (`.btn`, `.contact__link`,
  `.disclosure__summary`).

---

## Sistema canónico de componentes

La referencia visual y funcional es [`mockups/component-inventory.html`](mockups/component-inventory.html).
El núcleo está cerrado en **10 familias**; el resto son composiciones de página o utilidades de layout.

| Familia | Clases | Para qué |
|---|---|---|
| Label | `.label` | Contexto, metadatos y rótulos discretos. Sin mayúsculas forzadas ni tracking ornamental. |
| Botón | `.btn` `.btn--primary` `.btn--ghost` | Acciones primarias y secundarias. No hay versión táctil reducida. |
| Tag | `.tag` | Duración, categoría o estado breve. Un solo tratamiento visual. |
| Cita | `.quote` | Voz del cliente con una línea de acento mínima. |
| Superficie | `.surface` `.card` | Base visual compartida: fondo, borde de 1px y radio. `.disclosure` usa la misma gramática. |
| Métrica | `.stat` | Evidencia numérica con valor y explicación. |
| Checklist | `.checklist` | Entregables, criterios o resultados verificables. |
| Detalle | `.disclosure` | Contenido expandible con `<details>` nativo. |
| Comparación | `.compare` `.compare--compact` | Antes/después en filas lineales, sin convertir cada fila en una tarjeta. |
| Timeline | `.timeline` | Secuencia temporal o de trabajo. |

### Composiciones, no familias nuevas

- `.hero`, `.contact`, `.matrix`, `.proof-teaser`, `.case__stats`, `.not-selling` y el footer combinan componentes, contenido y layout para una sección concreta.
- `.grid--2/3/4`, `.stack`, `.cluster`, `.container` y `.container--narrow` son utilidades de layout.
- `.reveal` es una mejora progresiva de movimiento, no un componente visual.

### Regla para extender

1. Primero resolvé el caso con estas familias y las utilidades existentes.
2. Agregá una variante solo si cambia el significado o el comportamiento, no por una diferencia cosmética aislada.
3. Creá una familia nueva únicamente si el patrón aparece en más de un contexto y no cabe en una superficie existente.
4. Si el sistema cambia, actualizá en la misma entrega `components.css`, esta guía, el inventario canónico y su prueba.

---

## Movimiento

Una sola animación en toda la página: `.reveal` (fade + 12px de subida).
Se dispara con `IntersectionObserver` y se desactiva entera con `prefers-reduced-motion`.

Duraciones: `--dur-fast` (120ms) para hover, `--dur` (220ms) para transiciones de estado,
`--dur-slow` (520ms) para entradas.

---

## Presupuesto de performance

Medido con `bash scripts/size.sh`. Estado actual entre paréntesis.

| Recurso | Límite (crudo) | Hoy |
|---|---|---|
| HTML | 40 KB | 36 KB |
| CSS (5 archivos) | 45 KB | 36 KB |
| JS | 5 KB | 4.2 KB |
| Imágenes en el camino crítico | 0 | 0 |
| **Total transferido (gzip)** | **< 25 KB** | **20.4 KB** |

GitHub Pages sirve todo con gzip/brotli, así que el número que importa es el último.

Si algo no entra en el presupuesto, la pregunta correcta es si esa cosa tiene que estar.
