# Guía para agentes

Antes de diseñar frontend nuevo o modificar la interfaz existente, leer en este orden:

1. `PRODUCT.md`: objetivo del sitio, audiencia, contenido y restricciones funcionales.
2. `DESIGN.md`: reglas normativas de tokens, accesibilidad, layout y componentes.
3. `index.html` + `assets/css/components.css`: implementación canónica de las clases de producción.

## Contrato del frontend

- Componer primero con las 10 familias documentadas; no crear componentes nuevos si una familia o composición existente cubre el caso.
- Mantener `assets/css/tokens.css` como única fuente de valores visuales y `assets/css/components.css` como fuente de las piezas reutilizables.
- Reservar `assets/css/sections.css` para composiciones específicas de la landing. No mover a componentes un patrón que solo aparece en una sección.
- Conservar las clases públicas útiles (`.btn`, `.tag`, `.card`, `.quote`, `.stat`, `.checklist`, `.disclosure`, `.compare`, `.timeline`, `.matrix`) y evitar sistemas paralelos o prefijos temporales.
- Mantener controles con un target táctil mínimo de 44px, contraste AA, navegación por teclado, mobile-first, modo oscuro y funcionamiento completo sin JavaScript.
- Preservar rutas relativas: el sitio se publica como GitHub Project Page bajo `/consulting/`.
- No cambiar afirmaciones, datos de contacto ni contenido comercial sin validarlo contra `PRODUCT.md`, `CONTENT.md` y las marcas `REVISAR` de `index.html`.

## Al cambiar el sistema

Actualizar juntos:

- `assets/css/components.css` y, si corresponde, tokens o composiciones;
- `DESIGN.md`;
- las pruebas afectadas (`scripts/test-about.py`, `scripts/test-contact.py`).

Antes de entregar, ejecutar como mínimo:

```bash
python3 scripts/test-about.py
python3 scripts/test-contact.py
bash scripts/size.sh
```
