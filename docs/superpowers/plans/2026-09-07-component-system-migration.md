# Component System Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convertir el sistema reducido en la implementación efectiva de la landing y en el contrato obligatorio para futuros cambios de frontend.

**Architecture:** Conservar los nombres públicos útiles, consolidar diez familias en `components.css` y mantener las composiciones específicas en `sections.css`. El catálogo visual consume las clases reales de producción; `DESIGN.md` y `AGENTS.md` definen su uso normativo.

**Tech Stack:** HTML5, CSS nativo, JavaScript progresivo existente y Python estándar para pruebas estructurales.

**Spec:** `docs/superpowers/specs/2026-09-07-component-system-migration-design.md`

## Global Constraints

- Sitio estático puro, sin build ni dependencias nuevas.
- El contenido factual y el orden narrativo de `index.html` no cambian.
- Todo valor visual literal vive en `assets/css/tokens.css`; los demás CSS consumen tokens.
- La landing funciona sin JavaScript y usa `<details>` nativo.
- Targets interactivos de al menos 44 px, contraste AA y soporte de `prefers-reduced-motion`.
- Transferencia total de producción menor a 25 KB gzip.
- El mapa de madurez es el único componente con desplazamiento horizontal propio.

---

### Task 1: Proteger el contrato final

**Files:**
- Modify: `scripts/test-component-inventory.py`
- Test: `scripts/test-component-inventory.py`

**Interfaces:**
- Consumes: `mockups/component-inventory.html`, `index.html`, `AGENTS.md`, `DESIGN.md`.
- Produces: una prueba ejecutable que falla si reaparecen la comparación, prefijos temporales o clases retiradas.

- [ ] **Step 1: Escribir la prueba fallida**

Actualizar el parser para guardar texto y clases por documento. Exigir:

```python
assert "sistema-final" in parser.ids
assert "propuesta" not in parser.ids
assert not any(name.startswith("v2-") for name in parser.classes)
assert not ({"btn--sm", "tag--neutral"} & landing_parser.classes)
assert len(parser.final_components) == 10
assert AGENTS.exists()
assert "mockups/component-inventory.html" in AGENTS.read_text(encoding="utf-8")
assert "DESIGN.md" in AGENTS.read_text(encoding="utf-8")
```

- [ ] **Step 2: Ejecutar la prueba y confirmar el fallo**

Run: `python3 scripts/test-component-inventory.py`

Expected: FAIL porque el inventario aún usa `#propuesta` y `.v2-*`, y `AGENTS.md` no existe.

- [ ] **Step 3: No implementar todavía**

Conservar el fallo como evidencia RED para las tareas 2 y 3.

### Task 2: Migrar la landing al núcleo reducido

**Files:**
- Modify: `assets/css/components.css`
- Modify: `assets/css/sections.css`
- Modify: `assets/css/layout.css`
- Modify: `index.html`

**Interfaces:**
- Consumes: tokens semánticos de `assets/css/tokens.css` y el HTML actual.
- Produces: `.label`, `.btn`, `.tag`, `.quote`, `.surface`, `.stat`, `.checklist`, `.disclosure`, `.compare` y `.timeline`; composiciones existentes compatibles.

- [ ] **Step 1: Consolidar labels y acciones**

Definir `.label` y hacer que los selectores contextuales compartan la misma gramática:

```css
.label,
.section__eyebrow,
.phase__label,
.level__gate-label,
.timeline__when,
.not-selling__label {
  font-size: var(--fs-sm);
  font-weight: var(--fw-medium);
  line-height: var(--lh-normal);
  color: var(--text-muted);
}
```

Eliminar `.btn--sm` y `.tag--neutral`; reemplazar sus usos en `index.html` por las clases base.

- [ ] **Step 2: Unificar superficies**

Aplicar a `.surface`, `.card`, `.disclosure` y `.level`:

```css
.surface,
.card,
.disclosure,
.level {
  border: var(--border-width) solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
}
```

Quitar bordes superiores graduados de `.level`, sombras y decoraciones duplicadas.

- [ ] **Step 3: Simplificar citas y comparaciones**

