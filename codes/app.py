import os,subprocess
from definitions import ROOT_DIR
from getplag import getplag
from pre_process import pre_process

def check():
	pre_process()
	dirr = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	dirr = dirr.decode('utf-8')
	ot_mat = [["filename1","filename2","plagiarism result %"]]
	for file1 in os.listdir(dirr):
		with open(os.path.join(dirr,file1),'r') as f1:
			t1 = f1.read()
			for file2 in os.listdir(dirr):
				lst = []
				with open(os.path.join(dirr,file2),'r') as f2:
					t2 = f2.read()
					ff1 = file1[0:len(file1)-2]
					ff2 = file2[0:len(file2)-2]
					if ff1>ff2: ff1,ff2 = ff2,ff1
					lst.append(ff1)
					lst.append(ff2)
					lst.append(getplag(t1,t2)*100)
				ot_mat.append(lst)
				
	with open(os.path.join(ROOT_DIR, 'results.csv'),"w") as ff:
		b = [','.join(str(x) for x in ele) for ele in ot_mat]
		st = '\n'.join(b)
		ff.write(st)
	subprocess.call(('xdg-open',os.path.join(ROOT_DIR, 'results.csv')))
check()
