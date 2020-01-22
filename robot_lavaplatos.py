print("B I E N V E N I D O S A L R O B O T L A V A P L A T O S")
print("Por favor siga las instrucciones:")
def p():
    cantidad = int(input("Ingrese la cantidad de platos: "))
    r2 = input("quieres poner mas platos(P) o quieres que el robot(R) labe la loza(P/R): ")
    while r2 == "p" or r2 == "P":
        cantidad += int(input("Ingrese otra cantidad de platos: "))
        r2 = input("quieres poner mas platos(P) o quieres que el robot(R) labe la loza(P/R): ")
    function(cantidad)

def respuesta(r):
    if r == "y" or r =="Y":
        p()
    else:
        print("Gracias por seleccionar nuestro servicio, esperamos que lo vuelva a utilizar pronto")

def function(cantidad):
    while cantidad > 0:
        cantidad -= 1
        print("Platos que quedan en la pila: {}".format(cantidad+1))
    print("Los platos han sido lavados en su totalidad")
    r = input("Quiere que otra vez su robot personal labe los plato(Y/N): ")
    respuesta(r)
if __name__ == '__main__':
	r = input("Quiere que su robot personal labe los platos(Y/N): ")
	respuesta(r)