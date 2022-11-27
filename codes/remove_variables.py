#regular expession
import re 

def remove_variables(txt):
	
	#all variables have to follow these data types
	DTS = ["int","float","long","long long","char","double","void","long double"]
	vars = []
    
	#string searching and storing all strings in vars
	for dt in DTS:
		res = [i+len(dt)+1 for i in range(len(txt)) if txt.startswith(dt, i)]
		# print(res)
		for pos in res:
			np = pos
			while np<len(txt) and True:
				if np < len(txt) and txt[np]=='*': np = np+1
				i = np
				while i<len(txt) and txt[i].isalpha(): i = i+1
				if np!=i: vars.append(txt[np:i])
				while i<len(txt) and txt[i]!=',' and txt[i]!=';': i = i+1;
				if i<len(txt) and txt[i]==';': break;
				np = i+2
				
	#removing those variables			
	vars = [item for item in vars if item not in DTS]
	for var in vars:
		txt = re.sub(r'\b%s\b'%var,'',txt)
	return txt
