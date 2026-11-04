[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=DrPaulValle/MSF-IBF1020)

# Práctica 3: Modelado y control del sistema musculoesquelético

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana[cite: 2]. Esta práctica integra el modelado mecánico del tejido muscular, su conversión a analogías eléctricas mediante la relación fuerza–voltaje[cite: 93, 94], análisis temporal y de estabilidad, diseño de controladores PID, simulación computacional *in silico* y verificación cruzada entre múltiples plataformas[cite: 89, 90, 93].

El caso de estudio analiza las propiedades viscoelásticas del sistema musculoesquelético mediante una combinación de elementos contráctiles pasivos y activos, resortes y amortiguadores[cite: 87, 88]. Se busca evaluar y comparar la respuesta del desplazamiento $x(t)$ ante una fuerza aplicada $F(t)$[cite: 87, 88], evaluando la condición de un **individuo sano (control)** frente a un **caso simulado de atrofia muscular (caso)**, tanto en lazo abierto como en lazo cerrado mediante un controlador PID[cite: 87, 89].

**Docente:** Dr. Paul Antonio Valle Trujillo[cite: 3]  
**Correo:** paul.valle@tectijuana.edu.mx[cite: 3]  
**Departamento:** Ingeniería Eléctrica y Electrónica[cite: 3]  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana[cite: 3]  
**Asignatura:** Modelado de Sistemas Fisiológicos[cite: 3]  
**Programa:** Ingeniería Biomédica[cite: 2]  
**Estudiante:** Nombre completo · Número de control · correo@tijuana.tecnm.mx  

