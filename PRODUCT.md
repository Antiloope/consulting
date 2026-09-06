# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Lector primario: dos personas, una firma.**

- **Gerente de IT / líder técnico interno.** Ya sabe que hay deuda técnica. No necesita
  que lo convenzan del problema: necesita material con el que pedir presupuesto hacia
  arriba. Suele ser quien encuentra la página o quien la recibe primero.
- **Dueño / Director general de la PyME.** Es quien firma. No es técnico. Le importa la
  dependencia de una persona, el miedo a tocar producción y el costo de vivir apagando
  incendios — no el stack.

El material tiene que sostener **dos niveles de lectura simultáneos**: creíble para el
técnico que lo evalúa, comprensible para el dueño que lo aprueba. Ninguno de los dos
puede quedar afuera.

**Situación de uso:** el link se manda antes de una primera conversación de 30 minutos, o
se muestra durante esa reunión. No es un canal de captación en frío de alto volumen: es
material de prospecting y soporte de la primera reunión.

## Product Purpose

Consultoría de modernización tecnológica para PyMEs que **crecieron alrededor de su
software** y cuya forma de construirlo y mantenerlo no evolucionó a la velocidad del
negocio.

El trabajo se vende como intervenciones cerradas: diagnóstico, transformación del modelo
de ingeniería, plataforma interna, confiabilidad y gestión de incidentes, y modernización
de legacy por etapas.

**Éxito** = la conversación de 30 minutos ocurre, y ocurre con la persona correcta ya
alineada sobre cuál es el problema. La página no cierra la venta; califica y encuadra.

## Positioning

**No se moderniza el software: se moderniza la capacidad de la empresa para producir,
desplegar y operar software.** Esa capacidad es lo que queda cuando el proyecto termina.

Lo que un competidor vecino no puede copiar sin dejar de ser lo que es:

- **Precio fijo por resultado**, no horas de consultor.
- **Principio y fin**, con exclusiones explícitas en la propuesta.
- **Sin dependencia**: no se vende el mantenimiento de lo que se implementa.

Ese último punto es el diferencial real y es económicamente costoso de imitar: la mayoría
del sector monetiza justamente la dependencia que aquí se rechaza por contrato.

**Lo que explícitamente no se vende:** desarrollo a medida, staff augmentation, soporte
IT, consultoría por hora.

## Operating Context

- **Origen del contenido:** deck de 18 slides (`docs/deck-source.md`, transcripción
  completa). Es la fuente de verdad del copy.
- **Entrada al funnel:** referidos y contacto directo, más el link mandado antes de la
  reunión. Contacto por mail y LinkedIn; no hay formulario ni calendario embebido.
- **Alcance geográfico:** base en Córdoba, Argentina. Se trabaja **remoto en todo el país
  con visitas presenciales en momentos clave** (diagnóstico, adopción). Córdoba es dato de
  origen y de cercanía, no un límite comercial.
- **Capacidad de entrega:** operación individual con **colaboradores puntuales por
  proyecto** (SRE, infra, data). El compromiso y el liderazgo son siempre de Rodrigo
  Pizarro. Ningún material futuro debe insinuar una firma con equipo estable ni prometer
  múltiples intervenciones simultáneas.
- **Idioma:** español (`es`, variante argentina). No hay versión en inglés ni está
  decidido que vaya a haberla.

## Capabilities and Constraints

### Catálogo de intervenciones

| Intervención | Duración | Resultado |
|---|---|---|
| Technology Assessment | 2–4 semanas | Diagnóstico, roadmap priorizado y quick wins |
| Engineering Transformation | 2–4 meses | Modelo de ingeniería funcionando y adoptado |
| Developer Platform | 3 meses | Plataforma interna operativa y documentada |
| Reliability & Incident | 12 semanas | Gestión de incidentes y observabilidad |
| Legacy Modernization | Por etapa | Una etapa de migración en producción |

El **Technology Assessment** es la oferta de entrada, para el caso "sabemos que hay
problemas, pero no sabemos por dónde empezar".

### Framework y mapa de madurez

Cuatro fases: Diagnóstico → Planificación → Ejecución → Resultados finales.

