import sys
import re

def procesar(texto):
  t=""
  for i in range(len(texto)):
    t=t+texto[i]
  y=re.sub(r'[^\w\s]','',t)
  y=y.lower()
  x=y.split()
  return x

def reducir(arreglo):
  diccionario = dict()
  for p in arreglo:
    diccionario[p] = diccionario.get(p, 0)+1

  for clave in diccionario:
    print(diccionario[clave],clave)

def procesar2(texto):
  txt=""
  cont1=0
  for i in range(len(texto)):
    if texto[i]=="\t":
      cont1=cont1+1
    if cont1==0:
      txt=txt+texto[i]
  return txt

for line in sys.stdin:
  newline = newline+"\n"+line
  texto=texto+newline

reducir(procesar(texto))