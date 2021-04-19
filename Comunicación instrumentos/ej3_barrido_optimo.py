'''
Autores: Grupo 9
Ejercicio 4: densidad espectral
'''

import numpy as np
import matplotlib.pyplot as plt
import time
from lockin import SR830


ref_v=0.5
cant=10
pasos = 50
lista_parametros = [6,5,4,3,2,1]

def barrido(lock, pasos, tint_parametro,cant):
    
    #Defino listas internas
    r_values=[]
    r_vector_prom = []
    sigma_vector= []

    #Para adquirir el tiempo de integración
    setIntegrationTime(tint_parametro)
    time.sleep(3)
    t_int=getIntegrationTime(tint_parametro)
    time.sleep(3)
    
    #Defino el intervalo de frecuencias de acuerdo al tiempo de integración
    frecfin=1.0/t_int                
    frecini=frecfin-100 
    freqvec = np.linspace(frecini, frecfin, pasos)

    #Obtengo R y errores
    for f in freqvec:
        lock.setFreqReferencia(f)
        for n in range(cant):
            time.sleep(2*t_int)
            r, theta = lock.getMedicion('RT')
            r_values.append(r)
        r_ave=np.sum(r_values)/cant
        r_sigma=np.std(r_values)
        r_vector_prom.append(r_ave)
        sigma_vector.append(r_sigma)
        r_values=[]


    return freqvec, r_vector_prom, sigma_vector



if __name__ == '__main__':

    config = {
          'lockin_addr': 'GPIB0::8::INSTR',
          'medicion_modo' : 0, 
          'display_modo' : 'RT', 
          'sens' : 21,
          'slope' : 3, 
          't_int' : 7,
          'ref_intern' : True,
          'ref_freq' : 180,
          'ref_v' : ref_v,
          }
    
    lock_in = SR830(config)
    time.sleep(20)
 


    for tint_parametro in lista_parametros:  
        F, R, Sigma=barrido(lock, pasos, tint_parametro,cant)
        
        for f_intervalo,R_intervalo,Sigma_intervalo in zip(F,R,Sigma):
            lista_frec.append(f_intervalo)
            lista_R.append(R_intervalo)
            lista_Sigma.append(Sigma_intervalo)


    T= list(map(lambda x: x/ref_v,lista_R))
    T_sigma = list(map(lambda x: x/ref_v,lista_Sigma))
    
    #Funcion de transferencia con los errores
    plt.figure()
    plt.plot(lista_frec,T)
    plt.errorbar(lista_frec,T,yerr=T_sigma,fmt="",elinewidth=2.8) #ojo! la yerr es la mitad de la longitud total de la barra de error
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('T')

    #Densidad espectral
    plt.figure()
    plt.plot(lista_frec, T_sigma)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Sigma (T)')
    plt.show()

    file = open("prueba_ej4.csv","w")
    for i,j,k in zip(lista_frec,T,T_sigma):
        file.write("{},{},{}\n".format(i,j,k))
    file.close()
