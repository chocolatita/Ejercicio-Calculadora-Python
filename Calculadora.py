Opcion = 0
While (opción!=5):
           print(“opcion1.sumar”)
print(“opción 5. Salir”)

opción= int(input(“elige una opción:))
if opción=1:
      realiza suma()
	if opción=2:
   	      realiza resta()
          if opción=3:
                 realiza multiplicación()
          if opción=4:
                 realiza división()
          if opción=5:
                  break
realiza suma():
       numero1=int(input(“introduce primer numero a sumar ”))
       numero2=int(input(“introduce segundo número a sumar”))
       numero3= numero1+numero2
       print(“el resultado de la suma es”,numero3)
realiza resta():
        numero1=int(input(“introduce primer número a restar ”))
        numero2=int(input(“introduce segundo número a restar”))
       numero3= numero1-numero2
       print(“el resultado de la resta es”,numero3)
realiza multiplicación():
        numero1=int(input(“introduce primer número a multiplicar ”))
        numero2=int(input(“introduce segundo número a multiplicar”))
        numero3= numero1*numero2
        print(“el resultado de la multiplicación es”,numero3)
realiza división():
        numero1=int(input(“introduce primer número a dividir ”))
        numero2=int(input(“introduce segundo número a dividir”))
        numero3= numero1/numero2
        print(“el resultado de la división es”,numero3)




