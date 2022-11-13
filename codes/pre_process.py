import os
from comment_strip import comment_strip
from remove_variables import remove_variables
from definitions import ROOT_DIR
from validateC import validateProgramType
def pre_process():
	diri = os.fsencode(os.path.join(ROOT_DIR, 'input_files'))
	diro = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	dirs = os.fsencode(os.path.join(ROOT_DIR, 'semi_processed_files'))
	diri = diri.decode('utf-8')
	diro = diro.decode('utf-8')
	dirs = dirs.decode('utf-8')
	for file in os.listdir(diri):
		with open(os.path.join(diri,file),'r') as f:
			if validateProgramType(file):
				txt = f.read()
				txt = comment_strip(txt)
				with open(os.path.join(dirs,file),'w') as ff:
					ff.write(txt)
	for file in os.listdir(dirs):
		os.system("clang-format -style=Microsoft -i " + os.path.join(dirs,file))
			
	for file in os.listdir(dirs):
		with open(os.path.join(dirs,file),'r') as f:
			txt = f.read()
			txt = remove_variables(txt)
			with open(os.path.join(diro,file),'w') as ff:
				ff.write(txt)
     	
