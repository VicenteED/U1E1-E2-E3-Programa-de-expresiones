
from itertools import product

class punto2:
    operadores = []
    tabla = {}
    def separa_entrada(self):
        operacion = "((p->q)^p)->q"
        #operacion = "p^q"
        #operacion = "svp"
        resultado = []
        operacionActual = "" #Variable para cuando sea un '->'
        for posicion in operacion:
            #verifica si la posicion actual es una letra y en caso de que lo sea que no sea un 'v'
            if( posicion.isalpha() and posicion != "v" ):
                if( operacionActual != ""): #Se tiene que agregar '->'
                    resultado.append(operacionActual)
                    operacionActual = "" #Reiniciamos la variable.
                resultado.append(posicion)
                #Agregamos cada nueva letra a la lista de operadores generales para la tabla de verdad.
                if( posicion not in self.operadores):
                    self.operadores.append(posicion)
            elif( posicion == "(" or posicion == ")"):
                #Los parentesis se agregan directo a el resultado.
                resultado.append(posicion)
            else:
                #Combinamos los caracteres que no cumplan las condiciones anteriores.
                operacionActual+=posicion
        self.generar_tabla()
        self.transformar_notacion(resultado)
    def generar_tabla(self):
        #Usamos la libreria importada para realizar las combinaciones.
        global condiciones
        condiciones = list(product([False,True], repeat=len(self.operadores) ) )
        #Mandamos cada tupla al siguiente metodo para que se combinen con los operadores.
        for condicion in condiciones:
            #Se mandan las condiciones como objetos iterables.
            self.combinar_tabla(*condicion)
    def combinar_tabla(self,*args):
        #Recibimos las condiciones y las guardamos en un diccionario de datos.
        for operador, valor in zip(self.operadores, args):
            if( operador not in self.tabla):
                self.tabla[operador] = [valor]
            else:
                #Obtenemos la lista actual del diccionario
                auxiliar = self.tabla.get(operador)
                #Agregamos el nuevo valor a lista
                auxiliar.append(valor)
                #Actualizamos la lista
                self.tabla[operador] = auxiliar

    def transformar_notacion(self,operacion):
        salida, pilaTemporal = [], [] #Generamos 2 listas.
        while( len(operacion) > 0 ):
            #Obtenemos el primer elemento de la operacion, lo eliminamos y guardamos en una nueva variable.
            elementoActual = operacion.pop(0) 
            if( elementoActual.isalpha() and elementoActual != "v"): #'v' es el operador OR
                salida.append(elementoActual) #Guardamos variables directamente en la salida.
            elif( elementoActual == "("):
                #Los '(' sirven como topes para saber cuando dejar de sacar elementos de pila.
                pilaTemporal.append(elementoActual)
            elif( elementoActual == ")"):
                #Sacar elementos de pila hasta que esta no tenga elementos o se encuentre con un tope.
                while( len(pilaTemporal) > 0 and pilaTemporal[-1] != "("):
                    auxiliar = pilaTemporal.pop()
                    salida.append(auxiliar)
                if(pilaTemporal[-1] == "("):
                    pilaTemporal.pop()
            else:
                #No se cumplieron las opciones anteriores, por lo tanto es un operador.
                pilaTemporal.append(elementoActual)

        #En caso de que se quede algun operador en pila se tiene que sacar.
        while( len(pilaTemporal) > 0):
            auxiliar = pilaTemporal.pop() #Obtengo el ultimo elemento de la pila
            salida.append(auxiliar) #Guardo el ultimo elemento de pila en salida
        self.crear_frase(salida)
    def crear_frase(self,operacion): #pvq ['p','q','v']
        pilaTemporal = []
        
        for posicion in operacion:
            if( posicion in self.tabla):
                #En caso de que sea operador se agrega a pilaTemporal
                pilaTemporal.append(posicion)
            else:
                #Sacamos los valores de la pila, empezando por el final
                val_b = pilaTemporal.pop()
                val_a = pilaTemporal.pop()
                #Verificamos el tipo de operacion y escribimos la operacion segun sea el caso.
                if(posicion == "^"):
                    pilaTemporal.append("("+val_a+" and "+val_b+")")
                elif(posicion == "->"):
                    pilaTemporal.append("(not "+val_a+" or "+val_b+")")
                elif(posicion == "v"):
                    pilaTemporal.append("("+val_a+" or "+val_b+")")
        #Generamos la frase final
        global frase
        frase = pilaTemporal

        self.resolver()

    def resolver(self):
        #Lista de salida.
        evaluaciones = []
        for item in frase:
            original = item
            #Repetimos cuantas condiciones se hayan generado
            for i in range(len(condiciones)):
                for operador in self.operadores:
                    #Reemplazamos el valor del operador con su valor actual en diccionario
                    item = item.replace(operador, str(self.tabla.get(operador)[i]))
                #Hacemos evaluacion y guardamos en la salida.
                evaluaciones.append(eval(item))
                #Reiniciamos la frase.
                item = original
        print(f"Resultados: {evaluaciones}")