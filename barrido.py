# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:12:20 2020

@author: Publico
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from lockin import SR830


def barrido(lock, frecini, frecfin, pasos, config):

    freqvec = np.linspace(frecini, frecfin, pasos)

    rvector = []
    thetavector = []

    t_int = lock.getIntegrationTime()

    for f in freqvec:
        lock.setFreqReferencia(f)
        time.sleep(0.1)
        r, theta = lock.getMedicion('RT')
        rvector.append(r)
        thetavector.append(theta)
        time.sleep(100*t_int)
        print(f)

    return freqvec, rvector, thetavector

if __name__ == '__main__':

    config = {
          'lockin_addr': 'GPIB0::11::INSTR',
          'medicion_modo' : 'XY', 
          'display_modo' : 'XY', 
          'sens' : 24,
          'slope' : 3, 
          't_int' : 7,
          'ref_intern' : True,
          'ref_freq' : 5000,
          'ref_v' : 0.5,
          }
    
    lock_in = SR830(config)
    time.sleep(2)
    #frecini = 49.75e3
    #frecfin = 50.75e3
    
    frecini = 20e3
    frecfin = 40e3
    
    pasos = 50

    F, R, Theta = barrido(lock_in, frecini, frecfin, pasos, config)

    plt.figure()
    plt.plot(F, R)
    plt.xlabel('Frecuencia (kHz)')
    plt.ylabel('R')

    plt.figure()
    plt.plot(F, Theta)
    plt.xlabel('Frecuencia (kHz)')
    plt.ylabel('Theta')

    





