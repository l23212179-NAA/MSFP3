# Práctica 3: Modelado y control del sistema musculoesquelético

## Información de la estudiante

Nicole Arredondo Arevalo [23212179]; L23212179@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Modeliza sistemas fisiológicos mediante analogías entre sistemas físicos, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseña estrategias de control mediante técnicas de control clásico[cite: 1].

## Objetivos

1. Estudiar un modelo mecánico simplificado del sistema musculoesquelético, considerando sus componentes contráctiles, elásticos y amortiguadores [cite: 1].
2. Representar el modelo mecánico mediante un circuito eléctrico equivalente, aplicando la analogía fuerza-voltaje para relacionar los elementos de ambos sistemas [cite: 1].
3. Obtener las ecuaciones diferenciales que describen el comportamiento del sistema y determinar su función de transferencia [cite: 1].
4. Aplicar el principio de superposición y la transformada de Laplace para calcular las funciones de transferencia de un individuo sano y de un caso simulado de atrofia muscular [cite: 1].
5. Simular el comportamiento del sistema en MATLAB/Simulink y Simscape Electrical para analizar sus respuestas en lazo abierto [cite: 1].
6. Diseñar y ajustar un controlador PID en Simulink para reducir las diferencias entre la respuesta del sistema con atrofia muscular y la del individuo sano [cite: 1].
7. Elaborar un cuaderno computacional en MATLAB y un programa complementario en Python para verificar, graficar y comparar los resultados de las simulaciones [cite: 1].
8. Representar mediante una ilustración en BioRender la relación entre el sistema musculoesquelético, su modelo mecánico y su circuito eléctrico equivalente [cite: 1].

## Descripción detallada del sistema

En esta práctica se analiza un modelo mecánico simplificado del sistema musculoesquelético, basado en la representación viscoelástica descrita por Khoo [cite: 1]. El modelo está compuesto por una fuerza activa generada por el elemento contráctil $F_0(t)$, un amortiguador viscoso ($R$), que representa la disipación de energía en los tejidos, y dos elementos elásticos, $C_p$ y $C_s$, conectados en paralelo y en serie, respectivamente, que representan las propiedades elásticas del sarcolema y los tendones [cite: 1].

Para facilitar el análisis mediante circuitos eléctricos, se utiliza la analogía fuerza-voltaje, en la que la fuerza mecánica corresponde al voltaje, la velocidad a la corriente y el desplazamiento a la carga eléctrica. Asimismo, el amortiguador viscoso se representa mediante una resistencia, mientras que los elementos elásticos se modelan utilizando capacitores [cite: 1].

Se consideran dos condiciones para estudiar y comparar el comportamiento del sistema: un individuo sano, que funciona como referencia, y un caso simulado de atrofia muscular. Esta última condición se representa mediante un incremento considerable del amortiguamiento $R$, cuyo valor cambia de $100\ \Omega$ en el individuo sano a $10\ \text{k}\Omega$ en el caso de atrofia muscular [cite: 1]. Finalmente, se toma la respuesta del individuo sano como referencia para diseñar un sistema de control con retroalimentación mediante un controlador PID, con el objetivo de reducir las diferencias en la respuesta del sistema provocadas por la atrofia muscular [cite: 1].

Palabras clave: Sistema musculoesquelético; Analogía fuerza-voltaje; Modelo viscoelástico; Atrofia muscular; Controlador PID; Simscape Electrical; BioRender.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB `[.mlx y .pdf]`
2. Modelo de Simulink `[.slx]`
3. Archivo de Python `[.py]`
4. Análisis matemático realizado a mano: Modelo de ecuaciones, aplicación del principio de superposición y funciones de transferencia para cada condición `[.pdf]`.
5. Ilustración del sistema fisiológico realizada en BioRender `[.pdf]`.
6. Figuras de las simulaciones y resultados en formato PDF:
   * Respuestas en lazo abierto del individuo sano (control) y el caso de atrofia muscular `[.pdf]`.
   * Respuestas del sistema con el controlador PID sintonizado `[.pdf]`.

## Referencias

[1] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/[cite: 1]

[2] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

[3] N. S. Nise, *Control Systems Engineering*, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.