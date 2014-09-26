n = int(input("Escribe un número x mayor a 1 y te diremos los números primos desde el 2 hasta el x: "))

for x in range(1 ,n + 1):
   if x > 1:
       for y in range(2,x):
           if (x % y) == 0:
               print("{} no es primo".format(x))
               break
       else:
           print("{} es primo".format(x))