**Mapa de madurez — metodología propia, más allá de la transcripción del deck.**
Cinco estadíos (`00` Ad hoc · `01` Estabilización · `02` Estandarización · `03`
Plataforma · `04` Escalado), pero el nivel de la organización **no se declara, se
puntúa**: se evalúan seis verticales por separado contra evidencia observable —
Código y cambios, Build y deploy, Infraestructura y ambientes, Observabilidad e
incidentes, Ownership y prácticas, Seguridad y accesos — y el estadío real es el de
la vertical más atrasada, no un promedio. Cada nivel a partir del 01 tiene un
criterio de salida explícito y medible (ej.: "rollback ejecutado con éxito en menos
de 1 hora" para pasar a Estabilización). Reglas del modelo: el nivel lo fija la
vertical más baja; no se saltean niveles; se puntúa contra evidencia, no contra
respuestas ("¿tienen CI/CD?" siempre da que sí — cronometrar un deploy real da un
número). Esta matriz vive en `index.html` `#madurez` y es la fuente de verdad;
`docs/deck-source.md` documenta solo la versión original del deck, ya superada.

### Restricciones técnicas del sitio

- Sitio **estático puro**: HTML + CSS + un archivo de JS. Sin build, sin dependencias,
  sin `node_modules`. Se publica con `git push`.
- Se sirve en **GitHub Pages como *project page*** bajo el subpath `/consulting/`, no en
  la raíz de un dominio. Las rutas del `index.html` son relativas por esa razón.
- **Presupuesto de peso**: < 25 KB gzip transferidos. Sin webfonts, sin imágenes en el
  camino crítico. Verificable con `bash scripts/size.sh`.
- **Funciona sin JavaScript.** El JS solo agrega animación de entrada y estado del nav;
  los servicios se abren con `<details>` nativo.
- **Mobile-first.** La mayor parte del tráfico entra desde el celular.

### Decisiones de producto explícitamente abiertas

Estas ambigüedades vienen del deck original y **no deben resolverse inventando el valor**.
Están marcadas con `REVISAR` en `index.html`:

1. ~~Nivel 00 del mapa de madurez.~~ **Resuelto (2026-09-06).** La matriz de
   madurez nueva (ver arriba) le da al 00 una tesis y seis descripciones propias,
   distintas de las del 01 en las seis verticales. Ya no hay ambigüedad.
2. **Duración de Reliability & Incident.** El catálogo dice 12 semanas; el ejemplo de
   "Anatomía de un proyecto" usa 8. Sin resolver.
3. **Duración del Technology Assessment.** El catálogo dice 2–4 semanas; la slide de
   oferta de entrada dice 3. Puesto como 2–4.
4. **Rangos de la timeline.** "Semanas 2–7" y "Semana 8" son reconstrucciones del deck.

Tampoco están definidos: dominio propio, precios públicos, y si habrá versión en inglés.

## Brand Commitments

- **Nombre:** Rodrigo Pizarro. Sin nombre de firma ni marca paraguas. La consultoría es
  la persona; cualquier material que sugiera una empresa con estructura es falso.
- **Descriptor:** "Consultoría de tecnología", Córdoba, Argentina.
- **Voz:** primera persona del singular ("no vendo el mantenimiento de lo que
  implemento"). Directa, sin jerga vendedora, sin superlativos, sin promesas de
  transformación genérica. Las frases del prospecto se citan textuales, en su registro
  real ("Solo Marcos sabe cómo funciona eso").
- **Registro:** español argentino. Voseo en el copy conversacional, formal en los títulos.
- **Activo existente:** el deck de 18 slides es el material que se usa en reunión. El
  sitio y el deck son la misma pieza en dos formatos y no deberían contradecirse.

## Evidence on Hand

**Lo que es real y se puede mostrar con nombre:**

- **Caso SIGES** — red de estaciones de servicio, sistema legacy en Visual FoxPro,
  operación distribuida, cinco developers. Se puede nombrar al cliente y usar las métricas
  tal como están hoy en la página: **5** developers en el equipo, **2** conocían el núcleo
  del sistema, **0** control de versiones al empezar.
- **Antes / después de SIGES** (cinco pares verificados): código repartido sin control de
  versiones → monorepo versionado; deploy estación por estación con TeamViewer → deploy a
  toda la red en segundos desde el IDP; producción como ambiente de prueba → framework de
  testing y ambientes bajos; poca visibilidad → observabilidad con Grafana; conocimiento en
  dos personas → estándares, documentación y ownership del equipo.
- **`docs/deck-source.md`** — transcripción completa del deck original.

**Lo que NO existe y ningún trabajo futuro debe fabricar:**

- No hay testimonios ni citas atribuidas a clientes. Nadie puso su nombre todavía.
- No hay otros casos documentados. SIGES es el único.
- No hay logos de clientes, premios, certificaciones, prensa ni cantidad de clientes.
- No hay precios publicados ni benchmarks de industria.
- No hay fotografía propia ni retrato profesional cargado en el repo.
- El caso SIGES está **en curso**, no cerrado. No se puede hablar de él en pasado
  concluido ni atribuirle resultados finales que todavía no ocurrieron.

**Activos faltantes que sí se esperan:** `assets/img/og.png` (1200×630) y
`assets/img/apple-touch-icon.png` (180×180).

## Product Principles

1. **El entregable es la capacidad instalada, no el software.** Todo lo que se comunique
   tiene que poder responder "¿qué queda cuando me voy?".
2. **Dos lecturas, un solo material.** Nada puede ser tan técnico que pierda al dueño, ni
   tan blando que el líder técnico deje de creerlo.
3. **El límite es el argumento.** Precio fijo, alcance cerrado y no vender el
   mantenimiento no son restricciones que se disculpan: son la propuesta de valor. Se
   dicen primero, no en la letra chica.
4. **Se muestra lo que pasó, no lo que suena bien.** Un solo caso real vale más que cinco
   inventados; la ausencia de prueba se deja en blanco antes que rellenarse.
5. **Una etapa por vez, con el sistema en producción.** Vale para cómo se moderniza un
   legacy y para cómo crece este material: nada se rompe para mejorarlo.

## Accessibility & Inclusion

Compromisos ya sostenidos por el repo y que el trabajo futuro debe preservar: contraste
AA verificado, foco visible, targets táctiles de 44 px mínimo, soporte de
`prefers-reduced-motion`, modo oscuro por `prefers-color-scheme`, safe areas de iOS, y
funcionamiento completo sin JavaScript.

El lector puede estar leyendo desde el celular, apurado, entre reuniones. Legibilidad a
distancia de brazo y cero scroll horizontal no son detalles de pulido: son condiciones.
