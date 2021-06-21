# ParcialHerramientasComputacionales
## **solucion del punto (d) del parcial**

### ***¿Que problema es?***

Es un problema en donde nos piden que el usuario digite unos parametros para realizar un registro para poder comprar un producto y este tendra un descuento dependiendo de que tipo de rol pertenesca el usuario en la cafeteria de la Pontificia Universidad Javeriana de cali.

### ***¿Que modelo computacional lo reselve?***

Este modelo computacional se necesitaron seis datos de entrada en donde el usuario digitaba lo que se le soliccitaba en cada una, en las salidas se obtiene solo un dato en donde se juntan en una horacion los datos de entrada digitados por el usuario. Respecto a las restrinciones del modelo computacional serian que en algunos datos de entrada no tienen limitaciones, a lo que me refiero es que se pueden colocar datos de mas de los que se piden sin saltar alguntipo de error. El algoritmo se resuelve gracias a unos datos de entrada que digita el ususrio en donde el programa los guarda y en una parte del codigo los utiliza para ejecutar un calculo para asi imprimir el resultado.

### **Este algoritmo como dato de entrada utiliza los siguientes datos:**

* rol: A lo que se refiere este dato de estrada es a que tipo de usuario pertenece en la universidad en este caso el programa funciona con dos roles que serian estudiante o profesor.
* precio: En este dato se introduce el precio del producto deseado por el usuario.
* cantidad: En este dato se introduce la cantidad de productos que desea el usuario digite.
* cedula: En este dato se introduce la cedula para que al final de la ejecucion del programa lo imprima y quede como registro.
* codigo: En este dato se introduce el codigo del producto deseado por el usuario ya que cada producto cuenta con un codigo diferente.
* producto: En este dato el usuario introduce el nombre del producto deseado.

### **Este algoritmo como salida arroja el siguiente resultado:**

* El usuario al digitar los datos de entrada los cuales son necesarios para la ejecucion del programa, el programa internamente calcula los parametros digitados por el usuario y arroja un mensaje en donde contiene cada uno de los datos de entrda con su respectiva informacion digitada por el usuario como si fuese un recibo.

### ***¿Como lo calcula?***

La forma en la que calcula este modelo realiza el calculo es la siguiente:

* primero el programa le pide al ususario unos datos los cuales son de entrada en donde se le pide: rol, precio, cantidad, cedula, codigo y producto.
* el programa al obtener estos datos los guarda en unas variables.
* cuando el programa se ejecuta en sus algoritmos se encuentran las variables que almacenan los datos digitados por el usuarioy en donde se determina la funcion que va hacer el programa, para que funcione el programa primero se utiliza la variable de rol en donde se determina que tipo de descuento se debe tener en cuenta, cuando se tiene listo el algoritmo busca las variables en donde se almacena el precio y la cantidad del producto deseado calculando el valor exacto de su compra, al finalizar el calculo el algoritmo imprime lo demas que dijito el usuario como nombre del producto, cedula, codigo y las demas variables calculadas para asi dar por finalizado el programa.

