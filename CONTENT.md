# Cómo editar el contenido

Todo el contenido vive en `index.html`. Cada sección está delimitada por un comentario
de bloque numerado, en el mismo orden en que se lee la página:

| # | id | Sección | Qué hace |
|---|----|---------|----------|
| 01 | `#top` | Hero | Promesa + CTA. Es lo único que ve el 60 % de las visitas. |
| 02 | `#senales` | Lo que se escucha | 7 citas. El prospecto se reconoce acá. |
| 03 | `#problema` | El problema | Reencuadre en dos frases. |
| 04 | `#framework` | Framework | Las 4 fases del método. |
| 05 | `#madurez` | Mapa de madurez | Los 5 estadíos (00–04). |
| 06 | `#servicios` | Catálogo | 5 intervenciones, cada una en un `<details>`. |
| 07 | `#caso` | Caso SIGES | Métricas + tabla antes/después. |
| 08 | `#manifiesto` | Manifiesto | El diferencial en una frase. |
| 09 | `#anatomia` | Anatomía | Timeline de ejemplo. |
| 10 | `#modelo` | Modelo de trabajo | Cómo se contrata + lo que no se vende. |
| 11 | `#contacto` | Contacto | CTA final. |

Si agregás o sacás una sección, actualizá también los links del `<nav class="site-nav">`
en el header (el scroll-spy los toma de ahí automáticamente).

---

## § 1 · Placeholders obligatorios

Buscá y reemplazá en todo el repo antes de publicar:

```bash
grep -rn "TU-DOMINIO\|TU-USUARIO" --include="*.html" --include="*.txt" .
```

| Placeholder | Dónde | Reemplazar por |
|---|---|---|
| `TU-DOMINIO.com` | `index.html` (canonical, OG, JSON-LD, mailto), `robots.txt` | Dominio real |
| `TU-USUARIO` | `index.html` (LinkedIn) | Usuario de LinkedIn |
| `hola@TU-DOMINIO.com` | `index.html` (2 lugares + mailto del CTA) | Email de contacto |

El deck original también tenía estos datos como placeholder (`email@dominio.com`,
`linkedin.com/in/usuario`), así que hay que definirlos igual.

---

## § 2 · Recetas de edición

### Agregar un servicio al catálogo

Duplicar un bloque `<details class="disclosure">` completo dentro de
`<div class="reveal" data-exclusive>`. El `data-exclusive` del contenedor hace que
solo uno quede abierto a la vez. El primero tiene `open`; sacáselo si querés que
arranquen todos cerrados.

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

El deck original tenía tres puntos ambiguos o inconsistentes. Están marcados con
comentarios `REVISAR` en `index.html`:

```bash
grep -n "REVISAR\|TODO" index.html
```

1. **Nivel 00 del mapa de madurez.** En el deck, los niveles `00 Ad hoc` y
   `01 Estabilización` comparten la misma descripción ("Versionado, ambientes, incidentes").
   Puse *"Sin versionado, deploys manuales, conocimiento tácito"* como propuesta para el 00.
   Cambiala por la real.

2. **Duración de Reliability & Incident.** El catálogo dice **12 semanas** y el
   ejemplo de "Anatomía de un proyecto" usa **8 semanas**. Definir cuál va.

3. **Duración del Technology Assessment.** El catálogo dice **2–4 semanas** y la slide
   de oferta de entrada dice **3 semanas**. Está puesto como 2–4; ajustar si corresponde.

4. **Rangos de la timeline.** El deck listaba "SEMANAS 2" y "SEMANAS 8" sin el rango
   completo. Quedaron como *Semanas 2–7* y *Semana 8*. Confirmar.

Además, el deck tenía una slide sin contenido con los títulos
*"¿En qué consisten los niveles?"* y *"Ejemplos de procesos de transición de estadíos"*.
No está en la página. Si esa idea se desarrolla, el lugar natural es después de
`#madurez`, como un bloque de `.disclosure` por nivel.

---

## § 4 · Copy original

`docs/deck-source.md` tiene la transcripción completa del deck
*"Consultoría de tecnología - Rodrigo Pizarro.pdf"*. Sirve como fuente de verdad del copy
y para recuperar frases que no entraron en la página.
