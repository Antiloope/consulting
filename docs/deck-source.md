# Deck original — transcripción

Fuente: `Consultoría de tecnología - Rodrigo Pizarro.pdf` (18 slides).

Extraído del PDF con el `ToUnicode` CMap del subset de fuente embebido. La fuente no
incluía glifos para `Z`, `Y`, `W`, `J`, `H`, `Í`, `Ó`, `É`, `Á` mayúsculas ni para el
guion `-`, así que **los títulos en mayúscula y los rangos numéricos están reconstruidos**.
Donde quedó ambigüedad, está marcado con ⚠️.

---

## 01 · Portada

> CONSULTORÍA DE TECNOLOGÍA
> CÓRDOBA, ARGENTINA
>
> **MODERNIZACIÓN TECNOLÓGICA PARA PYMES CON SOFTWARE CRÍTICO**
>
> Crecer adaptando el software a la velocidad del negocio
>
> Rodrigo Pizarro

## 02 · Lo que se escucha

- "Solo Marcos sabe cómo funciona eso."
- "Tenemos miedo de tocar producción"
- "El conocimiento está en la cabeza de una persona"
- "No tenemos ambiente de testing"
- "Cada cambio da un poco de miedo"
- "Siempre apagando incendios"
- "El sistema no acompaña el crecimiento"

## 03 · El problema

> La empresa creció alrededor de su software.
> La forma de construirlo y mantenerlo no evolucionó a la velocidad del negocio.

## 04 · El framework de la solución

| Fase | Nombre | Descripción |
|---|---|---|
| 1 | Diagnóstico | Cómo funcionan hoy la tecnología, el equipo completo y la operación. |
| 2 | Planificación | Dependiendo el diagnóstico se arman caminos concretos a seguir |
| 3 | Ejecución | Se colabora en la ejecución del plan para dejar a la organización en un nuevo nivel |
| 4 | Resultados finales | Comparando el antes y después del proceso. El equipo queda preparado para seguir creciendo con autonomía. |

## 05 · Mapa de madurez tecnológica

> Cada organización es distinta y, con el diagnóstico inicial, el objetivo es comprender
> el estadío de madurez tecnológica actual y planificar a qué nuevo nivel se pretende llegar.

| Nivel | Nombre | Descripción |
|---|---|---|
| 00 | Ad hoc | Versionado, ambientes, incidentes ⚠️ *(idéntico al 01 en el deck — probable error)* |
| 01 | Estabilización | Versionado, ambientes, incidentes |
| 02 | Estandarización | Stack, prácticas, lineamientos, ownership |
| 03 | Plataforma | IDP, CI/CD, costos de infraestructura |
| 04 | Escalado | SRE, métricas, on-call, SLA, soporte |

## 06 · (slide sin contenido)

Solo dos títulos, sin cuerpo:

- ¿En qué consisten los niveles?
- Ejemplos de procesos de transición de estadíos

## 07 · Catálogo de intervenciones

| Intervención | Duración | Resultado |
|---|---|---|
| Technology Assessment | 2–4 semanas | Diagnóstico, roadmap priorizado y quick wins |
| Engineering Transformation | 2–4 meses | Modelo de ingeniería funcionando y adoptado |
| Developer Platform | 3 meses | Plataforma interna operativa y documentada |
| Reliability & Incident | 12 semanas ⚠️ | Gestión de incidentes y observabilidad |
| Legacy Modernization | Por etapa | Una etapa de migración en producción |

## 08 · Oferta de entrada — Technology Transformation Assessment

> "Sabemos que hay problemas, pero no sabemos por dónde empezar."

**3 semanas** ⚠️ *(el catálogo dice 2–4)*

Entregables:
- Current state y pain points
- Target state
- Roadmap priorizado por impacto y esfuerzo
- Quick wins
- Presentación ejecutiva para dirección

## 09 · Engineering Transformation — 2–4 meses

> Desarrollar software de forma profesional y predecible.

