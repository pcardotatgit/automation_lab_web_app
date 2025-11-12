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
    with sqlite3.connect('variables.db') as conn:
        c=conn.cursor()
        try:
            print("--- table : variables creation")
            sql_create=f"CREATE TABLE IF NOT EXISTS variables (`index` int PRIMARY KEY,name text ,environment_name text ,value text ,description text ,comment text ,used_by text)"
            c.execute(sql_create)
            print(green("--- OK variables table created",bold=True))
        except:
            sys.exit(red("couldn't create variables table",bold=True))
    return()    
    
def feed_database():
    database = os.getcwd()+'/variables.db'
    database=database.replace("\\","/")
    print('database is :',database)
    lines=[]    
    file='./init/variables.csv' 
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        indexA=0
        print()
        print(' variables table =>')
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
                sql_add="INSERT OR IGNORE into variables (`index`,name,environment_name,value,description,comment,used_by) VALUES (?,?,?,?,?,?,?)"
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
    conn=create_connection('variables.db') # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print('- Deleting table : variables =>')
        sql_request="drop table : variables"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleting table : variables')
        create_db_and_table()
        print(green('OK variables.db created',bold=True))
        print(yellow('Now ingest data into DB',bold=True))
        feed_database()
        print('-- OK data ingested')
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+'/variables.db'
        database=database.replace("\\","/")
        print('database is :',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(' Do you want to create the variables table ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ok let\'s Create table : variables')
        create_db_and_table()
        print(green('-- Ok Done - variables table succesfuly created ',bold=True))
        rep=input(' Do you want to ingest demo data from ./init/variables.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : variables')
            feed_database()
            print(green('-- OK  Demo data succesfuly ingested into table : variables',bold=True))
    except IOError:
        print(red("- NOK the database DO NOT exists... let's create it",bold=True))
        print('Create variables.db and table : variables')
        create_db_and_table()
        print('-- OK  Database and table created')
        print()
        rep=input(' Ingest demo data from ./init/variables.csv ( Y/N ) ? : ')
        if rep!='N':
            print('-- Ingest demo data into table : variables')
            feed_database()
            print('-- OK  Demo data ingested into table : variables')
        
if __name__ == "__main__":
    create_database_if_not_exits()
            print('ALL DONE')
        