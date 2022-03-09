import sys
import re

def reducir(txt):
  print(txt)

def procesar(texto):
  txt=""
  cont1=0
  cont2=0
  cont3=0
  for i in range(len(texto)):
    if cont2==2:
      if texto[i]=="-":
        cont3=cont3+1
      if cont3==0:
        txt=txt+texto[i]
    if texto[i]=="{":
      cont1=cont1+1
    if texto[i]==",":
      cont2=cont2+1
    
  if cont1>=1:
    return txt
  else:
    return ""



for line in sys.stdin:
  print("\n")
  reducir(procesar(line))