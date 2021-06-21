def parcial():
    rol = input(" ¿Que rol eres? ")
    precio = int(input(" ¿Cuanto vale el producto? "))
    cantidad = int(input(" Cantidad "))
    cedula = int(input(" Digite su cedula "))
    codigo = int(input(" Dijite el codigo del producto "))
    producto = input(" Elige tu producto ")

    valor = 0
    total = precio * cantidad

    if rol == " estudiante ":
        valor = total - ((total * 50) / 100)

    else:
        valor = total - ((total * 20) / 100)

    print(" El " + rol + " de cedula: " + str(cedula) + " debe pagar: " + str(valor) + " por el producto de codigo: " + str(codigo))

parcial()



