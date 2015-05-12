#!/usr/bin/python
# -*- coding: utf-8 -*-
# Aarón Ramírez De la Cruz 
# Ángel Callejas 
# Abril, 2015
# Jakatón. IIMAS, UNAM.

import re, sys 
reload(sys)
sys.setdefaultencoding('utf-8')

def removeHashtag(text):
    tokens= text.split(" ")
    
    new_line= []
    for token in tokens: 
        aux= re.sub(r'^#+\w* *', "", str(token))
        if len(aux) > 0: 
            new_line.append( aux )
  
    return " ".join(new_line)

# Comillas raras, guiones largos 
def replaceRareChars(sentence):
    sentence= re.sub(r'(&amp;)', "&", sentence)
    sentence= re.sub(r'”', '"', sentence)
    sentence= re.sub(r'—', '-', sentence)
    return re.sub(u"(\u2018|\u2019)", "'", sentence)

# Elimina enlaces; todos inician con 'http' o 'https' 
def removeLink(text):        return  re.sub(r'.?https*\:.*', "", text) 

def removeMention(sentence): return re.sub(r'(@\w+ *)', "", sentence) 

def removeRTmark(sentence):  return re.sub(r'([r|R][t|T] :)', "", sentence)

def cleanSentence(sentence):
    reemplazo = {'<' : '&lt;', '&' : '&amp;',
                    'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
                    'Á':'a', 'É':'e', 'Í':'i', 'Ó':'O', 'Ú':'u',
                    'ñ':'n', '\n':''}
    regex = re.compile("(%s)" % "|".join(map(re.escape,reemplazo.keys())))
    # r es el origen
    sentence = regex.sub(lambda x: str(reemplazo[x.string[x.start()
                                :x.end()]]), sentence.encode('UTF-8','strict'))
  
    sentence= removeLink(sentence)
    sentence= replaceRareChars(sentence)
    sentence= removeMention(sentence)
    sentence= removeRTmark(sentence)
  
    return sentence 

