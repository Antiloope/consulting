# Consultoría de tecnología — Rodrigo Pizarro

Landing de una sola página para **prospecting** y como **soporte visual de la primera reunión**.

Sitio estático puro: HTML + CSS + un archivo de JS. **Sin build, sin dependencias, sin `node_modules`.**
Se edita y se publica con `git push`.

---

## Estructura

```
.
├── index.html               ← toda la página. 11 secciones numeradas con comentarios.
├── 404.html
├── robots.txt
├── .nojekyll                ← evita que GitHub Pages procese el repo con Jekyll
├── assets/
│   ├── css/
│   │   ├── tokens.css       ← 1. TOKENS DE DISEÑO (colores, tipografía, espaciado, motion)
│   │   ├── base.css         ← 2. reset + defaults de elementos
│   │   ├── layout.css       ← 3. contenedores, secciones, header, footer, CTA fija
│   │   ├── components.css   ← 4. piezas reutilizables (botón, card, quote, timeline…)
│   │   └── sections.css     ← 5. ajustes propios de cada sección
│   ├── js/main.js           ← scroll-spy, reveal, CTA fija. Progressive enhancement.
│   └── img/                 ← favicon, og image, logos de clientes
├── docs/
│   └── deck-source.md       ← contenido del deck original, transcripto. Fuente del copy.
├── CONTENT.md               ← cómo editar el contenido
├── DESIGN.md                ← cómo usar y extender los tokens
└── .github/workflows/deploy.yml
```

**El orden de los `<link rel="stylesheet">` en `index.html` importa.** `tokens.css` va siempre primero.

---

## Desarrollo local

No hace falta ningún servidor: `open index.html` alcanza.

Si querés que las rutas absolutas de `404.html` funcionen igual que en producción, levantá un server estático:

```bash
python3 -m http.server 4177 --directory .
```

Y abrí <http://localhost:4177>.

Para probar en el celular contra la máquina local (mismo WiFi):

```bash
python3 -m http.server 4177 --bind 0.0.0.0 --directory .
```

### Scripts

| Script | Qué hace |
|---|---|
| `bash scripts/size.sh` | Mide el peso crudo y gzip. Falla si pasa los 25 KB gzip. |
| `bash scripts/shots.sh` | Capturas en viewports reales de mobile y desktop, en `.shots/`. Necesita el server levantado en el puerto 4177. |

`scripts/viewport.html` es sólo para `shots.sh`: mete el sitio en un iframe del
ancho pedido, porque Chrome headless ignora el `<meta viewport>` y maquetaría
todo a 980 px.

---

## Deploy

**En producción:** <https://antiloope.github.io/consulting/> · repo `Antiloope/consulting`

El workflow `deploy.yml` sube la carpeta tal cual en cada push a `main`.
Requisito único, una sola vez: en GitHub, **Settings → Pages → Source: GitHub Actions**.

> Alternativa sin Action: **Settings → Pages → Source: Deploy from a branch → `main` / `root`**.
> En ese caso podés borrar `.github/workflows/deploy.yml`. El `.nojekyll` es necesario en ambos casos.

### Ojo: es un *project page*, no un *user page*

El sitio se sirve en `/consulting/`, no en la raíz del dominio. Por eso:

- `index.html` usa **rutas relativas** (`assets/css/…`). No las pases a absolutas.
- `404.html` usa rutas **absolutas con el prefijo** `/consulting/`, porque un 404
  puede aparecer a cualquier profundidad y las relativas romperían.
- Si renombrás el repo, hay que actualizar: las 4 rutas de `404.html`, el
  `canonical` / `og:url` / `og:image` / JSON-LD de `index.html`, `robots.txt`
  y `sitemap.xml`.

### Dominio propio

Cuando lo tengas: agregar un archivo `CNAME` en la raíz con el dominio, apuntar el
DNS a GitHub Pages, y ahí sí el sitio pasa a la raíz — momento en el que conviene
sacarle el prefijo `/consulting/` a `404.html`.

---

## Criterios que sostiene este repo

- **Mobile-first**: todo el CSS arranca en una columna y crece con media queries `min-width`.
  La mayor parte del tráfico entra desde el celular.
- **Liviano**: sin frameworks, sin webfonts, sin imágenes en el camino crítico.
  Objetivo: **< 60 KB** de transferencia y first paint sin esperar red más allá del HTML+CSS.
- **Funciona sin JS**: `main.js` solo agrega animaciones y estado del nav.
  Los servicios se abren con `<details>` nativo.
- **Accesible**: contraste AA, foco visible, targets táctiles de 44 px, `prefers-reduced-motion`.

### Pendientes

- [x] Datos de contacto cargados (mail, LinkedIn, URL)
- [ ] Resolver los 4 `REVISAR` de `index.html` (ver `CONTENT.md § 3`)
- [ ] Agregar `assets/img/og.png` (1200×630) — sin esto el link se comparte sin imagen
- [ ] Agregar `assets/img/apple-touch-icon.png` (180×180)
- [ ] Probar en iPhone real: sin scroll horizontal, CTA fija no tapa contenido
- [ ] Lighthouse mobile ≥ 95 en las cuatro categorías
