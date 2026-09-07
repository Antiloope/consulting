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

- **Origen del contenido:** el copy vivo vive en `index.html`. La página arrancó a
  partir de un deck comercial; esa transcripción ya no forma parte del repo.
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

Este catálogo **no está publicado en la landing**: la página cuenta el método
(diagnóstico → mapa de madurez → plan), no la lista de productos. Vive acá para la
conversación y para la propuesta.

### Framework y mapa de madurez

Cuatro fases: Diagnóstico → Planificación → Ejecución → Resultados finales.

**Mapa de madurez — metodología propia, más allá de la transcripción del deck.**
Cinco estadíos (`00` Frágil · `01` Controlado · `02` Repetible · `03`
Autónomo · `04` Previsible), pero el nivel de la organización **no se declara, se
puntúa**: se evalúan seis verticales por separado contra evidencia observable —
Ownership y cultura, Desarrollo, DevOps e infraestructura, Testing y calidad,
Observabilidad y soporte, Seguridad y políticas — y el estadío real es el de
la vertical más atrasada, no un promedio. Cada nivel a partir del 01 tiene un
criterio de salida explícito y medible (ej.: "rollback ejecutado con éxito en menos
de 1 hora" para pasar a Controlado). Reglas del modelo: el nivel lo fija la
vertical más baja; no se saltean niveles; se puntúa contra evidencia, no contra
respuestas ("¿tienen CI/CD?" siempre da que sí — cronometrar un deploy real da un
número). En `#madurez` la landing publica los ejes completos y **una sola vertical
de muestra** ("Ownership y cultura", fila `.matrix__row--sample`); las otras cinco
quedan en placeholder porque el criterio de cada celda es parte de la propuesta de
negocio y se trabaja en el diagnóstico.

**Entregables anunciados en la landing.** `#framework` dice qué devuelve el
diagnóstico (informe ejecutivo y otro detallado, con puntos sobre la matriz de
madurez comparados a estándares de industria) y `#servicios` qué devuelve el plan
(alternativas de acción, calendarización del plan elegido, accionables ordenados
por impacto y esfuerzo). Son promesas públicas: si cambia la forma de trabajar,
cambian primero acá.

### Restricciones técnicas del sitio

- Sitio **estático puro**: HTML + CSS + un archivo de JS. Sin build, sin dependencias,
  sin `node_modules`. Se publica con `git push`.
- Se sirve en **GitHub Pages como *project page*** bajo el subpath `/consulting/`, no en
  la raíz de un dominio. Las rutas del `index.html` son relativas por esa razón.
- **Presupuesto de peso**: < 25 KB gzip transferidos. Sin webfonts, sin imágenes en el
  camino crítico. Verificable con `bash scripts/size.sh`.
- **Funciona sin JavaScript.** El JS solo agrega animación de entrada y estado del nav.
  Ninguna sección depende de él para mostrar su contenido.
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

- **Perfil de Rodrigo** — ingeniero en Computación, cinco años desarrollando software
  en Mercado Libre, experiencia de consultoría con PyMEs y proyectos propios.
- **Retrato de Rodrigo** — `assets/img/rodrigo-pizarro.jpg`, autorizado para la landing.
- **Una vertical del mapa de madurez publicada** — "Ownership y cultura", con sus cinco
  niveles escritos. Es la única celda de método que la landing muestra completa y hace de
  prueba de que la matriz existe.

**Lo que NO existe y ningún trabajo futuro debe fabricar:**

- No hay casos publicados. La landing no tiene sección de caso testigo y **no se
  reintroduce una sin decisión explícita**: se sacó a propósito.
- No hay testimonios ni citas atribuidas a clientes. Nadie puso su nombre todavía.
- No hay logos de clientes, premios, certificaciones, prensa ni cantidad de clientes.
- No hay precios publicados ni benchmarks de industria.

**Activos de marca ya publicados:** `assets/img/og.png` (1200×630) y
`assets/img/apple-touch-icon.png` (180×180), regenerables con `scripts/gen-images.sh`.
`assets/img/favicon.svg` y el retrato `assets/img/rodrigo-pizarro.jpg` también están
en el repo.

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
