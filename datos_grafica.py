#!/usr/bin/python
# -*- coding: utf-8 -*-
# Aarón Ramírez De la Cruz 
# Ángel Callejas 
# Abril, 2015
# Jakatón. IIMAS, UNAM.

import math, sys 

# def grafica(variable,titulo):
#     # Títulos
#     plt.xlabel("Promedio de Probabilidades")
#     plt.ylabel("Porcentaje")
#     plt.title(titulo)
  
#     color_list = ['#eeefff','#eeefff','#eeefff','#eeefff','#eeefff','#eeefff']
#     plt.bar(range(len(variable)),variable.values(),color=color_list )
#     plt.xticks(range(len(variable)), variable.keys())
  
#     plt.show()

def showResults(dic_occur, dic_freq, data_name= None):
    if data_name: 
        print "  Archivo: ", data_name, "\n"
  
    total_avg= 0
  
    for emotion in dic_occur.keys():
        occu= dic_occur[emotion] 
        if occu == 0: 
            print "   ", emotion, "=>  ", "0"
        else:
            print "   ", emotion, "=>  ", dic_freq[emotion] / occu
            total_avg+= dic_freq[emotion] / occu
  
    print "---"*10, "\n\t\tTotal", total_avg, "\n"

if __name__ == '__main__':

  
    # Opciones de depuración 
    aris_oc= {'Enojo': 64, 'Repulsión': 0, 'Miedo': 0, 'Sorpresa': 96, 'Tristeza': 160, 'Alegría': 0}
    aris_pr= {'Enojo': 56.46400000000004, 'Repulsión': 0, 'Miedo': 0, 'Sorpresa': 28.607999999999926, 'Tristeza': 110.99199999999972, 'Alegría': 0}
    aris_fin= {'Enojo': (56.46400000000004/64), 'Repulsion': 0, 'Miedo': 0, 'Sorpresa': 28.607999999999926/96, 'Tristeza': 110.99199999999972/160, 'Alegria': 0}
    showResults(aris_oc, aris_pr, "@AristeguiOnline")
  
    exel_oc= {'Enojo': 16, 'Repulsión': 0, 'Miedo': 32, 'Sorpresa': 16, 'Tristeza': 80, 'Alegría': 0}
    exel_pr= {'Enojo': 9.007999999999997, 'Repulsión': 0, 'Miedo': 24.48000000000001, 'Sorpresa': 14.384000000000007, 'Tristeza': 60.62400000000005, 'Alegría': 0}
    exel_fin= {'Enojo': (9.007999999999997/16), 'Repulsion': 0, 'Miedo': 24.48000000000001/32, 'Sorpresa': 14.384000000000007/16, 'Tristeza': 60.62400000000005/80, 'Alegria': 0}
    showResults(exel_oc, exel_pr, "@Excelsior")
     
    univ_oc= {'Enojo': 0, 'Repulsión': 0, 'Miedo': 64, 'Sorpresa': 48, 'Tristeza': 80, 'Alegría': 0}
    univ_pr= {'Enojo': 0, 'Repulsión': 0, 'Miedo': 48.86400000000002, 'Sorpresa': 33.008000000000024, 'Tristeza': 38.25600000000002, 'Alegría': 0}
    uniM_fin= {'Enojo': 0, 'Repulsion': 0, 'Miedo': 48.86400000000002/64, 'Sorpresa': 33.008000000000024/48, 'Tristeza': 38.25600000000002/80, 'Alegria': 0}
    showResults(univ_oc, univ_pr, "@ElUniversal")
  
    graf_oc= {'Enojo': 96, 'Repulsión': 0, 'Miedo': 96, 'Sorpresa': 32, 'Tristeza': 112, 'Alegría': 0}
    graf_pr= {'Enojo': 54.11199999999996, 'Repulsión': 0, 'Miedo': 76.06400000000002, 'Sorpresa': 23.903999999999996, 'Tristeza': 71.21600000000002, 'Alegría': 0}
    graf_fin= {'Enojo': (54.11199999999996/96), 'Repulsion': 0, 'Miedo': 76.06400000000002/96, 'Sorpresa': 23.903999999999996/32, 'Tristeza': 71.21600000000002/112, 'Alegria': 0}
    showResults(graf_oc, graf_pr, "@ElGraficoMX")
   
    publi_oc= {'Enojo': 64, 'Repulsion': 0, 'Miedo': 16, 'Sorpresa': 80, 'Tristeza': 160, 'Alegria': 0}
    publi_pr= {'Enojo': 38.27199999999999, 'Repulsión': 0, 'Miedo': 12.240000000000002, 'Sorpresa': 51.50400000000004, 'Tristeza': 101.07199999999985, 'Alegría': 0}
    publi_fin= {'Enojo': (38.27199999999999/64), 'Repulsion': 0, 'Miedo': 12.240000000000002/16, 'Sorpresa': 51.50400000000004/80, 'Tristeza': 101.07199999999985/160, 'Alegria': 0}
    showResults(publi_oc, publi_pr, "@PublimetroMX")
  
    uniM_oc= {'Enojo': 48, 'Repulsion': 0, 'Miedo': 32, 'Sorpresa': 32, 'Tristeza': 128, 'Alegria': 0}
    uniM_pr= {'Enojo': 43.13600000000002, 'Repulsión': 0, 'Miedo': 22.27200000000001, 'Sorpresa': 22.863999999999987, 'Tristeza': 60.48000000000011, 'Alegría': 0}
    uniM_fin= {'Enojo': (43.13600000000002/48), 'Repulsion': 0, 'Miedo': 22.27200000000001/32, 'Sorpresa': 22.863999999999987/32, 'Tristeza': 60.48000000000011/128, 'Alegria': 0}
    showResults(uniM_oc, uniM_pr, "@Univ_Metropoli")
   
    # Eliminar exit() para graficar datos  
    exit () 
    #grafica(aris_fin,'@AristeguiOnline')
    #grafica(exel_fin,'@Excelsior')
    #grafica(uniM_fin,'@ElUniversal')
    #grafica(graf_fin,'@ElGraficoMX')
    #grafica(publi_fin,'@PublimetroMX')
    #grafica(uniM_fin,'@Univ_Metropoli')


