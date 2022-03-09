import sys
import re

def procesar(texto):
  arrayText=[]
  txt=""
  
  for i in range(len(texto)):
    if texto[i]!="\n":
      txt=txt+texto[i]
    if texto[i]=="\n" or i==len(texto)-1:
      arrayText.append(txt)
      txt=""
  return arrayText
  

def reducir(arreglo):
  new_texto=[]
  value=[]
  lista=[]
  for i in range(len(arreglo)):
    newtexto= filter(str.isalpha, arreglo[i])
    new_texto.append(str(''.join(list(newtexto))))
    
    new_value = filter(str.isdigit, arreglo[i])
    value.append(int(''.join(list(new_value))))

  for i in range(len(arreglo)):
    lista.append([new_texto[i],value[i]])

  new_lista=[]
  divisor=[]

  diccionario = dict()
  for p in new_texto:
    diccionario[p] = diccionario.get(p, 0)+1

  for clave in diccionario:
    divisor.append([clave,diccionario[clave]])

  diccionario = dict()
  for p in new_texto:
    diccionario[p] = diccionario.get(p, 0)

  for clave in diccionario:
    new_lista.append([clave,diccionario[clave]])

  for i in range(len(new_lista)):
    for j in range(len(lista)):
      if new_lista[i][0]==lista[j][0]:
        new_lista[i][1]=(new_lista[i][1]+lista[j][1])
    new_lista[i][1]=new_lista[i][1]//divisor[i][1]
  print(new_lista)

for line in sys.stdin:
  newline = newline+"\n"+line
  texto=texto+newline

reducir(procesar(texto))