#dos numeros que devuelva division (no se usan 0)
#mostrar existe un error, divicion entre cero no es posible

num1=float(input("digite el primer numero"))
num2=float(input("digite el segundo numero"))
if(num1 !=0 and num2 !=0):
    division = num1/num2
    print("la divicion es :  ",division)
else:
    print("ERROR: divicion entre 0 no es posible")