# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:40:46 2017

@author: Winterfell
"""

import sqlite3 as sql
import sys

con=sql.connect('QuizPortal.db')
c = con.cursor()

def Student_reg(Name,userid,courseid):
    print(Name,userid,courseid,file=sys.stout,sep=' ',end='\n')

def Upload_file():
    try:
        fname=filedialog.askopenfilename()
        print(fname)
        with open("fname",'r') as csv_file:
            
            intermediate_file=csv_file.read()
            next(intermediate_file)
            for row in intermediate_file:
                c.execute("INSERT INTO QuestionSet VALUES(Question_text);")
    except FileNotFoundError:
        print("File you specifies does not exist.")
    except PermissionError:
        print("You do not have adequate permission to access the file.")
# Close connection
con.close()