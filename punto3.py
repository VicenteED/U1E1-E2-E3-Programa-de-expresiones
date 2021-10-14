class punto3:
    def _init_(self) -> None:
        pass
    def separacion(self):
        entrada = input("Ingresa cualquier dato que se te ocurra: ").split()
        print(f'Los valores que se encuentran dentro de nuestra pila son {entrada} y esta es la cantidad {len(entrada)}')
        enteros = []
        char = []
        cadenas = []
        for e in entrada:
            if e.isdigit():
               enteros.append(e)
            else:
                if len(e)>1:
                   cadenas.append(e)
                else:
                    char.append(e)
        print(f'Los valores que se encuentran de tipo enteros son {enteros} y estos son el número de elementos almacenados {len(enteros)}')
        print(f'Los valores que se encuentran de tipo cadena son {cadenas} y estos son el número de elementos almacenados {len(cadenas)}')
        print(f'Los valores que se encuentran de tipo caracter {char} y estos son el número de elementos almacenados {len(char)}')