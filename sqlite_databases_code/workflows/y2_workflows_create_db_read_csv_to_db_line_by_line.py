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
    with sqlite3.connect('workflows.db') as conn:
        c=conn.cursor()
        try:
            print("--- table : workflows creation")
            sql_create=f"CREATE TABLE IF NOT EXISTS workflows (`index` int PRIMARY KEY,workflow_name text ,step text ,step_name text ,input text ,output text ,comment text)"
            c.execute(sql_create)
            print(green("--- OK workflows table created",bold=True))
        except:
            sys.exit(red("couldn't create workflows table",bold=True))
    return()    
    
def feed_database():
    database = os.getcwd()+'/workflows.db'
    database=database.replace("\\","/")
    print('database is :',database)
    lines=[]    
    file='./init/workflows.csv' 
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        indexA=0
        print()
        print(' workflows table =>')
        print()
        for row in lines:
            #print ('print the all row  : ' + row)
            print(row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5])
            #print(row)
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let's go to every lines one by one and let's extract url, targeted brand
                sqlite_data=(indexA,row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5])
                sql_add="INSERT OR IGNORE into workflows (`index`,workflow_name,step,step_name,input,output,comment) VALUES (?,?,?,?,?,?,?)"
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
    conn=create_connection('workflows.db') # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print('- Deleting table : workflows =>')
        sql_request="drop table : workflows"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleting table : workflows')
        create_db_and_table()
        print(green('OK workflows.db created',bold=True))
        print(yellow('Now ingest data into DB',bold=True))
        feed_database()
        print('-- OK data ingested')
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+'/workflows.db'
        database=database.replace("\\","/")
        print('database is :',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(' Do you want to create the workflows table ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ok let\'s Create table : workflows')
        create_db_and_table()
        print(green('-- Ok Done - workflows table succesfuly created ',bold=True))
        rep=input(' Do you want to ingest demo data from ./init/workflows.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : workflows')
            feed_database()
            print(green('-- OK  Demo data succesfuly ingested into table : workflows',bold=True))
    except IOError:
        print(red("- NOK the database DO NOT exists... let's create it",bold=True))
        print('Create workflows.db and table : workflows')
        create_db_and_table()
        print('-- OK  Database and table created')
        print()
        rep=input(' Ingest demo data from ./init/workflows.csv ( Y/N ) ? : ')
        if rep!='N':
            print('-- Ingest demo data into table : workflows')
            feed_database()
            print('-- OK  Demo data ingested into table : workflows')
        
if __name__ == "__main__":
    create_database_if_not_exits()
            print('ALL DONE')
        