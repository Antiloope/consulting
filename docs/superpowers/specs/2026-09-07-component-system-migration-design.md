# Migración al sistema de componentes reducido

## Objetivo

Convertir la propuesta reducida del inventario visual en el sistema de diseño efectivo de la landing y en el contrato obligatorio para futuros trabajos de frontend.

La migración debe reducir variaciones visuales sin alterar el contenido, el orden narrativo, los enlaces, el funcionamiento sin JavaScript, el modo oscuro ni el presupuesto de peso del sitio.

## Estrategia

La migración conserva los nombres públicos que ya usa la landing siempre que expresen el mismo concepto. No se adoptan nombres temporales `.v2-*`.

Los estilos compartidos viven en `assets/css/components.css`. Las composiciones específicas de la página viven en `assets/css/sections.css`. `assets/css/layout.css` conserva únicamente estructura global, navegación y cierre fijo.

## Componentes núcleo

El sistema final contiene diez familias:

1. Label auxiliar: `.label`.
2. Acción: `.btn`, con variantes `.btn--primary` y `.btn--ghost`.
3. Etiqueta contextual: `.tag`.
4. Cita: `.quote`.
5. Superficie: `.surface`; `.card`, `.disclosure` y `.level` consumen su misma gramática visual sin herencia HTML artificial.
6. Métrica: `.stat`.
7. Lista de resultados: `.checklist`.
8. Disclosure: `.disclosure` sobre `<details>` nativo.
9. Comparación: `.compare`.
10. Timeline: `.timeline`.

Las primitivas `.container`, `.grid`, `.stack` y `.cluster` son utilidades de layout, no componentes de producto.

## Decisiones de consolidación

- `.section__eyebrow`, `.phase__label`, `.level__gate-label`, `.timeline__when` y `.not-selling__label` convergen visualmente en `.label`. Los nombres contextuales pueden coexistir sólo cuando la composición necesita un selector estructural; deben compartir las reglas de `.label`.
- `.tag--neutral` se elimina. Existe una única etiqueta contextual.
- `.btn--sm` se elimina. Todo control interactivo mantiene un mínimo de 44 px.
- `.card`, `.disclosure` y `.level` comparten borde de 1 px, radio y superficie. No usan borde de acento grueso ni sombra.
- `.quote` conserva el acento izquierdo, reducido a 1 px.
- `.compare` deja de encerrar cada fila en una tarjeta y pasa a una estructura lineal delimitada por separadores.
- `.level` comunica progresión mediante número, contenido y orden, no mediante intensidad variable de bordes.

## Composiciones

Hero, mapa de madurez, anticipo de caso, contacto, CTA fija y footer se documentan como composiciones. Pueden usar componentes núcleo, pero no deben extraerse como abstracciones genéricas.

El hero elimina el eyebrow y mantiene dos acciones del mismo tamaño. El mapa de madurez conserva sus cinco niveles y scroll horizontal nativo. El anticipo de caso conserva las tres métricas y la comparación compacta. Contacto, CTA y footer conservan sus enlaces y contenido actual.

## Fuente de verdad

- `PRODUCT.md`: propósito, usuarios, contenido permitido y restricciones.
- `DESIGN.md`: reglas normativas del sistema.
- `mockups/component-inventory.html`: referencia visual final y ejemplos de uso.
- `AGENTS.md`: orden de lectura y obligaciones para futuros agentes.

Ante una discrepancia, el contenido factual de `PRODUCT.md` gana; para implementación visual, `DESIGN.md` gana sobre el inventario.

## Migración

1. Actualizar las pruebas para exigir el contrato reducido y la referencia en `AGENTS.md`.
2. Consolidar componentes en `components.css` sin introducir valores literales fuera de `tokens.css`.
3. Ajustar composiciones en `sections.css` y layout global sólo donde sea necesario.
4. Migrar `index.html`: labels, tags y botones; conservar semántica y copy.
5. Reemplazar el inventario comparativo por un catálogo final que consuma los CSS de producción.
6. Actualizar `DESIGN.md`, `README.md` y crear `AGENTS.md`.

## Accesibilidad y comportamiento

- Todos los enlaces, botones y summaries mantienen al menos 44 px de alto.
- El foco visible, contraste AA y `prefers-reduced-motion` se preservan.
- Los servicios siguen funcionando mediante `<details>` sin JavaScript.
- No se introduce scroll horizontal de página; el único desplazamiento horizontal permitido es el controlado del mapa de madurez.
- El modo oscuro sigue dependiendo de `prefers-color-scheme`.

## Verificación

- Prueba estructural del contrato de componentes y documentación.
- Prueba existente del flujo de contacto.
- `git diff --check`.
- `bash scripts/size.sh`, con total menor a 25 KB gzip.
- Revisión visual de la landing y del inventario en 390 px y 1440 px.
- Comprobación de consola, navegación, foco, disclosures y ausencia de overflow.
- Detector de Impeccable ejecutado una vez al final de los cambios visuales.
