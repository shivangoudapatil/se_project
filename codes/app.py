#this is for opening files and imitate running various commands on terminal
import os,subprocess

#this makes our code work in any environment / folder
from definitions import ROOT_DIR 

#this will take two strings as input and output the plagiarism percentage
from getplag import getplag  

#this will remove comments and variables then convert c files to proper format
from pre_process import pre_process 

def check():
	
	##this will remove comments and variables then convert c files to proper format
	pre_process() 
	
	#directory to store processed files
	dirr = os.fsencode(os.path.join(ROOT_DIR, 'processed_files'))
	dirr = dirr.decode('utf-8')
	
	#heading of our csv file
	ot_mat = [["filename1","filename2","plagiarism result %"]]
	
	#checking each file with every other file for plagiarism
	for file1 in os.listdir(dirr):
		with open(os.path.join(dirr,file1),'r') as f1:
			t1 = f1.read()
			for file2 in os.listdir(dirr):
				lst = []
				with open(os.path.join(dirr,file2),'r') as f2:
					t2 = f2.read()
					ff1 = file1[0:len(file1)-2]
					ff2 = file2[0:len(file2)-2]
					
					#smaller file comes in first column in the csv file
					if ff1>ff2: ff1,ff2 = ff2,ff1 
					lst.append(ff1)
					lst.append(ff2)
					lst.append(getplag(t1,t2)*100)
				ot_mat.append(lst)
	
	#writing the 2d matrix os_mat to the csv file in proper format
	with open(os.path.join(ROOT_DIR, 'results.csv'),"w") as ff:
		b = [','.join(str(x) for x in ele) for ele in ot_mat]
		st = '\n'.join(b)
		ff.write(st)
		
	#opening the csv file with default app
	subprocess.call(('xdg-open',os.path.join(ROOT_DIR, 'results.csv')))
check()
