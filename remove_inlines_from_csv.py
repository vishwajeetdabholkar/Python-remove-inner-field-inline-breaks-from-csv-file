#removing inner-field inline breaks from csv file
#Author: Vishwajeet Dabholkar
import csv
#open a outputfile 
f = open("test_out.csv","a")
with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stripped = [col.replace('\n',' ') for col in row]
        print(','.join(stripped), file=f)
        
f.close() 
