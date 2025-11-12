import sys
import csv
from crayons import *
import sqlite3
import os
import json
def create_connection(db_file):
    ''' create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
   
def create_db_and_table():    
    #with sqlite3.connect(':memory:') as conn:
    with sqlite3.connect('api_calls.db') as conn:
        c=conn.cursor()
        try:
            print("--- table : api_calls creation")
            sql_create=f"CREATE TABLE IF NOT EXISTS api_calls (`index` int PRIMARY KEY,name text ,fqdn text ,relative_url text ,documentation text ,method text ,description text ,payload text ,header text ,body text ,query_params text ,custom_variables text ,authentication_profile text ,inputs_variables text ,output_variables text)"
            c.execute(sql_create)
            print(green("--- OK api_calls table created",bold=True))
        except:
            sys.exit(red("couldn't create api_calls table",bold=True))
    return()    
    
def feed_database():
    database = os.getcwd()+'/api_calls.db'
    database=database.replace("\\","/")
    print('database is :',database)
    lines=[]    
    file='./init/api_calls.csv' 
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        indexA=0
        print()
        print(' api_calls table =>')
        print()
        for row in lines:
            #print ('print the all row  : ' + row)
            print(row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5] ,row[6] ,row[7] ,row[8] ,row[9] ,row[10] ,row[11] ,row[12] ,row[13])
            #print(row)
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let's go to every lines one by one and let's extract url, targeted brand
                sqlite_data=(indexA,row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5] ,row[6] ,row[7] ,row[8] ,row[9] ,row[10] ,row[11] ,row[12] ,row[13])
                sql_add="INSERT OR IGNORE into api_calls (`index`,name,fqdn,relative_url,documentation,method,description,payload,header,body,query_params,custom_variables,authentication_profile,inputs_variables,output_variables) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                print()
                print('sql_add :',cyan(sql_add,bold=True))
                print()
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done",bold=True))
                indexA+=1
                            conn.commit()
        print()
        print(' ==> OK')
        print()
        
def reset_tables():
    conn=create_connection('api_calls.db') # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print('- Deleting table : api_calls =>')
        sql_request="drop table : api_calls"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleting table : api_calls')
        create_db_and_table()
        print(green('OK api_calls.db created',bold=True))
        print(yellow('Now ingest data into DB',bold=True))
        feed_database()
        print('-- OK data ingested')
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+'/api_calls.db'
        database=database.replace("\\","/")
        print('database is :',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(' Do you want to create the api_calls table ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ok let\'s Create table : api_calls')
        create_db_and_table()
        print(green('-- Ok Done - api_calls table succesfuly created ',bold=True))
        rep=input(' Do you want to ingest demo data from ./init/api_calls.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : api_calls')
            feed_database()
            print(green('-- OK  Demo data succesfuly ingested into table : api_calls',bold=True))
    except IOError:
        print(red("- NOK the database DO NOT exists... let's create it",bold=True))
        print('Create api_calls.db and table : api_calls')
        create_db_and_table()
        print('-- OK  Database and table created')
        print()
        rep=input(' Ingest demo data from ./init/api_calls.csv ( Y/N ) ? : ')
        if rep!='N':
            print('-- Ingest demo data into table : api_calls')
            feed_database()
            print('-- OK  Demo data ingested into table : api_calls')
        
if __name__ == "__main__":
    create_database_if_not_exits()
            print('ALL DONE')
        