'''
    create the api_calls.csv csv file to be ingested into the DB for testing
'''
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open('./init/api_calls.csv','w')
    ligne_out='name,fqdn,relative_url,documentation,method,description,payload,header,body,query_params,custom_variables,authentication_profile,inputs_variables,output_variables'
    file.write(ligne_out)
    file.write('\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'fqdn'+str(i)+','+'relative_url'+str(i)+','+'documentation'+str(i)+','+'method'+str(i)+','+'description'+str(i)+','+'payload'+str(i)+','+'header'+str(i)+','+'body'+str(i)+','+'query_params'+str(i)+','+'custom_variables'+str(i)+','+'authentication_profile'+str(i)+','+'inputs_variables'+str(i)+','+'output_variables'+str(i)
        file.write(ligne_out)
        file.write('\n')
    file.close()
 
if __name__=='__main__':
    create_csv_demos_data()
    print(green('DONE api_calls.csv for demos data was created',bold=True))
    