**Repositorio de la asignatura:** https://github.com/DrPaulValle/MSF-IBF1020[cite: 55]  
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo físico y analogía eléctrica](#analogia)
5. [Formulación matemática](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Señales de entrada y condiciones de simulación](#senales)
8. [Implementación en MATLAB, Simulink y Simscape](#matlab)
9. [Control en lazo cerrado y sintonización PID](#pid)
10. [Reproducción en Python](#python)
11. [Verificación entre representaciones](#verificacion)
12. [Resultados y verificación cruzada](#resultados)
13. [Flujo de trabajo](#flujo)
14. [Actividades del estudiante](#actividades)
15. [Estructura del repositorio](#estructura)
16. [Requisitos](#requisitos)
17. [Reproducibilidad y entregables](#reproducibilidad)
18. [Referencias](#referencias)

---

<a id="resumen"></a>
## Resumen

La práctica tiene como propósito **desarrollar un procedimiento completo de modelado, análisis, simulación y control *in silico*** para el sistema musculoesquelético[cite: 87, 89, 95]. Las propiedades viscoelásticas del tejido muscular se representan mediante una estructura mecánica constituida por un elemento contráctil $F_0(t)$, una amortiguación viscosa $R$ y elementos elásticos en serie ($C_s$) y en paralelo ($C_p$)[cite: 87, 88].

A través de la **analogía fuerza–voltaje**[cite: 87, 94], los elementos mecánicos se transforman en un circuito eléctrico equivalente donde las fuerzas corresponden a voltajes, las velocidades a corrientes y los desplazamientos a carga eléctrica. Se estudia el comportamiento dinámico comparando un sujeto sano frente a una patología de atrofia muscular representada por una alteración en la componente viscosa $R$[cite: 89]. Se incorpora un **controlador PID con retroalimentación negativa** que toma la respuesta del sujeto sano como referencia para corregir la respuesta del sujeto con atrofia[cite: 89]. Los resultados se validan mediante MATLAB, Simulink, Simscape Electrical y Python[cite: 89, 90, 93].

> **Nota sobre el alcance:** Esta práctica se desarrolla exclusivamente mediante **experimentación *in silico***[cite: 89, 95]. La estrategia de control tiene propósitos didácticos y computacionales, sin constituir un tratamiento clínico para la atrofia muscular[cite: 89, 90].

**Palabras clave:** sistema musculoesquelético; atrofia muscular; analogía fuerza-voltaje; controlador PID; modelado de sistemas fisiológicos; MATLAB; Simulink; Simscape Electrical; Python; simulación *in silico*.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## Competencia y objetivos

### Competencia a desarrollar

Modelizar sistemas fisiológicos mediante analogías entre sistemas físicos, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseñar estrategias de control clásico[cite: 87]. En particular, analizar un modelo mecánico del sistema musculoesquelético, construir su circuito eléctrico equivalente, comparar la respuesta de un individuo sano frente a un caso de atrofia muscular y diseñar una estrategia de control *in silico* para atenuar las diferencias dinámicas[cite: 87].

### Objetivo general

Modelar, analizar y simular la respuesta dinámica del sistema musculoesquelético ante una fuerza aplicada mediante su formulación matemática, analogía eléctrica equivalente y control por retroalimentación negativa, comparando la respuesta temporal de la condición de referencia (sano) y el caso patológico (atrofia).

### Objetivos específicos

- Identificar los componentes viscoelásticos (elemento contráctil, amortiguamiento viscoso, elasticidades serie y paralelo) y las variables de fuerza y desplazamiento[cite: 87, 88].
- Construir el circuito eléctrico equivalente aplicando la analogía fuerza–voltaje y sus reglas topológicas[cite: 87, 94].
- Derivar las ecuaciones diferenciales y la función de transferencia $G(s) = X(s)/F(s)$ para los casos de referencia y atrofia muscular[cite: 87, 91].
- Analizar la estabilidad y localización de polos en el plano complejo para ambas condiciones.
- Simular la respuesta en lazo abierto ante un impulso unitario en MATLAB, Simulink, Simscape y Python[cite: 89, 90, 91, 93].
- Diseñar y sintonizar un controlador PID para atenuar el error $e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)$[cite: 89, 92].
- Validar y verificar cruzadamente las respuestas computacionales obtenidas en las diferentes herramientas[cite: 89, 90, 93].
- Elaborar un diagrama biológico en BioRender que relacione las estructuras mecánicas con los equivalentes eléctricos[cite: 93, 94].

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## Relación con el temario

La práctica integra contenidos correspondientes a las tres unidades principales de la asignatura **Modelado de Sistemas Fisiológicos (IBF-1020)**:

| Unidad | Área | Contenidos aplicados |
|---|---|---|
| I | Sistemas de control retroalimentados[cite: 9] | Diagramas de bloques, respuesta ante impulso, análisis de error y criterios de estabilidad en el plano complejo[cite: 9, 28, 33]. |
| II | Modelado matemático[cite: 9] | Analogía mecánica–eléctrica (fuerza–voltaje)[cite: 10, 94], leyes de Kirchhoff[cite: 13], modelo dinámico del sistema musculoesquelético[cite: 10, 87] y función de transferencia[cite: 12]. |
| III | Controladores[cite: 10] | Configuración del controlador PID[cite: 11, 37], sintonización de ganancias $k_P, k_I, k_D$[cite: 10, 39] y retroalimentación negativa[cite: 11, 14]. |

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## Modelo físico y analogía eléctrica

### Descripción del modelo mecánico

El compartimento musculoesquelético se aproxima mediante un modelo mecánico compuesto por[cite: 87, 88]:
- $F_0(t)$: Fuerza desarrollada por el elemento contráctil activo del músculo ($F_0(t) = \alpha F(t)$, con $0 < \alpha < 1$)[cite: 87, 88].
- $R$: Amortiguación viscosa inherente al tejido muscular[cite: 88].
- $C_s$: Elasticidad del elemento en serie (asociada a los tendones)[cite: 88].
- $C_p$: Elasticidad del elemento en paralelo (asociada al sarcolema y estructuras pasivas)[cite: 88].
- $x(t)$: Desplazamiento total del elemento elástico paralelo[cite: 88].
- $x_1(t)$: Desplazamiento del elemento elástico en serie $C_s$[cite: 88].

### Analogía Fuerza–Voltaje (Mecánica a Eléctrica)

| Sistema mecánico | Variable eléctrica análoga | Interpretación fisiológica[cite: 87, 88] |
|---|---|---|
| Fuerza $F(t)$[cite: 94] | Voltaje $V(t)$[cite: 94] | Fuerza de tracción / excitación muscular[cite: 87] |
| Velocidad $\dot{x}(t)$[cite: 94] | Corriente $I(t)$[cite: 94] | Velocidad de deformación muscular[cite: 94] |
| Desplazamiento $x(t)$[cite: 94] | Carga eléctrica $q(t)$[cite: 94] | Deformación / elongación muscular[cite: 87, 88] |
| Amortiguador $R$[cite: 94] | Resistencia $R$[cite: 94] | Viscosidad y fricción tisular[cite: 88] |
| Compliancia $C_s, C_p$[cite: 94] | Capacitancia $C_s, C_p$[cite: 94] | Elasticidad pasiva y tendinosa[cite: 88] |
| Masa $M$[cite: 94] | Inductancia $L$[cite: 94] | Inercia de la masa muscular[cite: 94] |

> **Regla topológica de conversión:** Los componentes mecánicos conectados en paralelo se representan mediante elementos eléctricos en serie, mientras que elementos mecánicos en serie se representan como elementos eléctricos en paralelo[cite: 94].

### Parámetros eléctricos equivalentes para la simulación

| Parámetro[cite: 89] | Unidades[cite: 89] | Condición Control (Sano)[cite: 89] | Condición Caso (Atrofia)[cite: 89] |
|---|---|---|---|
| Entradas $F(t)$[cite: 89] | $\mathrm{V}$[cite: 89] | $1\,\mathrm{V}$[cite: 89] | $1\,\mathrm{V}$[cite: 89] |
| Factor $\alpha$[cite: 87] | Adimensional | $0.25$ | $0.25$ |
| Compliancia serie $C_s$[cite: 89] | $\mu\mathrm{F}$[cite: 89] | $10\,\mu\mathrm{F}$[cite: 89] | $10\,\mu\mathrm{F}$[cite: 89] |
| Compliancia paralelo $C_p$[cite: 89] | $\mu\mathrm{F}$[cite: 89] | $100\,\mu\mathrm{F}$[cite: 89] | $100\,\mu\mathrm{F}$[cite: 89] |
| Resistencia viscosa $R$[cite: 89] | $\Omega$[cite: 89] | $100\,\Omega$[cite: 89] | $10\,\mathrm{k}\Omega$ ($10\,000\,\Omega$)[cite: 89] |

La atrofia muscular se modela incrementando la resistencia $R$ de $100\,\Omega$ a $10\,\mathrm{k}\Omega$, afectando la componente viscosa y alterando la respuesta temporal del músculo[cite: 89].

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## Formulación matemática

### 1. Ecuaciones del circuito y del sistema

A partir del equilibrio de fuerzas y las relaciones constitutivas del circuito equivalente, considerando el desplazamiento $x(t)$ como la variable de salida, se establece la relación integro-diferencial que rige la dinámica del sistema[cite: 10].

### 2. Función de transferencia

Aplicando la transformada de Laplace con condiciones iniciales nulas ($\mathcal{L}\{\cdot\}$)[cite: 12], se obtiene la función de transferencia entre el desplazamiento y la fuerza aplicada:

$$\boxed{G(s) = \frac{X(s)}{F(s)}}$$

Sustituyendo los parámetros numéricos para cada caso:
- $G_{\text{control}}(s)$ para el individuo sano ($R = 100\,\Omega$)[cite: 89].
- $G_{\text{caso}}(s)$ para el caso de atrofia ($R = 10\,\mathrm{k}\Omega$)[cite: 89].

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## Análisis temporal y de estabilidad

### 1. Error en estado estacionario

El error en estado estacionario se evalúa considerando la respuesta final ante la señal de entrada, analizando cómo el cambio de la resistencia viscosa $R$ impacta el valor final y el seguimiento de referencia[cite: 10, 26, 27].

### 2. Polos y estabilidad

Se calculan las raíces del denominador de la función de transferencia $G(s)$[cite: 12]:
- Para $R, C_s, C_p > 0$, los polos se ubican en el semiplano izquierdo del plano complejo ($\mathrm{Re}(\lambda_i) < 0$), lo que garantiza la estabilidad BIBO del sistema[cite: 28, 29].
- Se compara el movimiento de los polos al cambiar de $R = 100\,\Omega$ a $R = 10\,\mathrm{k}\Omega$, analizando el nivel de amortiguamiento y la velocidad de respuesta del sistema muscular atrófico[cite: 29, 89].

[Volver al contenido](#contenido)

---

<a id="senales"></a>
## Señales de entrada y condiciones de simulación

El intervalo nominal de simulación se establece en $0 \le t \le 10\,\mathrm{s}$.

| Señal | Definición computacional | Propósito |
|---|---|---|
| Impulso unitario | Pulso rectangular de alta amplitud o función impulso en $t=0$[cite: 18, 91] | Evaluar la respuesta natural y la relajación viscoelástica muscular[cite: 29, 91] |

[Volver al contenido](#contenido)

---

<a id="matlab"></a>
## Implementación en MATLAB, Simulink y Simscape

Se evalúan tres representaciones equivalentes para ambas condiciones (Control y Caso)[cite: 89, 91]:

| Implementación | Descripción | Aspecto a verificar |
|---|---|---|
| Modelo integro-diferencial | Diagrama de bloques en Simulink basado en ecuaciones de equilibrio[cite: 10, 79] | Correcta integración de las derivadas de deformación[cite: 11] |
| Función de transferencia[cite: 91] | Bloque `Transfer Fcn` con $G(s)$[cite: 12] | Respuesta dinámica entrada-salida[cite: 13] |
| Circuito Simscape Electrical[cite: 91] | Esquema físico con componentes de dominio eléctrico[cite: 10, 79] | Consistencia entre la analogía física y los bloques matemáticos[cite: 10] |

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## Control en lazo cerrado y sintonización PID

### 1. Esquema de retroalimentación

Se utiliza la respuesta del individuo sano $x_{\text{control}}(t)$ como señal de referencia[cite: 89, 92]. La señal de error aplicada al controlador está dada por[cite: 89, 92]:

$$e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)$$

El controlador PID genera una señal de corrección $u(t)$ que actúa sobre el modelo del paciente atrófico para igualar la respuesta dinámica del sujeto sano[cite: 11, 89, 92].

### 2. Sintonización

Utilizando la herramienta **Tune** del bloque `PID Controller` en Simulink[cite: 10, 58], se determinan las ganancias óptimas $k_P$, $k_I$ y $k_D$[cite: 58]. El objetivo es lograr una respuesta estable que minimice el error de seguimiento y elimine oscilaciones indeseadas[cite: 10, 11, 58].

[Volver al contenido](#contenido)

---

<a id="python"></a>
## Reproducción en Python

A través de **Visual Studio Code** y la biblioteca `scipy.signal` / `control`, se implementan los scripts en Python para:
1. Definir las funciones de transferencia $G_{\text{control}}(s)$ y $G_{\text{caso}}(s)$[cite: 91].
2. Obtener la respuesta al impulso en lazo abierto[cite: 91].
3. Configurar el lazo cerrado incorporando el PID con las ganancias $k_P, k_I, k_D$ sintonizadas[cite: 92, 93].
4. Exportar los gráficos resultantes a formato PDF para su integración en la documentación[cite: 92, 93].

[Volver al contenido](#contenido)

---

<a id="verificacion"></a>
## Verificación entre representaciones

Se comparan las respuestas numéricas obtenidas en:
- Ecuaciones integro-diferenciales (Simulink)[cite: 91]
- Función de transferencia (Simulink)[cite: 91]
- Circuito Simscape Electrical[cite: 91]
- Cuaderno computacional de MATLAB (`.mlx`)
- Código ejecutable en Python (`.py`)

Todas las representaciones deben alinearse con precisión matemática, justificando cualquier ligera desviación asociada al solucionador numérico (*solver*) empleado[cite: 63, 71].

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## Resultados y verificación cruzada

Convención gráfica de colores utilizada[cite: 62]:
- **Línea Amarilla:** Señal de entrada / Referencia aplicada[cite: 62].
- **Línea Azul:** Respuesta de la planta en lazo abierto (Sujeto Sano - Control)[cite: 62, 89].
- **Línea Roja / Guiones:** Respuesta de la planta en lazo abierto (Sujeto con Atrofia - Caso)[cite: 62, 89].
- **Línea Verde:** Respuesta en lazo cerrado con controlador PID ($x_{\text{PID}}(t)$)[cite: 62, 92].

[Volver al contenido](#contenido)

---

<a id="flujo"></a>
## Flujo de trabajo

```mermaid
flowchart TD
    A[Modelo mecánico del músculo] --> B[Analogía Fuerza-Voltaje]
    B --> C[Circuito eléctrico equivalente RLC]
    C --> D[Ecuaciones integro-diferenciales]
    C --> E[Función de Transferencia Gs]
    E --> F[Análisis de Polos y Estabilidad]
    D --> G[Simulink: Bloques integro-diferenciales]
    E --> H[Simulink: Función de transferencia]
    C --> I[Simscape Electrical: Circuito físico]
    G --> J[Respuesta en Lazo Abierto]
    H --> J
    I --> J
    E --> K[Sistema de Control PID en Lazo Cerrado]
    K --> L[Sintonización Tune kP, kI, kD]
    L --> M[Simulación en Python]
    L --> N[Diagrama Biológico en BioRender]
    J --> O[Verificación Cruzada de Resultados]
    L --> O
    M --> O
    O --> P[Documentación en GitHub y README.md]
```

[Volver al contenido](#contenido)

---

<a id="actividades"></a>
## Actividades del estudiante

- [ ] **Etapa 1:** Analizar el modelo mecánico y transformar las variables a la analogía eléctrica fuerza–voltaje[cite: 90].
- [ ] **Etapa 2:** Derivar las ecuaciones diferenciales y la función de transferencia $G(s)$ para los casos de Control y Caso.
- [ ] **Etapa 3:** Realizar el análisis de estabilidad y ubicación de polos para ambas condiciones.
- [ ] **Etapa 4:** Construir los modelos en Simulink (ecuaciones y $G(s)$) y Simscape Electrical.
- [ ] **Etapa 5:** Diseñar el lazo cerrado en Simulink, sintonizar el PID y registrar las ganancias $k_P, k_I, k_D$.
- [ ] **Etapa 6:** Reproducir la simulación mediante código en Python dentro de Visual Studio Code.
- [ ] **Etapa 7:** Diseñar el diagrama biológico representativo en BioRender.
- [ ] **Etapa 8:** Documentar el trabajo, subir código y figuras al repositorio de GitHub y completar el archivo `CITATION.cff`.

[Volver al contenido](#contenido)

---

<a id="estructura"></a>
## Estructura del repositorio

```text
.
├── README.md                      # Reporte de la práctica y guía de reproducción
├── CITATION.cff                   # Archivo de citación académica
├── Apellido_NoControl.mlx         # Cuaderno de MATLAB del estudiante
├── Apellido_NoControl.pdf         # Exportación del cuaderno de MATLAB
├── modelo_musculoesqueletico.slx  # Modelo de Simulink y Simscape
├── modelo_musculoesqueletico.py   # Script de simulación en Python
├── diagrama_biologico.png        # Ilustración elaborada en BioRender
└── evidencias/                   # Gráficas en formato PDF/PNG y capturas
```

[Volver al contenido](#contenido)

---

<a id="requisitos"></a>
## Requisitos

### Software[cite: 59, 73]
- **MATLAB** (con Simulink y Control System Toolbox)[cite: 59, 73].
- **Simscape Electrical**[cite: 59, 73].
- **Python 3.x** con entornos **Visual Studio Code**[cite: 73].
- Bibliotecas de Python: `numpy`, `scipy`, `matplotlib`, `control`[cite: 73].
- **BioRender** (o herramienta equivalente) para diagramas biológicos[cite: 14, 73].
- **Git** y **GitHub** para control de versiones y publicación[cite: 55, 73].

[Volver al contenido](#contenido)

---

<a id="reproducibilidad"></a>
## Reproducibilidad y entregables

### Resultados mínimos esperados

| Entregable | Contenido requerido |
|---|---|
| **Matemático**[cite: 91] | Ecuaciones integro-diferenciales, función de transferencia $G(s)$ y polos de ambos casos[cite: 91]. |
| **Simulink**[cite: 91] | Modelo `.slx` con bloques matemáticos, función de transferencia y Simscape[cite: 91]. |
| **Control PID**[cite: 92] | Ganancias sintonizadas ($k_P, k_I, k_D$) y gráfica comparativa del lazo cerrado[cite: 92]. |
| **Python**[cite: 93] | Código `.py` ejecutable y gráficos exportados en PDF[cite: 93]. |
| **Diagrama**[cite: 93] | Esquema biológico-eléctrico exportado desde BioRender[cite: 93]. |
| **Repositorio**[cite: 94] | `README.md`, `CITATION.cff`, código fuente y gráficos organizados[cite: 94]. |

[Volver al contenido](#contenido)

---

<a id="referencias"></a>
## Referencias

[1] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed., IEEE Press, 2018[cite: 7].  
[2] F. C. Hoppensteadt y C. S. Peskin, *Modeling and Simulation in Medicine and the Life Sciences*, Springer[cite: 7].  
[3] J. E. Hall, *Guyton and Hall Textbook of Medical Physiology*, 14th ed., Elsevier, 2021[cite: 7].  
[4] K. Ogata, *Ingeniería de Control Moderna*, 5.ª ed., Pearson Educación, 2010[cite: 7].  
[5] N. S. Nise, *Control Systems Engineering*, 8th ed., John Wiley & Sons, 2020[cite: 7].  
[6] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B. C., México, 2026[cite: 7].  
[7] Tecnológico Nacional de México, *Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos, IBF-1020*[cite: 7].  

---

## Uso académico

Este repositorio es una evidencia académica desarrollada para la asignatura **Modelado de Sistemas Fisiológicos**[cite: 2]. Los modelos y simulaciones son de carácter didáctico *in silico*[cite: 89, 95] y no deben ser utilizados como recomendaciones o protocolos de diagnóstico/tratamiento médico real[cite: 74, 90].