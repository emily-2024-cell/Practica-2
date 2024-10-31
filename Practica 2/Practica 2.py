num_exam = int(input("Ingrese el numero de examenes realizados: "))
notas = int(input("ingrese sus notas: "))

promedio = sum(notas) / num_exam

print("Su promedio es:",promedio)

if promedio >=70:
    print("Aprovaste")
elif promedio >=60:
    print("Tiene que ir a ampliacion")
else:
    print("reprovaste")