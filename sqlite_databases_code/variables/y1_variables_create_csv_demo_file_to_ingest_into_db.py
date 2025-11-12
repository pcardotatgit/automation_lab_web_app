'''
    create the variables.csv csv file to be ingested into the DB for testing
'''
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open('./init/variables.csv','w')
    ligne_out='name,environment_name,value,description,comment,used_by'
    file.write(ligne_out)
    file.write('\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'value'+str(i)+','+'description'+str(i)+','+'comment'+str(i)+','+'used_by'+str(i)
        file.write(ligne_out)
        file.write('\n')
    file.close()
 
if __name__=='__main__':
    create_csv_demos_data()
    print(green('DONE variables.csv for demos data was created',bold=True))
    