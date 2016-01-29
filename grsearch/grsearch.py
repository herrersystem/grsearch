#!/usr/bin/env python
# -*- coding:utf-8 -*-


def search(text, keyword, exactly=False, case_sensitive=False, limit_iteration=False):
	result=None
	
	if exactly:
		result=s_exactly(text, keyword, case_sensitive, limit_iteration)
	else:
		result=s_notexactly(text, keyword, case_sensitive, limit_iteration)
	
	return result
	

def search_infile(filename, keyword, exactly=False, case_sensitive=False, limit_iteration=False):
	result=None
	
	if exactly:
		result=f_exactly(filename, keyword, case_sensitive, limit_iteration)
	else:
		result=f_notexactly(filename, keyword, case_sensitive, limit_iteration)
	
	return result


def clean_text(text):
	'''
	Suppression de la ponctuation.
	'''
	text=text.replace('.', ' ')
	text=text.replace(',', ' ')
	text=text.replace(';', ' ')
	text=text.replace('?', ' ')
	text=text.replace('!', ' ')
	text=text.replace(':', ' ')
	text=text.replace('\'', ' ')
	text=text.replace('(', ' ')
	text=text.replace(')', ' ')
	
	return text

	
'''
Function for search within string chars.
'''

def s_exactly(text, keyword, case_sensitive, limit_iteration):
	playhead=0	
	result=[]
	
	for kw in keyword:
		result.append([kw,0,[]])
	
	if not case_sensitive:
		text=text.lower()
		
		#Formate keyword.
		for i,kw in enumerate(keyword):
			keyword[i]=keyword[i].lower()
	
	text=clean_text(text) #Remove ponctuation.
	
	#Search keyword within the text.		
	for word in text.split(' '):
		for i,kw in enumerate(keyword):
			if limit_iteration and result[i][1] >= limit_iteration:
				continue
				
			if kw == word:
				result[i][1]+=1
				result[i][2].append(playhead)
		
		playhead+=len(word)+1 #add 1 for space.
			
	return result		


def s_notexactly(text, keyword, case_sensitive, limit_iteration):
	playhead=0	
	result=[]
	
	#Create response object (list).
	for kw in keyword:
		result.append([kw,0,[]])
		
	if not case_sensitive:
		text=text.lower()
		
		#Formate keyword.
		for i,kw in enumerate(keyword):
			keyword[i]=keyword[i].lower()

	#Search keyword within the text.		
	for word in text.split(' '):	
		for i,kw in enumerate(keyword):
			if limit_iteration and result[i][1] >= limit_iteration:
				continue
				
			index=word.find(kw)
			if index != -1:
				result[i][1]+=1
				result[i][2].append(playhead+index)
									
		playhead+=len(word)+1 #add 1 for space.
		
	return result


'''
Function for search within file.
'''

def f_exactly(filename, keyword, case_sensitive, limit_iteration):
	result=[]
	playhead=0
	
	for kw in keyword:
		result.append([kw,0,[]])
	
	if not case_sensitive:
		for i,kw in enumerate(keyword):
			keyword[i]=keyword[i].lower()
	
	with open(filename, 'rb') as f:
		filestream=True
		
		while filestream:
			text=f.readline()
			
			if len(text) == 0:
				break
			
			if not case_sensitive:
				text=text.lower()
			
			text=str(text)[2:-1] #Conversion bytes -> str.
			print(text)
			text=clean_text(text) #Remove ponctuation.
			
			#Search keyword within the text.		
			for word in text.split(' '):
				for i,kw in enumerate(keyword):
					if limit_iteration and result[i][1] >= limit_iteration:
						continue
						
					if kw == word:
						result[i][1]+=1
						result[i][2].append(playhead)
				
				playhead+=len(word)+1 #add 1 for space.
			
	return result


def f_notexactly(filename, keyword, case_sensitive, limit_iteration):
	result=[]
	playhead=0
	
	for kw in keyword:
		result.append([kw,0,[]])
	
	if not case_sensitive:
		for i,kw in enumerate(keyword):
			keyword[i]=keyword[i].lower()
	
	with open(filename, 'rb') as f:
		filestream=True
		
		while filestream:
			text=f.readline()
			
			if len(text) == 0:
				break
			
			text=str(text)[2:-1] #Conversion bytes -> str.
			
			if not case_sensitive:
				text=text.lower()
					
			#Search keyword within the text.		
			for word in text.split(' '):	
				for i,kw in enumerate(keyword):
					if limit_iteration and result[i][1] >= limit_iteration:
						continue
						
					index=word.find(kw)
					if index != -1:
						result[i][1]+=1
						result[i][2].append(playhead+index)
											
				playhead+=len(word)+1 #add 1 for space.
			
	return result

