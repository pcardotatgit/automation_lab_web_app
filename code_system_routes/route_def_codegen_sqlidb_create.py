#  def_codegen_sqlidb_create***
@app.route('/codegen_sqlidb_create', methods=['GET'])
def codegen_sqlidb_create():
    '''
    Created : 2025-10-29
    description : create SQLITE DB Management structure and files and add it to the application
    '''
    route="/codegen_sqlidb_create"
    env.level+='-'
    print('\n'+env.level,white('route codegen_sqlidb_create() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route codegen_sqlidb_create() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # GET variable from calling web page
        db_name=request.args.get("db_name")
        db_name=db_name.strip().lower()
        print("\ndb_name : ",db_name)
        # GET variable from calling web page
        table_name=request.args.get("table_name")
        print("\ntable_name : ",table_name)
        table_name.strip().lower()
        # GET variable from calling web page
        description=request.args.get("description")
        print("\ndescription : ",description)
        # GET variable from calling web page
        column_names=request.args.get("column_names")
        db_details={}
        db_details['db_name']=db_name
        db_details['table_name']=table_name
        db_details['description']=description
        if ',' in column_names:
            columns=column_names.split(',')
        else:
            columns=column_names.split(';')
        print("\ncolumns : ",columns)
        db_details['columns']=columns
        db_details_text=json.dumps(db_details,sort_keys=True,indent=4, separators=(',', ': '))
        if os.path.exists('./sqlite_databases_code/databases.txt'):
            print(green('OK ./sqlite_databases_code exists ',bold=True))
            if os.path.exists('./sqlite_databases_code/'+db_name+'/db_scripts.txt'):
                pass
            else:
                os.mkdir('./sqlite_databases_code/'+db_name)
                os.mkdir('./sqlite_databases_code/'+db_name+'/init')
                with open('./sqlite_databases_code/'+db_name+'/db_details.txt',"w") as file:
                    file.write(db_details_text)
                with open('./sqlite_databases_code/'+db_name+'/db_description.txt',"w") as file:
                    file.write(description)
                with open('./sqlite_databases_code/databases.txt',"a+") as file:
                    file.write(db_name+'\n')
        else:
            print(red('ERROR ./sqlite_databases_code doesn\'t exists ! Let\'s create it',bold=True))
            os.mkdir('./sqlite_databases_code')
            with open('./sqlite_databases_code/databases.txt',"w") as file:
                pass
            os.mkdir('./z_bases')
            with open('./z_bases/databases.txt',"w") as file:
                pass
            os.mkdir('./sqlite_databases_code/'+db_name)
            os.mkdir('./sqlite_databases_code/'+db_name+'/init')
            with open('./sqlite_databases_code/'+db_name+'/db_details.txt',"w") as file:
                file.write(db_details_text)
            with open('./sqlite_databases_code/'+db_name+'/db_description.txt',"w") as file:
                file.write(description)
            with open('./sqlite_databases_code/databases.txt',"a+") as file:
                file.write(db_name+'\n')
        '''
        if os.path.exists('./z_bases/store_sqllite_DBs.txt'):
            print(green('OK ./z_bases exists ',bold=True))
        else:
            print(red('ERROR ./z_bases doesn\'t exists ! Let\'s create it',bold=True))
            os.mkdir('./z_bases')
            with open('./z_bases/store_sqllite_DBs.txt',"w") as file:
                pass
        '''
        output='''\'\'\'
    create the '''+db_name+'''.csv csv file to be ingested into the DB for testing
\'\'\'
import sys
import sqlite3
from crayons import *
    
def create_csv_demos_data():    
    file=open(\'./init/'''+db_name+'''.csv\',\'w\')
    ligne_out=\''''
        for col in columns:
            output=output+col+','
        output=output[:-1]
        output=output+'''\'
    file.write(ligne_out)
    file.write(\'\\n\')
    for i in range (0,10):
        ligne_out=\''''
        len_columns=len(columns)-1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+'''\'+str(i)+\',\'+\''''
            else:
                output=output+col+'''\'+str(i)'''
            i+=1
        output=output+'''
        file.write(ligne_out)
        file.write(\'\\n\')
    file.close()
 
if __name__==\'__main__\':
    create_csv_demos_data()
    print(green(\'DONE '''+db_name+'''.csv for demos data was created\',bold=True))
    '''
        with open('./sqlite_databases_code/'+db_name+'/y1_'+db_name+'_create_csv_demo_file_to_ingest_into_db.py','w') as file:
            file.write(output)
            
        output='''import sys
import csv
from crayons import *
import sqlite3
import os
import json
def create_connection(db_file):
    \'\'\' create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    \'\'\'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
   
def create_db_and_table():    
    #with sqlite3.connect(\':memory:\') as conn:
    with sqlite3.connect(\''''+db_name+'''.db\') as conn:
        c=conn.cursor()
        try:
            print("--- table : '''+table_name+''' creation")
            sql_create=f"CREATE TABLE IF NOT EXISTS '''+table_name+''' (`index` int PRIMARY KEY,'''
        len_columns=len(columns)-1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+''' text ,'''
            else:
                output=output+col+''' text'''
            i+=1
        output=output+''')"
            c.execute(sql_create)
            print(green("--- OK '''+table_name+''' table created",bold=True))
        except:
            sys.exit(red("couldn\'t create '''+table_name+''' table",bold=True))
    return()    
    
def feed_database():
    database = os.getcwd()+\'/'''+db_name+'''.db\'
    database=database.replace("\\\\","/")
    print(\'database is :\',database)
    lines=[]    
    file=\'./init/'''+db_name+'''.csv\' 
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=\',\')
        lines = list(reader)
        indexA=0
        print()
        print(\' '''+table_name+''' table =>\')
        print()
        for row in lines:
            #print (\'print the all row  : \' + row)
            print('''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+'''row['''+str(i)+'''] ,'''
            else:
                output=output+'''row['''+str(i)+'''])'''
            i+=1
        output=output+'''
            #print(row)
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let\'s go to every lines one by one and let\'s extract url, targeted brand
                sqlite_data=(indexA,'''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+'''row['''+str(i)+'''] ,'''
            else:
                output=output+'''row['''+str(i)+'''])\n                sql_add="INSERT OR IGNORE into '''+table_name+''' (`index`,'''
            i+=1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+','
            else:
                output=output+col+') VALUES (?,'
            i+=1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+'?,'
            else:
                output=output+'?)"'
            i+=1
        output=output+'''
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
    conn=create_connection(\''''+db_name+'''.db\') # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print(\'- Deleting table : '''+table_name+''' =>\')
        sql_request="drop table : '''+table_name+'''"
        c.execute(sql_request)
        conn.commit()
        print(\'-- OK DONE : Deleting table : '''+table_name+'''\')
        create_db_and_table()
        print(green(\'OK '''+table_name+'''.db created\',bold=True))
        print(yellow(\'Now ingest data into DB\',bold=True))
        feed_database()
        print(\'-- OK data ingested\')
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+\'/'''+db_name+'''.db\'
        database=database.replace("\\\\","/")
        print(\'database is :\',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(\' Do you want to create the '''+table_name+''' table ( Y/N ) ? : \')
        if rep==\'Y\':
            print(\'-- Ok let\\'s Create table : '''+table_name+'''\')
        create_db_and_table()
        print(green(\'-- Ok Done - '''+table_name+''' table succesfuly created \',bold=True))
        rep=input(\' Do you want to ingest demo data from ./init/'''+db_name+'''.csv ( Y/N ) ? : \')
        if rep==\'Y\':
            print(\'-- Ingest demo data into table : '''+table_name+'''\')
            feed_database()
            print(green(\'-- OK  Demo data succesfuly ingested into table : '''+table_name+'''\',bold=True))
    except IOError:
        print(red("- NOK the database DO NOT exists... let\'s create it",bold=True))
        print(\'Create '''+db_name+'''.db and table : '''+table_name+'''\')
        create_db_and_table()
        print(\'-- OK  Database and table created\')
        print()
        rep=input(\' Ingest demo data from ./init/'''+db_name+'''.csv ( Y/N ) ? : \')
        if rep!=\'N\':
            print(\'-- Ingest demo data into table : '''+table_name+'''\')
            feed_database()
            print(\'-- OK  Demo data ingested into table : '''+table_name+'''\')
        
if __name__ == "__main__":
    create_database_if_not_exits()
            print(\'ALL DONE\')
        '''
        with open('./sqlite_databases_code/'+db_name+'/y2_'+db_name+'_create_db_read_csv_to_db_line_by_line.py','w') as file:
            file.write(output)
        output='''import pandas as pd
import sqlalchemy
from pandas import DataFrame
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
db_name = "'''+db_name+'''.db"
table_name = "'''+table_name+'''"
engine = sqlalchemy.create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
df = pd.read_sql_table(table_name, engine)
out_df = df[[\''''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+"','"
            else:
                output=output+col+"']]"
            i+=1
        output=output+'''
#save result to csv file
out_df.to_csv(r\''''+db_name+'''.csv\')
df = DataFrame(out_df)
print (df)
print(\'=========================================\')
print(\'DONE\')
            '''
        with open('./sqlite_databases_code/'+db_name+'/y3_'+db_name+'_read_sqlite_db_and_create_csv.py','w') as file:
            file.write(output)
        output='''import pandas as pd
from sqlalchemy import create_engine
# the csv file is : '''+db_name+'''.csv
# database will be : '''+db_name+'''.db
# the table name is  : '''+table_name+'''
df = pd.read_csv(\''''+db_name+'''s.csv\', sep=\',\')
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
engine = create_engine(\'sqlite:///'''+db_name+'''.db\')
df.to_sql(\''''+table_name+'''\', engine) #With this one the table and database must not already exists
#df.to_sql(\''''+table_name+'''\', con=engine, if_exists=\'append\')   #with this one you can append data to an existing database
#df.to_sql(\''''+table_name+'''\', con=engine, if_exists=\'replace\')   #with this one you can truncat an existing database
'''
        with open('./sqlite_databases_code/'+db_name+'/y4_'+db_name+'_ingest_csv_into_sqlite_db_panda.py','w') as file:
            file.write(output)
        output='''from crayons import *
from array import array
def clean_text_file(file):
    print(red(file))
    print()
    line_out=""
    with open( file, \'rb\' ) as file:
        data = array( \'B\', file.read() ) # buffer the file
        list=[147,148]
                for byte in data:
            v = byte # int value
            if v > 140 and v < 160:
                #print(red(f"{v} : {c}"))
                #print(c)
                c = chr(32)
            elif v == 226:
                #print(yellow(f"{v} : {c}"))
                c = chr(32)
                #print(c)
            elif v == 255:
                #print(yellow(f"{v} : {c}"))
                c = chr(46)
                        #print(c)
            elif v not in list:
                c = chr(byte)
            else:
                c = chr(39)
            #print(yellow(f"{v} : {c}"))
            #print(c)
            line_out+=c
    return(line_out)
    
def csv_file_cleaning(fichier):
    text_out=clean_text_file(fichier)
    list_lines=text_out.split(\'\\n\')
    new_file_name=\'./init/'''+db_name+'''.csv\'
    #new_file_name=\'./init/clean_'''+db_name+'''.csv\'
    print(red(new_file_name,bold=True))
    with open(new_file_name,\'w\',encoding=\'utf-8\') as fich:
        for line in list_lines:
            line=line.strip()
            if line!=\'\':
                print(line)
                fich.write(line+\'\\n\')
    print()
    print()    
    print(cyan(\'================ Original CSV file cleaning DONE ==================\',bold=True))
    print()     
    
if __name__ == "__main__":
    csv_file_cleaning(\'./init/'''+db_name+'''.txt\')
        print(\'ALL DONE\')
        '''
        with open('./sqlite_databases_code/'+db_name+'/y5_'+db_name+'_normalize_original_file.py','w') as file:
            file.write(output)
        output='''\'\'\'
    this resource manages interaction with the sqllite database
\'\'\'
import sys
import sqlite3
from crayons import *
from datetime import datetime, timedelta
import time
import json
def date_time():
    \'\'\'
        get current date time in yy-mm-dd-H:M:S:fZ format
    \'\'\'
    current_time = datetime.utcnow()
    current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    current_date=current_time.split(\'T\')[0]
    return(current_time,current_date)
def create_connection(db_file):
    \'\'\' create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    \'\'\'
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
            sys.exit("couldn\'t read database")
    return(liste) 
    
def update_db_generic(database,table,where_clause,data):
    liste=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_request = f"UPDATE {table} SET "
        for key,value in data.items():
            print(cyan(key))
            print(red(value))
            sql_request =sql_request + key +" = \'"+value+"\',"
        sql_request=sql_request[:-1]
        if where_clause!=\'\':
            sql_request=sql_request+\' where \'+where_clause
        print()
        print(sql_request)
        print()
        try:
            cursor.execute(sql_request)
            print("Execute UPDATE IN DB")
        except:
            sys.exit("couldn\'t execute update on database")
    return(1)  
def update_db2(database,table,where_clause,sql_fields,sql_data_list):
    liste=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_data=(\'\')
        sql_data=sql_data_list
        sql_request = f"UPDATE {table} SET "
        for item in sql_fields:
            sql_request =sql_request + item +" = ? , "
        sql_request=sql_request[:-2]
        if where_clause!=\'\':
            sql_request=sql_request+\' where \'+where_clause
        print()
        print(sql_request)
        print()
        try:
            cursor.execute(sql_request)
            print("Execute UPDATE IN DB")
        except:
            sys.exit("couldn\'t execute update on database")
    return(1)     
def read(database,table):    
    file=open(\'out.txt\',\'w\')
    where=\' where selected = "YES"\'
    where=\'\'
    resultats = read_db(database,table,where)    
    if resultats :
        for resultat in resultats:
            print(resultat)
            ligne_out=resultat[0]+\';\'+resultat[1]+\';\'+resultat[2]+\';\'+resultat[3]+\';\'+resultat[4]
            file.write(ligne_out)
            file.write(\'\\n\')
    else:
        print(\'NO RESULTS\')
    file.close()
def delete_row(db_name,table_name,id):
    con = sqlite3.connect(db_name)
    sql=f"DELETE FROM \'{table_name}\' WHERE `index`=?"
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
    print(\'database :\','''+db_name+''')     
    print(\'table :\','''+table_name+''')    
    print(\'where clause :\',where_clause)
    
    sql=f"DELETE FROM {table} where {where_clause}"
    print()
    print(yellow(sql,bold=True))
    print()    
    try:
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(green(\'OK DONE\',bold=True))
        return 1
    except:
        print(red(\'Error\',bold=True))
        return 0
        
def drop_table(database,table):
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print(\'- Deleting table : '''+table_name+''' =>\')
        sql_request="drop table '''+table_name+'''"
        c.execute(sql_request)
        conn.commit()
        print(\'-- OK DONE : table : '''+table_name+''' Deleted \')
def reset_table(database,table):
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        try:
            print("-- try to create : '''+table_name+''' in case it does not exit")
            sql_create=f"CREATE TABLE IF NOT EXISTS '''+table_name+''' ( `index` int PRIMARY KEY,'''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+''' text ,'''
            else:
                output=output+col+''' text)"'''
            i+=1
        output=output+'''
            c.execute(sql_create)
            print("--- OK '''+table_name+''' table created")
        except:
            sys.exit("couldn\'t create '''+db_name+'''.db")
        print(\'- Deleting table : '''+table_name+''' =>\')
        sql_request="drop table '''+table_name+'''"
        c.execute(sql_request)
        conn.commit()
        print(\'-- OK DONE : table : '''+table_name+''' Deleted \')
        try:
            print("-- create table : network_objects")
            sql_create=f"CREATE TABLE IF NOT EXISTS '''+table_name+''' ( `index` int PRIMARY KEY,'''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+''' text ,'''
            else:
                output=output+col+''' text)"'''
            i+=1
            output=output+'''
            c.execute(sql_create)
            print("--- OK network_objects table created")
        except:
            sys.exit("couldn\'t create '''+db_name+'''.db")
        
def insert_new_row(row,database,table): # row is a list of items
    print()
    print(cyan("insert a new row into DB",bold=True))
            print(row)
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        # STEP 1 get the number of item in the database in order to calculate the next index
        where=\'\'
        resultats = read_db(database,table,where)
        nb=0
        if resultats :
            for resultat in resultats:
                #print(resultat)
                nb+=1
        else:
            print(\'NO RESULTS\')
        # STEP 2 : add the new item into the database
        indexA=nb+1
        sqlite_data=(indexA,'''
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+'''row['''+str(i)+'''] ,'''
            else:
                output=output+'''row['''+str(i)+'''])\n                sql_add="INSERT OR IGNORE into '''+table_name+''' (`index`,'''
            i+=1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+col+','
            else:
                output=output+col+') VALUES (?,'
            i+=1
        i=0
        for col in columns:
            print(col)
            if i<len_columns:
                output=output+'?,'
            else:
                output=output+'?)"'
            i+=1
        output=output+'''
        conn.execute(sql_add, sqlite_data)
        conn.commit()
        print(green("OK DONE",bold=True))
        
def create_database_if_not_exits():
    try:
        database = os.getcwd()+\'/'''+db_name+'''.db\'
        database=database.replace("\\\\","/")
        print(\'database is :\',database)
        f = open(database)
        print(green("- OK the database exists",bold=True))
        f.close()
        rep=input(\' Do you want to create the '''+table_name+''' table ( Y/N ) ? : \')
        if rep==\'Y\':
            print(\'-- Create table : '''+table_name+'''\')
        create_db_and_table()
        print(\'-- Ok Done - '''+table_name+''' table succesfuly created \')
        rep=input(\' Do you want to ingest demo data from ./init/'''+db_name+'''.csv ( Y/N ) ? : \')
        if rep==\'Y\':
            print(\'-- Ingest demo data into table : '''+table_name+'''\')
            feed_database()
            print(\'-- OK  Demo data succesfuly ingested into table : '''+table_name+'''\')
    except IOError:
        print(red("- NOK the database DO NOT exists... let\'s create it",bold=True))
        print(\'Create '''+db_name+'''.db and table : '''+table_name+'''\')
        create_db_and_table()
        print(\'-- OK  Database and table created\')
        print()
        rep=input(\' Ingest demo data from ./init/'''+db_name+'''.csv ( Y/N ) ? : \')
        if rep==\'Y\':
            print(\'-- Ingest demo data into table : '''+table_name+'''\')
            feed_database()
            print(\'-- OK  Demo data ingested into table : '''+table_name+'''\')
        
\'\'\'    
if __name__==\'__main__\':
    database="'''+db_name+'''.db"
    table="'''+table_name+'''"
    #main(database,table)   
    client_name=\'ACME COMPANY\'
    #update_client_db(database,table,client_name)
    id=0
    #delete_row(id)
\'\'\'
        '''
        with open('./sqlite_databases_code/'+db_name+'/y6_'+db_name+'_read_write_sqlite_database.py','w') as file:
            file.write(output)
        output='''\'\'\'
    use functions that are into y6_trace_read_write_sqlite_database.py
    
    and manages Data in sqliteDB
\'\'\'
import sys
import csv
import sqlite3
from crayons import *
from y6_'''+db_name+'''_read_write_sqlite_database import read_db,update_db_generic,delete_row,read,insert_new_row
database="'''+db_name+'''.db"
table="'''+table_name+'''"
def get_rows():
    print()
    print(cyan("Read DB and select item in database to be displayed",bold=True))
    where_clause=" where `index`<10"
    #where_clause=" where `time`=\'time4\'"
    #where_clause=" group by event"
    #print(\'where clause :\',where_clause)
    result=read_db(database,table,where_clause)
    #print(cyan(result))
    for item in result:
        print
        print(yellow(item,bold=True))
        print()
    print(green("Done",bold=True))
    return(result)
def add_row():
    liste=[\'name10\',\'address10\',\'local_contacts10\',\'ftd_list10\',\'description10\',\'version10\']    
    insert_new_row(liste,database,table)
def update_db():
    # data and field are passed thru a dictionnary    
    data_to_set={"device_type":"red_cross","color":"PAT2","c3":"PAT3"}
    where="c2 = \'hitch_hacker-B\' and device_type = \'expand\'"
    update_db_generic(database,table,where,data_to_set)
    
def update_db2():
    # data and field are passed thru 2 lists, one for field ans one for data
    data_list=["red_cross","PAT2","PAT3"]
    field_list=["device_type","color","c3"]
    where="c2 = \'hitch_hacker-B\' and device_type = \'expand\'"
    update_db2(database,table,where,field_list,data_to_set)
def delete_objects():
    where="c2 = \'one_to_many_policy_matrix\' and y = \'-172\'"
    #where="c2 = \'policy-draft-1\' and device_type = \'arrow_green_round\'"
    delete_from_db(database,table,where)
    
if __name__==\'__main__\':
    #get_rows()
    #add_row()
        #update_db()
'''
        with open('./sqlite_databases_code/'+db_name+'/y7_'+db_name+'_example_of_queries.py','w') as file:
            file.write(output)
        #
        # Create sub scripts structure here under
        #
        create_rte_for_db_dashboard(db_name)
        create_rte_for_create_db(db_name)
        create_rte_for_db_demo_data(db_name)
        create_rte_for_db_clear_function(db_name)
        create_rte_for_db_read_function(db_name)
        create_rte_for_db_update_entry_function(db_name)
        create_rte_for_db_delete_entry_function(db_name)
        create_rte_for_db_add_entry_function(db_name)
        create_rte_for_db_ingest_cvs(db_name)
        create_rte_for_sqlite_db_duplicate_entry_function(db_name)
        message1="SQLITE DB CREATED"
        image="../static/images/ok.png"
        message2="SQLITE DB structure and files had been created and added into this application."
        message3="/stop"
        message4="YOU MUST RESTART FLASK !!"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF codegen_sqlidb_create() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
