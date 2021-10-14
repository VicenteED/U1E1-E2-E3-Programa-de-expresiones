import punto1
import punto2
import punto3 


pt1 = punto1.punto1()
pt2 = punto2.punto2()
pt3 = punto3.punto3()

expresionAritmetica = 1
expresionLogica = 2
expresionLogicaV2 = 3
salir = 4


def menu():
    print(f'''            Menu
    {expresionAritmetica} Expresión aritmetica
    {expresionLogica} Expresión lógica
    {expresionLogicaV2} Expresión logica v2
    {salir} Salir
    ''')

    continuar = True

    while continuar:
        opc = int(input('Selecciona la opción: '))
        if opc == 1:
            pt1.separarEntrada()
        elif opc == 2:
            pt2.separa_entrada()
        elif opc == 3:
            pt3.separacion()
        elif opc == 4:
           continuar = False
           print("Nos vemos")
        else:
            print("No es una opción valida")

def main():
    menu()


if __name__ == '_main_':
    menu()