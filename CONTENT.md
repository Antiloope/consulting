# Cómo editar el contenido

Todo el contenido vive en `index.html`. Cada sección está delimitada por un comentario
de bloque numerado, en el mismo orden en que se lee la página:

| # | id | Sección | Qué hace |
|---|----|---------|----------|
| 01 | `#top` | Hero | Promesa + CTA. Es lo único que ve el 60 % de las visitas. |
| 02 | `#senales` | Lo que se escucha | 7 citas. El prospecto se reconoce acá. |
| 03 | `#problema` | El problema | Reencuadre en dos frases. |
| 04 | `#framework` | Framework | Diagnóstico como primer paso del método, con un entregable único debajo de los objetivos. |
| 05 | `#madurez` | Mapa de madurez | Matriz: 6 verticales × 5 niveles (00–04). La primera fila va completa como muestra; el resto en placeholder. |
| 06 | `#servicios` | Plan de acción | Mapa simbólico A → B con plazos por tramo, más los entregables del plan. |
| 08 | `#manifiesto` | Manifiesto | El diferencial en una frase. |
| 09 | `#anatomia` | Anatomía | Timeline de ejemplo. |
| 10 | `#sobre-mi` | Sobre mí | Experiencia, forma de involucrarse y retrato de Rodrigo. |
| 11 | `#contacto` | Contacto | CTA final. |

El `07` falta a propósito: era el caso testigo y se sacó de la página. La numeración de
los comentarios de bloque quedó como está para no renumerar todo el archivo.

Si agregás o sacás una sección, actualizá también los links del `<nav class="site-nav">`
en el header (el scroll-spy los toma de ahí automáticamente).

---

## § 1 · Datos de contacto y URL

Ya están cargados. Si alguno cambia, estos son todos los lugares donde aparece:

| Dato | Valor actual | Dónde |
|---|---|---|
| Email | `rodrigopizarro1234@gmail.com` | `index.html`: `mailto` del botón, `href` del link, texto del link |
| LinkedIn | `pizarrorodrigo` | `index.html`: `href` del link y su texto |
| URL del sitio | `https://antiloope.github.io/consulting/` | `index.html`: `canonical`, `og:url`, `og:image`, JSON-LD · `robots.txt` · `sitemap.xml` · rutas de `404.html` |

Cuando tengas dominio propio conviene pasar el contacto a un mail del dominio
(`hola@…`) y no al Gmail personal: queda mejor en la propuesta y te deja migrar
sin tocar la página.

---

## § 2 · Recetas de edición

### Agregar una vertical al mapa de madurez

`#madurez` es una `<table class="matrix">`: columnas = niveles (00–04), filas =
verticales. Para agregar una: sumar un `<tr>` con `<th scope="row">` y cinco `<td>`
con `.matrix__placeholder`, en el mismo orden que el resto. Definí antes qué
evidencia la puntúa.

### Mostrar (o esconder) el criterio de una vertical

La primera fila lleva `class="matrix__row--sample"` y sus cinco `<td>` tienen texto
en vez de `.matrix__placeholder`. Es la única que publica su criterio: sirve de
prueba de que la matriz existe sin regalar el método entero.

Para publicar otra, poné texto en sus `<td>` y agregale la clase a su `<tr>`. Para
volver a esconderla, reemplazá el texto por
`<span class="matrix__placeholder" aria-hidden="true"></span>` y sacá la clase.
Si cambia la cantidad de filas de muestra, ajustá la `<caption>`, el
`.matrix-hint` de abajo y el `.lede` de la sección, que hoy dicen que hay una sola.

### Cambiar lo que promete cada entregable

Hay dos bloques `.deliverable` que dicen qué recibe el cliente, y son promesas
públicas: uno debajo de las tarjetas de `#framework` (lo que devuelve el
diagnóstico) y otro al final de `#servicios` (lo que devuelve el plan). Si cambia
la forma de trabajar, se actualizan estos dos antes que nada. La etiqueta es
`.card__label`; el de `#servicios` usa `.checklist`.

### Cambiar el orden de las secciones

Mover el bloque `<section>` completo. Alterná el fondo entre `section`,
`section--alt` y `section--invert` para que la página respire.

### Sacar el modo oscuro

Borrar el bloque `@media (prefers-color-scheme: dark)` al final de
`assets/css/tokens.css`. Nada más.

---

## § 3 · Pendientes marcados con `REVISAR` en el HTML

El deck original tenía cuatro puntos ambiguos o inconsistentes. Quedan tres sin
resolver, marcados con comentarios `REVISAR` en `index.html`:

```bash
grep -n "REVISAR\|TODO" index.html
```

1. ~~**Nivel 00 del mapa de madurez.**~~ Resuelto: `#madurez` es una matriz propia
   (6 verticales × 5 niveles). Se publica la estructura completa y el criterio de
   una sola vertical como muestra; el resto se trabaja en el diagnóstico. Ver § 2.

2. **Duración de Reliability & Incident.** El catálogo dice **12 semanas** y el
   ejemplo de "Anatomía de un proyecto" usa **8 semanas**. Definir cuál va.

3. **Duración del Technology Assessment.** El catálogo dice **2–4 semanas** y la slide
   de oferta de entrada dice **3 semanas**. Está puesto como 2–4; ajustar si corresponde.

4. **Rangos de la timeline.** El deck listaba "SEMANAS 2" y "SEMANAS 8" sin el rango
   completo. Quedaron como *Semanas 2–7* y *Semana 8*. Confirmar.

La explicación detallada de niveles y transiciones se cubre en la conversación de
diagnóstico, no en la landing pública: `#madurez` muestra los ejes completos y una
sola vertical escrita.
