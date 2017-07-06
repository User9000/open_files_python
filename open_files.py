

import csv
import codecs
import tempfile


temp_file = tempfile.NamedTemporaryFile(mode='w',delete=False)
data_file = "data.csv"

with codecs.open(data_file,'rb',encoding='utf8') as csvfile,temp_file:
	 reader = csv.DictReader(csvfile)
	 fieldnames = ['id','name','email','amount','sent']
	 writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
	 print(temp_file.name)
   	 
	 writer.writeheader()
	 for row in reader:
		 writer.writerow({ 'id':row['id'], 'name':row['name'], 'email':row['email'], 'amount':'1323','sent':'yes'})
		 print(row)