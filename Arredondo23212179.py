"""
Práctica 3: Modelado y control del sistema musculoesquelético

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Nicole Arredondo Arevalo
Número de control: 23212179
Correo institucional: l23212179@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy as np 
import matplotlib.pyplot as plt
import control as ctrl

# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,10,5
#x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5
N = round((tend-t0)/dt)+1 
t = np.linspace(t0,tend,N) 
u = np.zeros(N)
u[round(1/dt):round(2/dt)]=1


#Funcion de transferencia CASO
def casos(R):
    a,Cp,Cs=0.25,100E-6,10E-6
    # Componentes del circuito RC y FC
    num = [Cs*R,1-a]
    den = [R*(Cs+Cp),1]
    sys = ctrl.tf(num, den)
    # Polos del sistema
    L= np.roots(den)
    return sys,L

#Funcion de transferencia CONTROL
R= 100
sysControl,L = casos(R)
print(f"Funcion de transferencia del control:{sysControl}")
print(f"Polos del sistema: L1 = {L[0]:.3e}\n")
#Llamar FC del caso
R= 10E3
sysCaso,L = casos(R)
print(f"Funcion de transferencia del control:{sysCaso}")
print(f"Polos del sistema: L1 = {L[0]:.3e}\n")

#Colores
clr1 = np.array([92, 46, 60])/255
clr2 = np.array([87, 128, 136])/255
clr3 = np.array([202, 126, 76])/255
clr4 = np.array([157, 217, 210])/255

#Componentes del Controlador PI
kP = 0.217027995506822
kI = 3671.16027000031
Cr = 1e-6
Re = 1/(kI*Cr)
Rr = kP*Re
numPID = [Rr*Cr,1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID, denPID)

# Sistema de control en lazo cerrado
print(f"Funcion de transferencia del caso en lazo cerrado: {PID} \n")

#Funciones del sistema en lazo abierto y lazo cerrado
_,Fsx = ctrl.forced_response(sysControl,t,u,x0) #Control
_,Fsy = ctrl.forced_response(sysCaso,t,u,x0) #Caso

sysPID=ctrl.feedback(ctrl.series(PID,sysCaso),1,sign =-1) #Pi con caso
_,PI = ctrl.forced_response(sysPID,t,Fsx,x0) #PI Tratamiento usando control 

#Respuestas: Simulaciones numericas
fg=plt.figure(1)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.plot(t,u,'-',linewidth=1,color=clr1,label='F(t)')
plt.plot(t,Fsx,'-',linewidth=1,color=clr2,label='Fs(t): Control')
plt.plot(t,Fsy,':',linewidth=1,color=clr3,label='Fs(t): Caso')
plt.plot(t,PI,'--',linewidth=1,color=clr4,label='PI(t): Tratamiento')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-0.2,1.2); plt.yticks(np.arange(-0.2,1.3,0.1))
plt.xlabel('t[s]')
plt.ylabel ('F(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25), loc='center', ncol=4,frameon=False)
fg.savefig('Caso_python.pdf',bbox_inches='tight')
plt.show()
