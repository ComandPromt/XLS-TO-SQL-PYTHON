
import pandas as pd

import mysql.connector

import os

from datetime import datetime

xls = pd.ExcelFile("listado.xls")
  
error=False;

indice=0;

contenido = ""

columnas = []

columnas.append("test")

columnas.append("test")

columnas.append("test")

columnas.append("test")

columnas.append("test")

sheetX = xls.parse(0)

texto=""

contador=0

cnx = mysql.connector.connect(user='test', password='test',host='test',database='test') 

mycursor = cnx.cursor()

sql="INSERT INTO test (test,test,test,test,test) VALUES "

def replace_last(string, find, replace):

    reversed = string[::-1]
    
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    
    return replaced[::-1]

while not error:

    try:
        for i in range(5):
        
            fila = sheetX[columnas[i]]
        
            valor =str(fila[indice]);
        
            if len(valor)==7:
                valor='1970-01-01  00:00:00'
                
            if i== 0 or i==1 or i==3:
                
                if i==1:
                   
                    mycursor.execute("SELECT test FROM test WHERE test='"+valor+"'")

                    myresult = mycursor.fetchone()
                    
                    valor=str(myresult)
                    
                    if valor != "None":
                        
                        valor=valor.replace("(","")
                        
                        valor=valor.replace(",","")
                        
                        valor=valor.replace(")","")

                    else:
                    
                        valor=""
                        
                        texto=""
                
                if i==0:

                    mycursor.execute("SELECT id FROM producto WHERE raiz='"+valor+"'")

                    myresult = mycursor.fetchone()
                    
                    valor=str(myresult)
                    
                    if valor != "None":

                        valor=valor.replace("(","")
                        
                        valor=valor.replace(",","")
                        
                        valor=valor.replace(")","")

                    else:
                    
                        valor=""
                        
                        texto=""

                if contador==1 and valor!="":
                
                    texto=texto+valor+","
                    
                    contador=1
                    
            else:
                
                if valor!="" and texto!="" and contador==1:
                
                    texto=texto+"'"+valor
                    
                if i<4:
                
                    if i==2 and valor=="nan":
   
                        texto=texto.replace("nan","")
                        
                    if valor!="" and texto!="" and contador==1:    
                        
                        texto=texto+"',"
                        
                        contador=1
                        
                    else:
                        contador=0
                        
            if valor!="" and texto!="":
                contador=1 
            else:
                contador=0
            
            if contador>0 and i==4:
            
                contador=1 
                
                sql=sql+"("+texto+"'),"
               
                texto=""

        contador=1
        
        indice+=1;
        
    except:
    
        error=True;
        
sql=replace_last(sql, ",", ";")

print(sql)

#mycursor.execute(sql)

#cnx.commit()

cnx.close()