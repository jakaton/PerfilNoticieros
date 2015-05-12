#!/usr/bin/python
# -*- coding: utf-8 -*-
# Aarón Ramírez De la Cruz 
# Ángel Callejas 
# Abril, 2015
# Jakatón. IIMAS, UNAM.

"""
  A partir de la información en los tweets de un usuario, definir qué emociones persisten 
  en las noticias publicadas: joy, anger, fear, sadness, surprise, and disgust
"""
from __future__ import division
import datos_grafica 
import os, sys, codecs, re 
reload(sys)
sys.setdefaultencoding('utf-8')
cur_dir= os.getcwd() 
import TagText

import LimpiaTweets

emotions= {} 

def loadEmotions():
    """
    Diccionario de emociones. Disponible en http://www.cic.ipn.mx/~sidorov/
    Carga en un diccionario el contenido en una estructura diccionario 
    """
    txt_emotions= codecs.open("emociones_short.txt", encoding= "utf8", mode= "r").readlines()
  
    for emotion in txt_emotions: 
        emotion= re.sub(r'\n', "", emotion) 
        word, prob, emotion= emotion.split('\t') 
        emotions.update({ word: (prob, emotion) })

def main():
    # Ocurrencias de las emociones
    occ_basic_emotions= {
      "Alegría":   0,
      "Enojo":     0,
      "Miedo":     0,
      "Tristeza":  0,
      "Sorpresa":  0,
      "Repulsión": 0
    }
    # Probabilidad acumulada las emociones
    prob_basic_emotions= {
      "Alegría":   0,
      "Enojo":     0,
      "Miedo":     0,
      "Tristeza":  0,
      "Sorpresa":  0,
      "Repulsión": 0
    }
    # Resultados de depuración   
    almacen_palabra_emociones = {
      "Alegría":   [],
      "Enojo":     [],
      "Miedo":     [],
      "Tristeza":  [],
      "Sorpresa":  [],
      "Repulsión": []
    }
  
#    try: 
    tweets_file= codecs.open(sys.argv[1], encoding= "utf-8", mode= "r").readlines()
#    except: 
#        print "USE: python", sys.argv[0], "archivo_tweets.txt"
#        exit() 
  
    for tweet in tweets_file : 
        tweet= LimpiaTweets.cleanSentence(tweet)
        tweet= re.sub(r"[\d\/]+", "", tweet, re.U)
        tweet= re.sub(r"[^\w]", " ",  tweet, re.U)
        tweet= re.sub(r" {1,}", " ",  tweet, re.U)
        tweet= re.sub(r'^ {1}', "", tweet)
        tagged= TagText.tag(tweet)
  
        for word, tag, lemma in tagged: 
            if tag == 'ADJ' or tag == 'NP' or tag == 'NC': 
                try:
                    prob, emotion=  emotions[lemma.lower()] 
                    if lemma not in almacen_palabra_emociones[emotion]: 
                        almacen_palabra_emociones[emotion].append(lemma.lower())
                    prob_basic_emotions[emotion]= prob_basic_emotions[emotion] +  float(prob)
                    occ_basic_emotions [emotion]= occ_basic_emotions [emotion] + 1
                except:
                    pass 
  
    datos_grafica.showResults(occ_basic_emotions, prob_basic_emotions, sys.argv[1])

if __name__ == '__main__':
    loadEmotions() 
    main()

    