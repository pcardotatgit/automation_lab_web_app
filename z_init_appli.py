'''
    modification : 20251111
    
    description : initialize the application, create empty files  clean folder
'''
import glob
import os
import json
import env as env
from crayons import *

ok_delete=1

#  def_create_connection***
def create_connection(db_file):
    '''
    MODIFIED : 2025-09-23T16:05:16.000Z
    description : create create connection to database
    
    how to call it : conn=create_connection(database)
    '''
    route="/create_connection"
    env.level+='-'
    print('\n'+env.level,white('def create_connection() in app.py : >\n',bold=True))
    #loguer(env.level+' def create_connection() in app.py : >')
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    env.level=env.level[:-1]
    return conn 
    
    
def reset_databases():
    action_type = 'replace'
    # WORKFLOWS
    print(red('RESET VARIABLES',bold=True))
    with open('./sqlite_databases_code/workflows/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    database = os.getcwd()+'/z_bases/workflows.db'
    database=database.replace("\\","/")
    print('database is :',database)
    print('table is :', db_details_dict["table_name"])
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print(f'- Deleting table : {db_details_dict["table_name"]} =>')
        sql_request="drop table "+db_details_dict["table_name"]
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
        create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
        print(f'-- OK table {db_details_dict["table_name"]} reseted')     
    db_name='workflows'
    with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    database = os.getcwd()+'/z_bases/'+db_name+'.db'
    database=database.replace("\\","/")
    print('database is :',database)
    print('table is :',db_details_dict['table_name'])
    lines=[]
    file='./DB_backups/workflows_init_20251109.csv'
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        if action_type=="replace":
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                sql_request="drop table "+db_details_dict["table_name"]
                c.execute(sql_request)
                conn.commit()
                print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
            indexA=0
        else:
            indexA=sqlite_db_get_last_index(db_name)+1
        conn=create_connection(database) # open connection to database
        for row in lines:
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let's go to every lines one by one and let's extract url, targeted brand
                len_columns=len(db_details_dict['columns'])-1
                sqlite_data=[indexA]
                for cel in row:
                    sqlite_data.append(cel)
                print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                i=0
                for col in db_details_dict['columns']:
                    print(col)
                    if i<len_columns:
                        sql_add=sql_add+col+","
                    else:
                        sql_add=sql_add+col+")"
                    i+=1
                sql_add=sql_add+' VALUES (?,'
                i=0
                for col in db_details_dict['columns']:
                    print(col)
                    if i<len_columns:
                        sql_add=sql_add+"?,"
                    else:
                        sql_add=sql_add+'?)'
                    i+=1
                #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                print('\nsql_add :',cyan(sql_add,bold=True))
            c.execute(sql_add, sqlite_data)
            print(green("==> OK Done : demo data ingested",bold=True))
            indexA+=1
            conn.commit()

    #VARIABLES
    print(red('RESET VARIABLES',bold=True))
    with open('./sqlite_databases_code/variables/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/variables/init/variables.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'value'+str(i)+','+'description'+str(i)+','+'comment'+str(i)+','+'used_by'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "variables"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/variables/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/variables_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()  
    # FUNCTIONS
    with open('./sqlite_databases_code/functions/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/functions/init/functions.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'description'+str(i)+','+'called_function'+str(i)+','+'input_variables'+str(i)+','+'output_variables'+str(i)+','+'comment'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "functions"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/functions/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/functions_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()  
    # ACCOUNT KEYS
    with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/account_keys/init/account_keys.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'type'+str(i)+','+'username'+str(i)+','+'password'+str(i)+','+'key'+str(i)+','+'comment'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "account_keys"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        
    result=1
    if result==1:
        with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/account_keys_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()
    # API_CALLS
    with open('./sqlite_databases_code/api_calls/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/api_calls/init/api_calls.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'fqdn'+str(i)+','+'relative_url'+str(i)+','+'documentation'+str(i)+','+'method'+str(i)+','+'description'+str(i)+','+'payload'+str(i)+','+'header'+str(i)+','+'body'+str(i)+','+'query_params'+str(i)+','+'custom_variables'+str(i)+','+'authentication_profile'+str(i)+','+'inputs_variables'+str(i)+','+'output_variables'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "api_calls"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/api_calls_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()  

def init_appli():
    with open('./venv/Scripts/activate.bat','w') as file:
        line_out='''@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=C:\patrick\Python_DEV\current_dev\python\z_poc_simplification\venv

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(venv) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
set VIRTUAL_ENV_PROMPT=(venv) 
python compile.py
:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)

        '''
        file.write(line_out)    
    os.remove("a.bat")
    os.remove("b.bat")
    os.remove("c.bat")
    os.remove("d.bat") 
    os.remove("e.bat")
    with open('a.bat','w') as file:
        file.write('venv\\scripts\\activate')    
    with open('b.bat','w') as file:
        file.write('python compile.py')        
    with open('port.txt','w') as file:
        file.write('4000')     
    with open('server_ip_address.txt','w') as file:
        file.write('localhost')          
                
if __name__=="__main__":
    init_appli()
    #reset_databases()    
    print('OK DONE')