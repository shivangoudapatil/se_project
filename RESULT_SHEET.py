import pandas as pd
import sys
import csv
import os
def final():
	threshold=sys.argv[1]
	df=pd.read_csv('results.csv')
	df=df.reset_index()
	list=[]
	dic={}
	for i,row in df.iterrows():
		if row["filename1"]!=row["filename2"] and row["plagiarism result %"]>=float(threshold):
			if row["filename1"] not in dic:
				list.append(row["filename1"])
				dic.update({row["filename1"]:1})
			if row["filename2"] not in dic:
				list.append(row["filename2"])
				dic.update({row["filename2"]:1})
	with open('Final_Sheet.csv', 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(list)