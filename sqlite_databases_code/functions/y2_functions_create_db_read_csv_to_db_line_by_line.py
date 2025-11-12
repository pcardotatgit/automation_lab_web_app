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
    with sqlite3.connect('functions.db') as conn:
        c=conn.cursor()
        try:
            print("--- table : functions creation")
            sql_create=f"CREATE TABLE IF NOT EXISTS functions (`index` int PRIMARY KEY,name text ,environment_name text ,description text ,called_function text ,input_variables text ,output_variables text ,comment text)"
            c.execute(sql_create)
            print(green("--- OK functions table created",bold=True))
        except:
            sys.exit(red("couldn't create functions table",bold=True))
    return()    
    
def feed_database():
    database = os.getcwd()+'/functions.db'
    database=database.replace("\\","/")
    print('database is :',database)
    lines=[]    
    file='./init/functions.csv' 
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        indexA=0
        print()
        print(' functions table =>')
        print()
        for row in lines:
            #print ('print the all row  : ' + row)
            print(row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5] ,row[6])
            #print(row)
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let's go to every lines one by one and let's extract url, targeted brand
                sqlite_data=(indexA,row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5] ,row[6])
                sql_add="INSERT OR IGNORE into functions (`index`,name,environment_name,description,called_function,input_variables,output_variables,comment) VALUES (?,?,?,?,?,?,?,?)"
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
    conn=create_connection('functions.db') # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print('- Deleting table : functions =>')
        sql_request="drop table : functions"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleting table : functions')
        create_db_and_table()
        print(green('OK functions.db created',bold=True))
        print(yellow('Now ingest data into DB',bold=True))
        feed_database()
        print('-- OK data ingested')
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+'/functions.db'
        database=database.replace("\\","/")
        print('database is :',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(' Do you want to create the functions table ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ok let\'s Create table : functions')
        create_db_and_table()
        print(green('-- Ok Done - functions table succesfuly created ',bold=True))
        rep=input(' Do you want to ingest demo data from ./init/functions.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : functions')
            feed_database()
            print(green('-- OK  Demo data succesfuly ingested into table : functions',bold=True))
    except IOError:
        print(red("- NOK the database DO NOT exists... let's create it",bold=True))
        print('Create functions.db and table : functions')
        create_db_and_table()
        print('-- OK  Database and table created')
        print()
        rep=input(' Ingest demo data from ./init/functions.csv ( Y/N ) ? : ')
        if rep!='N':
            print('-- Ingest demo data into table : functions')
            feed_database()
            print('-- OK  Demo data ingested into table : functions')
        
if __name__ == "__main__":
    create_database_if_not_exits()
            print('ALL DONE')
        