#!/usr/bin/python
# -*- coding: utf-8 -*-
# Aarón Ramírez De la Cruz 
# Ángel Callejas 
# Abril, 2015
# Jakatón. IIMAS, UNAM.

import sys, os, re, codecs 
reload(sys)
sys.setdefaultencoding('utf-8')

""" Etiquetado POS con TreeTagger """

sys.path.append(os.getcwd())
this_dir= os.getcwd()
os.chdir( "TreeTagger/" )

sys.path.append( "TreeTagger" )
# Necesario para el módulo treetaggerwrapper.py que es el 
# enlace entre TreeTagger y Python 
# Carpeta raíz proyecto completo TreeTagger 
TREETAGGER = os.getcwd() 
os.environ['TAGDIR'] = TREETAGGER 

# Para utilizar módulo treetaggerwrapper 
os.path.abspath(os.curdir) 
sys.path.append(os.curdir) 
sys.path.append( (os.path.abspath(os.curdir))+"/TreeTagger/ttpw" ) 
os.chdir( os.getcwd()+ "/ttpw/"  )

import treetaggerwrapper 


# Etiquetado POS de 'str_sentence' 
# Devuelve lista de tuplas 
def tag(str_sentence, nltk_format= False):
  
    tagger = treetaggerwrapper.TreeTagger(TAGLANG= 'es')  
    ttager = tagger.TagText(str_sentence , encoding= "utf-8")
    
    # Lista de tuplas en formato de NLTK: 
    # [(word, POS_TAG), (word, POS_TAG)]  
    if nltk_format: 
        lst_nltk_format= [] 
        nltk_token= () 
  
        for item in ttager : 
            aux= re.split(r'\t', item) 
            nltk_token = aux[0], aux[1]  
            lst_nltk_format.append(nltk_token) 
        return lst_nltk_format 
  
    else: 
        # Lista de tuplas en formato de TreeTagger: 
        # [(word, POS_TAG, lemma), (word, POS_TAG, lemma)]  
        lst_ttager_format= [] 
        ttager_token= () 
  
        for item in ttager : 
            aux= re.split(r'\t', item) 
            try:
                ttager_token = aux[0], aux[1], aux[2] 
                lst_ttager_format.append(ttager_token) 
            except: pass 
        return lst_ttager_format 

# Devuelve a carpeta original 
os.chdir(this_dir)

