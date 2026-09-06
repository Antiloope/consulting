# Cómo editar el contenido

Todo el contenido vive en `index.html`. Cada sección está delimitada por un comentario
de bloque numerado, en el mismo orden en que se lee la página:

| # | id | Sección | Qué hace |
|---|----|---------|----------|
| 01 | `#top` | Hero | Promesa + CTA. Es lo único que ve el 60 % de las visitas. |
| 02 | `#senales` | Lo que se escucha | 7 citas. El prospecto se reconoce acá. |
| 03 | `#problema` | El problema | Reencuadre en dos frases. |
| 03b | `#compromiso` | Compromiso + anticipo de prueba | El diferencial (precio fijo/alcance cerrado/sin dependencia) grande, más 2 filas de SIGES antes de entrar al framework. `.not-selling` vive acá, no en `#modelo`. |
| 04 | `#framework` | Framework | Las 4 fases del método. |
| 05 | `#madurez` | Mapa de madurez | Matriz de 6 verticales × 5 niveles (00–04), puntuada contra evidencia. |
| 06 | `#servicios` | Catálogo | 5 intervenciones, cada una en un `<details>`. |
| 07 | `#caso` | Caso SIGES | Métricas + tabla antes/después completa (5 filas). |
| 08 | `#manifiesto` | Manifiesto | El diferencial en una frase. |
| 09 | `#anatomia` | Anatomía | Timeline de ejemplo. |
| 10 | `#modelo` | Modelo de trabajo | Cómo se contrata, en detalle (las 3 tarjetas). |
| 11 | `#contacto` | Contacto | CTA final. |

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

### Agregar un servicio al catálogo

Duplicar un bloque `<details class="disclosure">` completo dentro de
`<div class="reveal" data-exclusive>`. El `data-exclusive` del contenedor hace que
solo uno quede abierto a la vez. El primero tiene `open`; sacáselo si querés que
arranquen todos cerrados.

### Agregar una vertical al mapa de madurez

Cada una de las 5 tarjetas `<li class="level">` de `#madurez` tiene un `<dl
class="level__verticals">` con las mismas 6 verticales, en el mismo orden. Para
agregar una vertical nueva hay que sumar un `<div><dt>…</dt><dd>…</dd></div>` a
**las 5 tarjetas**, en la misma posición, con la descripción de esa vertical en
cada nivel (00 a 04). No hay atajo: la matriz solo funciona si las 6 filas están
completas en las 5 columnas. Definí primero qué evidencia la puntúa (ver los
"Reglas del modelo" al final de la sección) antes de escribir las 5 descripciones.

### Agregar una fila a la tabla antes/después

Duplicar un `<div class="compare__row">`. En mobile se apila como par etiquetado;
en desktop se acomoda solo en dos columnas. No hay límite de filas.

### Agregar un caso

Duplicar la sección `07 · CASO EN CURSO` entera con otro `id` (`#caso-xxx`) y
alternar `section--alt` para que no queden dos fondos iguales pegados.

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

1. ~~**Nivel 00 del mapa de madurez.**~~ Resuelto: `#madurez` ya no es la
   transcripción del deck, es una matriz propia (6 verticales × 5 niveles,
   puntuada contra evidencia, con criterio de salida por nivel). El 00 tiene
   tesis y las seis descripciones propias, distintas del 01. Ver § 2 abajo para
   agregar una vertical nueva.

2. **Duración de Reliability & Incident.** El catálogo dice **12 semanas** y el
   ejemplo de "Anatomía de un proyecto" usa **8 semanas**. Definir cuál va.

3. **Duración del Technology Assessment.** El catálogo dice **2–4 semanas** y la slide
   de oferta de entrada dice **3 semanas**. Está puesto como 2–4; ajustar si corresponde.

4. **Rangos de la timeline.** El deck listaba "SEMANAS 2" y "SEMANAS 8" sin el rango
   completo. Quedaron como *Semanas 2–7* y *Semana 8*. Confirmar.

La slide sin contenido del deck (*"¿En qué consisten los niveles?"* / *"Ejemplos
de procesos de transición de estadíos"*) ya está cubierta: cada tarjeta de
`#madurez` explica en qué consiste su nivel (tesis + las 6 verticales) y el
criterio de salida hace de "ejemplo de transición". No hace falta un bloque aparte.

---

## § 4 · Copy original

`docs/deck-source.md` tiene la transcripción completa del deck
*"Consultoría de tecnología - Rodrigo Pizarro.pdf"*. Sirve como fuente de verdad del copy
y para recuperar frases que no entraron en la página.
