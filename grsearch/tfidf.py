#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
from grsearch.gsearch import *


def nbr_word(text, is_file):
	compt=0
	
	if is_file:
		with open(text, 'rb') as f:
			filestream=True
			
			while filestream:
				line=f.readline()
				
				if len(line) == 0:
					break
				
				line=str(line)[2:-1] #convert bytes -> str
				
				for w in line.split(' '):
					compt+=1
					
	else:
		for w in text.split(' '):
			compt+=1

	return compt
	

def calcul_tfidf(keyword, corpus, is_file=False):
	global_result,result_tfidf=[],[]
	nbr_occur=[0]*len(keyword)
	nbr_text=len(corpus)
	
	#Search keyword in all texts.
	for text in corpus:
		if is_file:
			result=search_infile(text, keyword, exactly=True)
		else:
			result=search(text, keyword, exactly=True)
		
		global_result.append([result, nbr_word(text, is_file)])
	
	#Calcul number of occurences in all texts.
	for i,x in enumerate(global_result):
		indice, d=0,0
		
		for y in x[0]:
			if x[0][indice][1] > 0:
				nbr_occur[indice]+=1
				
			indice+=1
	
	for i,rtext in enumerate(global_result):
		buff_tfidf=[]
		
		#Cacul tfidf for each keywords.
		for j,rkeyword in enumerate(rtext[0]):
			
			#Prevent 0 division.
			if nbr_occur[j] == 0:
				tf=0.0
				idf=0.0
			else:
				tf=rkeyword[1]/rtext[1]
				idf=math.log10(nbr_text/nbr_occur[j])
				
			buff_tfidf.append([rkeyword[0], tf*idf])
			
		result_tfidf.append(list(buff_tfidf))
	
	return result_tfidf	
	
