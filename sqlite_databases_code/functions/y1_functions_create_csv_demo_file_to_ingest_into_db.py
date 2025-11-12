'''
    create the functions.csv csv file to be ingested into the DB for testing
'''
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open('./init/functions.csv','w')
    ligne_out='name,environment_name,description,called_function,input_variables,output_variables,comment'
    file.write(ligne_out)
    file.write('\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'description'+str(i)+','+'called_function'+str(i)+','+'input_variables'+str(i)+','+'output_variables'+str(i)+','+'comment'+str(i)
        file.write(ligne_out)
        file.write('\n')
    file.close()
 
if __name__=='__main__':
    create_csv_demos_data()
    print(green('DONE functions.csv for demos data was created',bold=True))
    