Usar un acento de un solo píxel en `.quote`. Convertir `.compare` en filas lineales con `border-block` y separadores, sin cards por fila; preservar el apilado mobile y las dos columnas desde `48em`.

- [ ] **Step 4: Mantener composiciones en su capa**

Eliminar el eyebrow del hero. Conservar mapa de madurez, anticipo, contacto, CTA y footer como reglas en `sections.css`/`layout.css`. Asegurar que todos los `<summary>` y `.btn` tengan altura mínima:

```css
min-height: calc(var(--sp-10) + var(--sp-1));
```

- [ ] **Step 5: Ejecutar pruebas de regresión existentes**

Run: `python3 scripts/test-contact.py`

Expected: `Contacto: flujo verificado`.

Run: `bash scripts/size.sh`

Expected: total menor a 25 KB gzip.

### Task 3: Publicar la referencia final y las reglas para agentes

**Files:**
- Modify: `mockups/component-inventory.html`
- Modify: `DESIGN.md`
- Modify: `README.md`
- Create: `AGENTS.md`
- Test: `scripts/test-component-inventory.py`

**Interfaces:**
- Consumes: las clases finales implementadas por Task 2.
- Produces: un único catálogo visual final y un orden de autoridad inequívoco para futuros agentes.

- [ ] **Step 1: Reemplazar el catálogo comparativo**

Eliminar la versión actual, la sección “Propuesta reducida”, el mapa de decisiones y todas las clases `.v2-*`. Mostrar exactamente diez ejemplos marcados así:

```html
<article class="specimen" data-final-component="action">…</article>
```

Usar directamente `.label`, `.btn`, `.tag`, `.quote`, `.surface`, `.stat`, `.checklist`, `.disclosure`, `.compare` y `.timeline`.

- [ ] **Step 2: Actualizar DESIGN.md**

Reemplazar el listado previo por las diez familias, sus límites, las composiciones y esta regla:

```markdown
Antes de crear una variante, comprobá que el caso no pueda resolverse componiendo las diez familias existentes. Una undécima familia requiere documentar un uso repetido con la misma intención.
```

- [ ] **Step 3: Crear AGENTS.md**

Incluir el orden obligatorio:

```markdown
Antes de modificar frontend, leer en este orden: `PRODUCT.md`, `DESIGN.md` y `mockups/component-inventory.html`.
```

Prohibir `.v2-*`, valores visuales literales fuera de tokens, nuevas variantes sin repetición demostrada, cambios de copy factual y dependencias/build steps nuevos.

- [ ] **Step 4: Actualizar README.md**

Agregar `AGENTS.md` y el inventario a la estructura del repo y explicar que el catálogo es la referencia visual final.

- [ ] **Step 5: Ejecutar la prueba y confirmar GREEN**

Run: `python3 scripts/test-component-inventory.py`

Expected: `component inventory: ok`.

### Task 4: Verificación integral

**Files:**
- Verify: `index.html`
- Verify: `mockups/component-inventory.html`
- Verify: `assets/css/*.css`

**Interfaces:**
- Consumes: implementación y documentación de Tasks 1–3.
- Produces: evidencia de comportamiento, responsive, presupuesto y limpieza del diff.

- [ ] **Step 1: Ejecutar checks automatizados**

Run individually:

```bash
python3 scripts/test-component-inventory.py
python3 scripts/test-contact.py
bash scripts/size.sh
git diff --check
```

Expected: todos con exit code 0 y total de producción menor a 25 KB gzip.

- [ ] **Step 2: Ejecutar detector visual una sola vez**

Run:

```bash
.agents/skills/impeccable/scripts/impeccable detect --json index.html mockups/component-inventory.html
```

Expected: sin defectos nuevos de la implementación final; documentar sólo excepciones estrechas si el detector marca contenido intencional.

- [ ] **Step 3: Verificar en navegador**

Abrir landing e inventario en 390×844 y 1440×1000. Comprobar scroll horizontal, targets, foco, apertura de disclosures, navegación, consola y modo responsive.

- [ ] **Step 4: Revisar el diff final**

Confirmar que no se alteraron copy factual, URLs de contacto, JSON-LD, metadatos o restricciones abiertas `REVISAR`.
