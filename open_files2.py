
import csv

data_file ='data.csv'
with open(data_file,'rb') as csvfile:
	  #data = csvfile.readlines()
	 #print(type(data.decode('utf-8', newline='')))
	  reader = csv.DictReader(csvfile)
	  for row in reader:
		  print(row)