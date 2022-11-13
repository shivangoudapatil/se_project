import os
from definitions import ROOT_DIR
from plagcheck import plagcheck
def check():
	dirr = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	ot_mat = []
	for file1 in os.listdir(dirr.decode('utf-8')):
			for file2 in os.listdir(dirr.decode('utf-8')):
				with open(os.path.join(dirr.decode('utf-8'),file1),'r') as f1:
					t1 = f1.read()
					lst = []
					with open(os.path.join(dirr.decode('utf-8'),file2),'r') as f2:
						t2 = f2.read()
						ff1 = file1[0:len(file1)-2]
						ff2 = file2[0:len(file2)-2]
						if ff1>ff2: ff1,ff2 = ff2,ff1
						lst.append(ff1)
						lst.append(ff2)
						lst.append(plagcheck(t1,t2))
					ot_mat.append(lst)
	print(ot_mat)
check()