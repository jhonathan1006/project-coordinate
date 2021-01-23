print("CONVERSION DE COORDENADAS GEOGRAFICAS A UTM")
print("Método Cotichia-Surace")
# ingresando los valores de forma
Longitud= ("73°7'24.97”W") 
Latitud = ("7◦6'18,42”N")
print("Longitud(ƛ)")
print(Longitud)
print("Latitud(Φ)")
print(Latitud)
#print("Valores de semieje de la tierra:")
#existe la posibilidad de cambiar los valores de los semiejes
numero_a=6378137
numero_b= 6356752.314245
#print("Semi_eje mayor")
#print(numero_a)
#print("Semi_eje menor")
#print(numero_b)
#Ecuacion 1
#print("Hallando los valores de las excentricidades:")
numeroExcm=(((numero_a)**2-(numero_b)**2)**0.5)/numero_b
#print("Excentricidad mayor es:")
#print(numeroExcm)
#Ecuacion 2
numeroExc=(((numero_a)**2-(numero_b)**2)**0.5)/numero_a
#print("Excentricidad menor es:")
#print(numeroExc)
#Ecuacion 3
#print("Hallando el cuadrado de la excentricad mayor:")
numero_c=numeroExcm**2
#print("El valor de la excentricad mayor al cuadrado  es:")
#print(numero_c)

#Ecuacion 4
#print("Hallando el radio polo de la curvatura:")
numeroRadio=(numero_a)**2/numero_b
#print("El valor del aplanamiento es:"+str(numeroRadio))


#Ecuacion 4
#print("Hallando el aplanamiento:")
numero_apla=(numero_a-numero_b)/numero_a
#print("El valor del aplanamiento es:")
#print(numero_apla)

# valor a ingresar dato muy importante
#Ecuacion 5
print("")
print("Conviertiendo los valores de latitud y longitud en grados decimales:")

Longitud= ("73°7'24.97”W")
numeroLong= (73+7/60+24.97/3600)
Latitud = ("7◦6'18,42”N")
numeroLat= (7+6/60+18.42/3600)
print("Longitud(ƛ)")
print(numeroLong)
print("Latitud(Φ)")
print(numeroLat)
#
print("")
print("Analizando el signo de los valores de latititud y longitud:") 
#print("Si la longitud esta asociada al oeste del meridiano de greenwich entonces el signo es negativo, y si pertenece al este el signo será positivo")
#print("Si la latitud corresponde sobre la linea ecuatorial el valor del signo sera pisitivo; si se encuentra por de bajo de la linea acuatorial el valor será negativo")
print("")
print("Asociando los valores del signo de latitud y longitud en grados decimales:")
Longitud= ("3°48'06,7439''W")
numeroLong1= numeroLong*(-1) #EVALUAR SIGNO DE LOS DATOS
Latitud = ("43°29'18,2670''N")
numeroLat1= numeroLat*(1) #EVALUAR SIGNO DE LOS DATOS
print("Longitud(ƛ)")
print(numeroLong1)
print("Latitud(Φ)")
print(numeroLat1)

#Ecuacion 6
print("")
print("Asociando los valores del signo de latitud y longitud en radianes:")
import math
math.pi
pi= math.pi
Longitud= ("3°48'06,7439''W")
numeroLorad= numeroLong1*pi/180
Latitud = ("43°29'18,2670''N")
numeroLarad= numeroLat1*pi/180
print("Longitud(ƛ)")
print(numeroLorad)
print("Latitud(Φ)")
print(numeroLarad)
print("")
#Ecuacion 7
print("Intentamos calcular el Huso:")
numeroHuso= int((numeroLong1/6)+31)
print("El valor del huso es:" +str(numeroHuso)+", debe considerarse el valor entero")
print("")
#Ecuacion 8
print("Calcualmos el meridiano del huso:")
numeroMeri=numeroHuso*6-183
print("El valor del huso es:" +str(numeroMeri))
#Ecuacion 9
print("")
print("Calculamos la distancia angular entre la longitud de un punto y el meridiano:")
numeroDist= (numeroLorad- numeroMeri*(pi/180))
print("El resultados es:" +str(numeroDist))

#Ecuacion 9
print("")
print("INTENTAMOS UTILIZAR  LOS PARAMETROS DE COTICCHIA-SURACE")
numeroA= math.cos(numeroLarad)*math.sin(numeroDist)
#print(numeroA)
numeroE= 0.5*(math.log((1+numeroA)/(1-numeroA)))
#
numeroN= (math.atan(math.tan(numeroLarad)/math.cos(numeroDist)))- numeroLarad
#
numeroV= (numeroRadio/(1+numero_c*math.cos(numeroLarad)**2)**0.5)*0.9996
#
numeroZ= ((numero_c/2)*numeroE**2*math.cos(numeroLarad)**2)
#
numeroA1= math.sin(2*numeroLarad)
#
numeroA2= numeroA1*math.cos(numeroLarad)**2
#
numeroJ2= numeroLarad+(numeroA1/2)
#
numeroJ4= (3*numeroJ2+numeroA2)/4
#
numeroJ6= (5*numeroJ4+numeroA2*math.cos(numeroLarad)**2)/3
#
numero_I= (0.75*numero_c )
#
numero_B= ((5/3)*numero_I**2)
#
numero_G= ((35/27)*numero_I**3)
#
numero_B0= 0.9996*numeroRadio*(numeroLarad-numero_I*numeroJ2+numero_B*numeroJ4-numero_G*numeroJ6)
#
print("")
print("Calculamos las cordenadas UTM")
numero_X= (numeroE*numeroV*(1+(numeroZ/3)))+500000
print("El valor  de la coordena en el eje X es:" +str(numero_X))
#
numero_Y= (numeroN*numeroV*(1+numeroZ))+ numero_B0
print("El valor  de la coordena en el eje Y es:" +str(numero_Y))
