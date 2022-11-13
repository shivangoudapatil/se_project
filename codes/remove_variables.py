import re
def remove_variables(txt):
	dts = ["int","float","long","long long","char","double","void","long double"]
	vars = []
	for dt in dts:
		res = [i+len(dt)+1 for i in range(len(txt)) if txt.startswith(dt, i)]
		# print(res)
		for pos in res:
			np = pos
			while True:
				if txt[np]=='*': np = np+1
				i = np
				while txt[i].isalpha(): i = i+1
				vars.append(txt[np:i])
				while txt[i]!=',' and txt[i]!=';': i = i+1;
				if txt[i]==';': break;
				np = i+1
	for var in vars:
		txt = re.sub(r'\b%s\b'%var,'',txt)
	return txt

# with open("D:\study\se_pro\input_files\src1.c",'r') as f: 
# 	txt = f.read();
# 	return rem_var(txt)
# 	# print(txt)