- **Engineering** — Git, arquitectura, estándares, testing, code review
- **Delivery** — CI/CD, ambientes, releases, rollback
- **Way of working** — Backlog, planificación, roles, ownership
- **Developer experience** — Templates, onboarding, automatizaciones

## 10 · Developer Platform — 3 meses

> Un developer nuevo hace por sí mismo lo que antes requería conocer cinco proveedores,
> tres máquinas y dos personas.

- Repos y templates
- CI/CD y rollback
- Infra como código
- Ambientes y secrets
- Observabilidad

## 11 · Reliability & Incident Transformation — 12 semanas

> "¿Quién sabe arreglar esto?"
> "¿Cuál es el proceso para resolver esto?"

- **Incident management** — Niveles de soporte, escalamiento, war rooms
- **Reliability** — Observabilidad, métricas, alertas, ownership
- **Aprendizaje** — Postmortems y seguimiento de acciones
- **Equipo** — Capacitación, simulaciones, documentación

## 12 · Legacy Modernization — Especialización

> Una etapa por vez, con el sistema en producción.

1. Identificar dominio
2. Encapsular
3. Crear nueva API
4. Migrar funcionalidad
5. Retirar el componente legacy

## 13 · Caso en curso — SIGES

> Red de estaciones de servicio. Sistema legacy en Visual FoxPro, operación distribuida,
> cinco developers.

- **5** developers en todo el equipo
- **2** conocían el núcleo del sistema
- **0** control de versiones al empezar

## 14 · Antes y después

| Antes | Después |
|---|---|
| Código repartido, sin control de versiones | Monorepo versionado con arquitectura limpia |
| Deploy estación por estación con TeamViewer | Deploy a toda la red en segundos desde el IDP |
| Producción como ambiente de prueba | Framework de testing y ambientes bajos |
| Poca visibilidad de la operación | Observabilidad de toda la red con Grafana |
| Conocimiento concentrado en dos personas | Estándares, documentación y ownership del equipo |

## 15 · Manifiesto

> No modernizamos solamente el software. Modernizamos la capacidad de la empresa para
> producir, desplegar y operar software.
>
> Esa capacidad es lo que queda cuando el proyecto termina.

## 16 · Anatomía de un proyecto — Ejemplo: Reliability en 8 semanas

| Cuándo | Qué | Detalle |
|---|---|---|
| Semana 1 | Inicio | Assessment y acuerdo de alcance |
| Semanas 2–7 ⚠️ | Implementación | Procesos y herramientas funcionando |
| Semana 8 ⚠️ | Adopción | Capacitación, simulación y ajustes |
| Cierre | Entrega | Documentación y ownership interno |

## 17 · Modelo de trabajo

- **Precio fijo** — Se compra un resultado en un plazo, no horas de consultor.
- **Principio y fin** — Alcance cerrado, con exclusiones explícitas en la propuesta.
- **Sin dependencia** — No vendo el mantenimiento de lo que implemento.

**Lo que no vendo:** Desarrollo a medida, staff augmentation, soporte IT, consultoría por hora.

## 18 · Primer paso

> **EMPECEMOS POR ENTENDER CÓMO ESTÁ HOY**
>
> Una conversación de 30 minutos para ver si hay un problema que valga la pena resolver.
>
> email@dominio.com *(placeholder en el deck)*
> linkedin.com/in/usuario *(placeholder en el deck)*

---

## Paleta extraída del PDF

| Color | Apariciones | Rol |
|---|---|---|
| `#000000` | 345 | Texto |
| `#555555` | 67 | Texto secundario |
| `#0f0f0f` | 65 | Fondos oscuros |
| `#f5f5f5` | 57 | Fondo alterno |
| `#026fd7` | 37 | **Acento único** |
| `#e4e4e4` | 31 | Bordes |
| `#fcfcfc` | 30 | Fondo de página |
| `#484848` `#a5a5a5` `#d1d1d1` `#b7b7b7` `#cecece` | <10 | Grises de apoyo |
