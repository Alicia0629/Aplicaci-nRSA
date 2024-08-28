import math
import random


def generar_claves_automaticamente():
  while True:
    p=int(random.choice(open("primos"+str(random.randrange(100))+".txt","r").read().split(", ")))
    q=int(random.choice(open("primos"+str(random.randrange(100))+".txt","r").read().split(", ")))
    if p>q:
      p,q=q,p
    if (p*algoritmo_extendido_de_euclides(p,q))%q ==1:
      break
  phi=(p-1)*(q-1)
  while True:
    posible_e=int(random.randint(3,phi))
    if math.gcd(posible_e,phi) == 1:
      e=posible_e
      d=algoritmo_extendido_de_euclides(e,phi)
      if (e*d)%phi==1:
        break
  print("KU { e="+str(e)+", n="+str(p*q)+"}")
  print("KR { d="+str(d)+", p="+str(p)+", q="+str(q)+"}")

def cifrar():
  plaintext=input("Ingresa un texto que cifrar: ")
  print("Ingresa la llave pública:")
  claves=clave("KU")
  e=claves[0]
  n=claves[1]
  print(" ")
  lista=(texto_a_numeros(plaintext,n))
  lista2=[]
  for i in lista:
    lista2.append(sliding_window_exponentiation(i,e,n))
  print("Texto cifrado: '"+numeros_a_texto(lista2,n)+"'")

def descifrar_teorema_chino_del_resto():
  ciphertext=input("Ingresa un texto que descifrar: ")
  print("Ingresa la llave privada:")
  claves=clave("KR")
  d=claves[0]
  p=claves[1]
  q=claves[2]
  print(" ")
  lista=[]
  pinverso= algoritmo_extendido_de_euclides(q,p)
  t=pinverso%q
  for i in (texto_a_numeros(ciphertext,p*q)):
    mp=pow(i,d%(p-1),p)
    mq=pow(i,d%(q-1),q)
    u=((mq-mp)*t)%q
    m=mp+u*p
    lista.append(m)
  return("Texto descifrado: '"+numeros_a_texto(lista,p*q)+"'")

l=" ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")

def texto_a_numeros(texto,n):
  a=0
  for i in range(len(texto)):
    a+=pow(len(l),len(texto)-1-i) * (l.index(texto[i]))
  b=a
  c=[]
  for i in range(int(math.log(a,n)),-1,-1):
    c.append(b//pow(n,i))
    b-=c[-1]*pow(n,i)
  return(c)

def numeros_a_texto(c,n):
  m=0
  m2=[]
  prueba=[]
  pr2=[]
  for i in range(len(c)):
    m+=c[i]*pow(n,len(c)-i-1)
    prueba.append(len(c)-i-1)
    pr2.append(c[i])
  texto=""
  for i in range(int(math.log(m,len(l))),-1,-1):
    texto+=l[m//pow(len(l),i)]
    m-=l.index(texto[-1])*pow(len(l),i)
  return(texto)

def sliding_window_exponentiation(x,exponente_inicial,n):

  exponente_para_2=[]
  i=2

  while pow(2, sum(exponente_para_2))<=exponente_inicial:
    i+=1
    exponente_para_2.append(i)
  exponente_para_2.remove(i)
  exponente_para_2.append(0)


  exponente_para_x=[]
  for i in range(len(exponente_para_2)):
    j=0
    while j*pow(2,sum(exponente_para_2[i:]))<=exponente_inicial:
      j+=1
    exponente_para_x.append(j-1)
    exponente_inicial-=exponente_para_x[-1]*pow(2,sum(exponente_para_2[i:]))

  exponentes_para_y=[1]
  for i in range(len(exponente_para_x)-1):
    exponentes_para_y.append(pow(2,(3+i)))

  y=1
  for i in range(len(exponente_para_x)):
    y=pow(y,exponentes_para_y[i],n)
    y*=pow(x,exponente_para_x[i])
    y%=n
  return(y)

def algoritmo_extendido_de_euclides(p,q):
  if p<q:
    p,q=q,p
  a=[p]
  b=[q]
  c=[p//q]
  while True:
    a2=b[-1]
    b2=a[-1]%b[-1]
    a.append(a2)
    b.append(b2)
    c.append(a2//b2)
    if a2%b2==1:
      break
  x=0
  y=1
  for i in range(len(c)-1,-1,-1):
    y2=x-c[i]*y
    x2=y
    y=y2
    x=x2
  return y

def clave(a):
  clave=[""]
  for i in input(a+": ")+".":
    if i in "1234567890-":
      clave[-1]=clave[-1]+i
    else:
      if clave[-1] != "":
        clave.append("")
  return list(map(int,(clave[:-1])))

while True:
  print("Acción 1 --> generar claves.")
  print("Acción 2 --> cifrar.")
  print("Acción 3 --> descifrar.")
  accion=input("¿Qué acción quieres realizar?[1/2/3] ")
  print(" ")
  if accion == "1":
    generar_claves_automaticamente()
  elif accion == "2":
    cifrar()
  elif accion == "3":
    print(descifrar_teorema_chino_del_resto())
  else:
    print("Debes ingresar 1, 2 o 3.")

  print(" ")
  print("_"*50)
  print(" ")

