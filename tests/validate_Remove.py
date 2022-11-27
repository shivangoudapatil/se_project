import unittest
from Remove_Variables1 import remove_variables

tc = unittest.TestCase()

tc.assertEqual(remove_variables("int x,y,z;"),"int ,,;")
tc.assertEqual(remove_variables("for(int i=0;i<10;i++)"),"for(int =0;<10;++)")
tc.assertEqual(remove_variables("int x=5; float y=2; char c = 'a' "),"int =5; float =2; char  = 'a' ")

# Invalid input should end with semicolon but we will still use line to check for plagarism
tc.assertEqual(remove_variables("int x,y"),"int ,") 
tc.assertEqual(remove_variables("int ml = hello()"),"int  = hello()")
tc.assertEqual(remove_variables("hello"),"hello")
'''
import re
def remove_variables(txt):
	dts = ["int","float","long","long long","char","double","void","long double"]
	vars = []
    
	for dt in dts:
		res = [i+len(dt)+1 for i in range(len(txt)) if txt.startswith(dt, i)]
		# print(res)
		for pos in res:
			np = pos
			while np<len(txt) and True:
				if np < len(txt) and txt[np]=='*': np = np+1
				i = np
				while i<len(txt) and txt[i].isalpha(): i = i+1
				vars.append(txt[np:i])
				while i<len(txt) and txt[i]!=',' and txt[i]!=';': i = i+1;
				if i<len(txt) and txt[i]==';': break;
				np = i+1
	for var in vars:
		txt = re.sub(r'\b%s\b'%var,'',txt)
	return txt
'''