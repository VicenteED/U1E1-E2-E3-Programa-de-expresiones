class punto1:
    #Se crea una lista con los operadores.
    operadores = list("^*/+-(")

    #Entrada de prueba: (6+2)*3/2^2-4
    #Salida esperada -> [(, 6, +, 2, ), *, 3, /, 2, ^, 2, -, 4]
    #reconocer un metodo de la misma clase (self)
    def separarEntrada(self):
        entrada = input("Ingresa la operacion\n")
        salida = []
        numerosTemporales = ""
        for e in entrada:
            if e.isdigit():
                numerosTemporales += e
            else:
                if(numerosTemporales != ""):
                    salida.append(numerosTemporales)
                salida.append(e)
                #Limpiamos los numeros.
                numerosTemporales = ""
        if(numerosTemporales != ""):
            salida.append(numerosTemporales)
            numerosTemporales = ""

        self.convertir(salida)

    #Regresa la prioridad del operador.
    def prioridades(self,elemento):
        #Parentesis no cuentan en prioridades, sirven para acomodar los operadores.
        if elemento == "(":
            return 0
        elif elemento == "^":
            return 4
        elif elemento == "*" or elemento =="/":
            return 3
        elif elemento == "+" or elemento == "-":
            return 2

    #pila de operadores
    pila = []
    #lista final de la notacion
    lista_salida = []

    def convertir(self,expresion):
        while len(expresion) > 0:
            #Tomamos el primer elemento actual de la expresion
            elemento = expresion.pop(0)
            #Si el elemento es un numero se agrega a la lista postorden
            if elemento.isdigit():
                self.lista_salida.append(elemento)
            #Un parentesis de apertura se agrega a la pila directamente
            elif elemento == "(":
                self.pila.append(elemento)
            #Se sacan todos los operadores hasta que la lista este vacia o encuentre
            #su par de apertura
            elif elemento == ")":
                while len(self.pila)>0 and self.pila[-1] != "(":
                    self.lista_salida.append(self.pila.pop())

                #Si encuentra un parentesis de apertura lo elimina, en caso contrario
                #los parentesis estan desequilibrados
                if self.pila[-1] == "(":
                    self.pila.pop()
                else:
                    print("Error parentesis no equilibrado")
            #Al encontrar un operador sacar todos los operadores que tengan una priodad
            #mayor en la pila de operadores
            elif elemento in self.operadores:
                # and pila[-1] != "("
                while( (len(self.pila) > 0) and (self.prioridades(self.pila[-1]) >= self.prioridades(elemento))):
                    self.lista_salida.append(self.pila.pop())
                #Agregamos a la pila el operador actual
                self.pila.append(elemento)
        #Sacamos de la pila los operadores sobrantes
        while len(self.pila) > 0:
            self.lista_salida.append(self.pila.pop())
        #Juntamos para impresion la lista de salida

        self.operacion(self.lista_salida)
    
    def operacion(self,convertida):
        pilaFinal = [] 
        for e in convertida:
            if e.isdigit():
             pilaFinal.append(e)
            else:
                b = pilaFinal.pop()
                a = pilaFinal.pop()
                if e == "+":
                    resultado = int(a) + int(b)
                    
                elif e == "-":
                    resultado = int(a) - int(b)
                    
                elif e == "*":
                    resultado = int(a) * int(b)
                elif e == "/":
                    resultado = int(a) / int(b)
                elif e == "^":
                    resultado = int(a) ** int(b)
                pilaFinal.append(resultado)
            
            print(pilaFinal)