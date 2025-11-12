'''
    create the workflows.csv csv file to be ingested into the DB for testing
'''
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open('./init/workflows.csv','w')
    ligne_out='workflow_name,step,step_name,input,output,comment'
    file.write(ligne_out)
    file.write('\n')
    for i in range (0,10):
        ligne_out='workflow_name'+str(i)+','+'step'+str(i)+','+'step_name'+str(i)+','+'input'+str(i)+','+'output'+str(i)+','+'comment'+str(i)
        file.write(ligne_out)
        file.write('\n')
    file.close()
 
if __name__=='__main__':
    create_csv_demos_data()
    print(green('DONE workflows.csv for demos data was created',bold=True))
    