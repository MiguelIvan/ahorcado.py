print('Juego del ahorcado')
print('-----------------')
print('Tematica del juego:')
print('1)Las letras faltantes estan enumeradas, ingrese el numero que quiere editar.')
print('2)Tiene 5 intentos para completar la palabra.')
print('3)A medida que acierte se le premiara con un intento extra.')
print('4)Si la letra es incorrecta se le restara intentos.')
print('\n')

contador=5
intentos=0
letra=''
l1='_'
l2='_'
l3='_'
l4='_'
l5='_'
print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
print(' ','1',' ','2',' ',' ','3','4',' ','5')

while (intentos<5):
    numero=int(input('Introduzca el numero de la opcion a editar: '))
    intentos = intentos + 1
    contador=contador-1
    if numero==1:
        letra=input('Introduzca letra(1): ')
        if letra=='a':
            l1='a'
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
        else:
            print('Incorrecto')
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
    elif numero==2:
        letra=input('Introduzca letra(2): ')
        if letra=='p':
            l2='p'
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
        else:
            print('Incorrecto')
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
    elif numero==3:
        letra=input('Introduzca letra(3): ')
        if letra=='e':
            l3='e'
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
        else:
            print('Incorrecto')
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
    elif numero==4:
        letra=input('Introduzca letra(4): ')
        if letra=='n':
            l4='n'
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
        else:
            print('Incorrecto')
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')

    elif numero==5:
        letra=input('Introduzca letra(5): ')
        if letra=='o':
            l5='o'
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
        else:
            print('Incorrecto')
            print('\n')
            print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
            print(' ','1',' ','2',' ',' ','3','4',' ','5')
            print('\n')
            print('Intentos:',intentos,',le quedan:',contador, 'intentos')
            print('\n')
    else:
        intentos=intentos-1
        contador=contador+1
        print('\n')
        print('No existe este valor en opciones, reintente ingresar valor existente')
        print('c',l1,'m',l2,'a','m',l3,l4,'t',l5)
        print(' ','1',' ','2',' ',' ','3','4',' ','5')
        print('\n')

if (l1=='a')and(l2=='p')and(l3=='e')and(l4=='n')and(l5=='o'):
    print('HAZ GANADO!:D')
else:
    print('HAZ PERDIDO! :(')
