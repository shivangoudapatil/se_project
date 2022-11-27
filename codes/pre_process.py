import os
from comment_strip import comment_strip
from remove_variables import remove_variables
from definitions import ROOT_DIR

#if its not c file we will not consider it
from validateC import validateProgramType


def pre_process():

	#creating path for temporary files if program is being run for first time
	if not os.path.exists(os.path.join(ROOT_DIR, 'processed_files')):
		os.makedirs(os.path.join(ROOT_DIR, 'processed_files'))
	if not os.path.exists(os.path.join(ROOT_DIR, 'semi_processed_files')):
		os.makedirs(os.path.join(ROOT_DIR, 'semi_processed_files'))
		
	diri = os.fsencode(os.path.join(ROOT_DIR, 'input_files'))
	diro = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	dirs = os.fsencode(os.path.join(ROOT_DIR, 'semi_processed_files'))
	diri = diri.decode('utf-8')
	diro = diro.decode('utf-8')
	dirs = dirs.decode('utf-8')
	
	#validating and removing comment
	for file in os.listdir(diri):
		with open(os.path.join(diri,file),'r') as f:
			if validateProgramType(file):
				txt = f.read()
				txt = comment_strip(txt)
				with open(os.path.join(dirs,file),'w') as ff:
					ff.write(txt)
					
	#properly formatting / beautifying c code to maintain uniformity
	for file in os.listdir(dirs):
		os.system("clang-format -style=Microsoft -i " + os.path.join(dirs,file))
		
	#for removing new line and tab
	ESCAPE_SEQUENCE = ['\n','\t',' ']
			
	#removing variables in every file in directory
	for file in os.listdir(dirs):
		with open(os.path.join(dirs,file),'r') as f:
			txt = f.read()
			txt = remove_variables(txt)
			new_txt = [i for i in txt if i not in ESCAPE_SEQUENCE]
			out_txt = ''.join(new_txt)
			with open(os.path.join(diro,file),'w') as ff:
				ff.write(out_txt)
     	
