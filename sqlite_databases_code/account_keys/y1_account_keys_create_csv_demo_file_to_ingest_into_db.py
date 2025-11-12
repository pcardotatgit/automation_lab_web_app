'''
    create the account_keys.csv csv file to be ingested into the DB for testing
'''
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open('./init/account_keys.csv','w')
    ligne_out='name,type,username,password,key,comment'
    file.write(ligne_out)
    file.write('\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'type'+str(i)+','+'username'+str(i)+','+'password'+str(i)+','+'key'+str(i)+','+'comment'+str(i)
        file.write(ligne_out)
        file.write('\n')
    file.close()
 
if __name__=='__main__':
    create_csv_demos_data()
    print(green('DONE account_keys.csv for demos data was created',bold=True))
    