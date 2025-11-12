'''
    this resource manages interaction with the sqllite database
'''
import sys
import sqlite3
from crayons import *
from datetime import datetime, timedelta
import time
import json
def date_time():
    '''
        get current date time in yy-mm-dd-H:M:S:fZ format
    '''
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    current_date=current_time.split('T')[0]
    return(current_time,current_date)
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
    
def read_db(database,table,where_clause):
    liste=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_request = f"SELECT * from {table} {where_clause}"
        print()
        print(sql_request)
        print()
        try:
            cursor.execute(sql_request)
            for resultat in cursor:
                #print(resultat)
                liste.append(resultat)
        except:
            sys.exit("couldn't read database")
    return(liste) 
    
def update_db_generic(database,table,where_clause,data):
    liste=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_request = f"UPDATE {table} SET "
        for key,value in data.items():
            print(cyan(key))
            print(red(value))
            sql_request =sql_request + key +" = '"+value+"',"
        sql_request=sql_request[:-1]
        if where_clause!='':
            sql_request=sql_request+' where '+where_clause
        print()
        print(sql_request)
        print()
        try:
            cursor.execute(sql_request)
            print("Execute UPDATE IN DB")
        except:
            sys.exit("couldn't execute update on database")
    return(1)  
def update_db2(database,table,where_clause,sql_fields,sql_data_list):
    liste=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_data=('')
        sql_data=sql_data_list
        sql_request = f"UPDATE {table} SET "
        for item in sql_fields:
            sql_request =sql_request + item +" = ? , "
        sql_request=sql_request[:-2]
        if where_clause!='':
            sql_request=sql_request+' where '+where_clause
        print()
        print(sql_request)
        print()
        try:
            cursor.execute(sql_request)
            print("Execute UPDATE IN DB")
        except:
            sys.exit("couldn't execute update on database")
    return(1)     
def read(database,table):    
    file=open('out.txt','w')
    where=' where selected = "YES"'
    where=''
    resultats = read_db(database,table,where)    
    if resultats :
        for resultat in resultats:
            print(resultat)
            ligne_out=resultat[0]+';'+resultat[1]+';'+resultat[2]+';'+resultat[3]+';'+resultat[4]
            file.write(ligne_out)
            file.write('\n')
    else:
        print('NO RESULTS')
    file.close()
def delete_row(db_name,table_name,id):
    con = sqlite3.connect(db_name)
    sql=f"DELETE FROM '{table_name}' WHERE `index`=?"
    #print(sql)
    try:
        cur = con.cursor()
        cur.execute(sql, (id,))
        con.commit()
        return 1
    except:
        return 0
def delete_from_db(database,table,where_clause):
    con = sqlite3.connect(database)
    print()
    print('database :',variables)     
    print('table :',variables)    
    print('where clause :',where_clause)
    
    sql=f"DELETE FROM {table} where {where_clause}"
    print()
    print(yellow(sql,bold=True))
    print()    
    try:
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(green('OK DONE',bold=True))
        return 1
    except:
        print(red('Error',bold=True))
        return 0
        
def drop_table(database,table):
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print('- Deleting table : variables =>')
        sql_request="drop table variables"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : table : variables Deleted ')
def reset_table(database,table):
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        try:
            print("-- try to create : variables in case it does not exit")
            sql_create=f"CREATE TABLE IF NOT EXISTS variables ( `index` int PRIMARY KEY,name text ,environment_name text ,value text ,description text ,comment text ,used_by text)"
            c.execute(sql_create)
            print("--- OK variables table created")
        except:
            sys.exit("couldn't create variables.db")
        print('- Deleting table : variables =>')
        sql_request="drop table variables"
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : table : variables Deleted ')
        try:
            print("-- create table : network_objects")
            sql_create=f"CREATE TABLE IF NOT EXISTS variables ( `index` int PRIMARY KEY,name text ,
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,environment_name text ,
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,value text ,
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,description text ,
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,comment text ,
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,used_by text)"
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn't create variables.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=''
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print('NO RESULTS')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5])
                sql_add="INSERT OR IGNORE into variables (`index`,name,environment_name,value,description,comment,used_by) VALUES (?,?,?,?,?,?,?)"
        conn.execute(sql_add, sqlite_data)
        conn.commit()
        print(green("OK DONE",bold=True))
        
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
            print('-- Create table : variables')
        create_db_and_table()
        print('-- Ok Done - variables table succesfuly created ')
        rep=input(' Do you want to ingest demo data from ./init/variables.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : variables')
            feed_database()
            print('-- OK  Demo data succesfuly ingested into table : variables')
    except IOError:
        print(red("- NOK the database DO NOT exists... let's create it",bold=True))
        print('Create variables.db and table : variables')
        create_db_and_table()
        print('-- OK  Database and table created')
        print()
        rep=input(' Ingest demo data from ./init/variables.csv ( Y/N ) ? : ')
        if rep=='Y':
            print('-- Ingest demo data into table : variables')
            feed_database()
            print('-- OK  Demo data ingested into table : variables')
        
'''    
if __name__=='__main__':
    database="variables.db"
    table="variables"
    #main(database,table)   
    client_name='ACME COMPANY'
    #update_client_db(database,table,client_name)
    id=0
    #delete_row(id)
'''
        