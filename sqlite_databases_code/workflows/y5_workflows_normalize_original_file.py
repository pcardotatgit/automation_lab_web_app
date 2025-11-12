from crayons import *
from array import array
def clean_text_file(file):
    print(red(file))
    print()
    line_out=""
    with open( file, 'rb' ) as file:
        data = array( 'B', file.read() ) # buffer the file
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
    list_lines=text_out.split('\n')
    new_file_name='./init/workflows.csv'
    #new_file_name='./init/clean_workflows.csv'
    print(red(new_file_name,bold=True))
    with open(new_file_name,'w',encoding='utf-8') as fich:
        for line in list_lines:
            line=line.strip()
            if line!='':
                print(line)
                fich.write(line+'\n')
    print()
    print()    
    print(cyan('================ Original CSV file cleaning DONE ==================',bold=True))
    print()     
    
if __name__ == "__main__":
    csv_file_cleaning('./init/workflows.txt')
        print('ALL DONE')
        