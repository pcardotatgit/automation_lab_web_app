'''
    use functions that are into y6_trace_read_write_sqlite_database.py
    
    and manages Data in sqliteDB
'''
import sys
import csv
import sqlite3
from crayons import *
from y6_workflows_read_write_sqlite_database import read_db,update_db_generic,delete_row,read,insert_new_row
database="workflows.db"
table="workflows"
def get_rows():
    print()
    print(cyan("Read DB and select item in database to be displayed",bold=True))
    where_clause=" where `index`<10"
    #where_clause=" where `time`='time4'"
    #where_clause=" group by event"
    #print('where clause :',where_clause)
    result=read_db(database,table,where_clause)
    #print(cyan(result))
    for item in result:
        print
        print(yellow(item,bold=True))
        print()
    print(green("Done",bold=True))
    return(result)
def add_row():
    liste=['name10','address10','local_contacts10','ftd_list10','description10','version10']    
    insert_new_row(liste,database,table)
def update_db():
    # data and field are passed thru a dictionnary    
    data_to_set={"device_type":"red_cross","color":"PAT2","c3":"PAT3"}
    where="c2 = 'hitch_hacker-B' and device_type = 'expand'"
    update_db_generic(database,table,where,data_to_set)
    
def update_db2():
    # data and field are passed thru 2 lists, one for field ans one for data
    data_list=["red_cross","PAT2","PAT3"]
    field_list=["device_type","color","c3"]
    where="c2 = 'hitch_hacker-B' and device_type = 'expand'"
    update_db2(database,table,where,field_list,data_to_set)
def delete_objects():
    where="c2 = 'one_to_many_policy_matrix' and y = '-172'"
    #where="c2 = 'policy-draft-1' and device_type = 'arrow_green_round'"
    delete_from_db(database,table,where)
    
if __name__=='__main__':
    #get_rows()
    #add_row()
        #update_db()
