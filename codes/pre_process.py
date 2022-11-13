import os
from comment_strip import comment_strip
from remove_variables import remove_variables
from definitions import ROOT_DIR
def main():
	diri = os.fsencode(os.path.join(ROOT_DIR, 'input_files'))
	diro = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	diri = diri.decode('utf-8')
	diro = diro.decode('utf-8')
	for file in os.listdir(diri):
		with open(os.path.join(diri,file),'r') as f:
			txt = f.read()
			txt = comment_strip(txt)
			os.system("clang-format -style=Google -i ")
			txt = remove_variables(txt)
			with open(os.path.join(diro,file),'w') as ff:
				ff.write(txt)
     	
if __name__ == '__main__':
	main()
