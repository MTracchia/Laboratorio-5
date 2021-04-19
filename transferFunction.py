
import numpy as np
import matplotlib.pyplot as plt
import time
from lockin import SR830

#Defino listas y parámetros
Tv_list = []	#Tv = Transfer value
steps = 50
ref_v = 0.1

#Función que me devuelve R y Theta
def getR (lock):
	R, theta = lock.getMedicion('RT')
 	return R 	

if __name__ == '__main__':
	
	config = {
          'lockin_addr': 'GPIB0::11::INSTR',
          'medicion_modo' : 0, 
          'display_modo' : 'RT', 
          'sens' : 21,
          'slope' : 3, 
          't_int' : 6,
          'ref_intern' : True,
          'ref_freq' : 40,
          'ref_v' : ref_v,
          }

    #Instancio la clase SR830
	lock_in = SR830(config)
	time.sleep(2)
	#t_int = lock.getIntegrationTime() #Descomentar en caso de emergencia

	#Esto es para tomar la medición del R varias veces
	for stp in steps:
		R_val = getR(lock_in)
		T_val = (R_val/ref_v)
		Tv_list.append(T_val)
		#time.sleep(0.1) #Posiblemente se tenga que dormir x segundos, por cada iteración.

	#Para graficar la función de transferencia en función de los pasos
 	plt.figure()
 	plt.plot(Tv_list)
 	plt.xlabel('Paso')
	plt.ylabel('R/Vin')