import random  # Importa el módulo random para generar elecciones aleatorias de la computadora

# Define las opciones posibles en el juego
opciones = ('piedra', 'papel', 'tijera')

# Inicializa las variables para controlar las rondas y los puntajes
rondas = 1
computadoraGana = 0
usuarioGana = 0

# Muestra un mensaje de bienvenida al usuario
print("""
      [  🤖  Bienvenido al juego Piedra, Papel o Tijera 🙋 ]
                    >>> Ingresa una opción <<<
      """)

# Inicia el bucle del juego que se repetirá hasta que se completen 3 rondas
while rondas < 4:
    print('***' * 10)  # Imprime separadores decorativos para distinguir las rondas
    print('Round ', rondas)  # Muestra el número de la ronda actual
    print('***' * 10)

    # Muestra el puntaje actual antes de comenzar la ronda
    print(f'''
    Puntuacion
    Computadora: {computadoraGana}
    Usuario: {usuarioGana}
          ''')

    # Solicita al usuario que ingrese su elección y la convierte a minúsculas
    opcionUsuario = input('>>> Piedra, papel o tijera => ').lower()

    # Valida que la opción ingresada sea válida, en caso contrario solicita de nuevo la opción
    while not opcionUsuario in opciones:
        print('Esa opción no es valida')  # Muestra un mensaje de error si la opción no es válida
        opcionUsuario = input('>>> Piedra, papel o tijera => ').lower()

    # La computadora elige aleatoriamente una de las opciones usando el módulo random
    opcionComputadora = random.choice(opciones)

    # Muestra las elecciones de la computadora y del usuario
    print('El usuario elije => ', opcionUsuario)
    print('La computadora elije => ', opcionComputadora)

    # Compara las elecciones y determina el ganador de la ronda
    if opcionUsuario == opcionComputadora:
        print ("---" * 10)
        print('Empate!\n')  # Caso de empate
    elif opcionUsuario == 'piedra':
        if opcionComputadora == 'tijera':
            print('🪨 Piedra gana a tijera ✂️')
            print ("---" * 10)
            print('¡Usuario gana!\n')
            usuarioGana += 1  # Suma un punto al usuario si gana la ronda
        else:
            print('📄 Papel gana a piedra 🪨')
            print ("---" * 10)
            print('¡Computadora gana!\n')
            computadoraGana += 1  # Suma un punto a la computadora si gana la ronda
    elif opcionUsuario == 'papel':
        if opcionComputadora == 'piedra':
            print('📄 Papel gana a piedra 🪨')
            print ("---" * 10)
            print('¡Usuario gana!\n')
            usuarioGana += 1
        else: 
            print('✂️ Tijera gana a papel 📄')
            print ("---" * 10)
            print('¡Computadora gana!\n')
            computadoraGana += 1
    elif opcionUsuario == 'tijera':
        if opcionComputadora == 'papel':
            print('✂️ Tijera gana a papel 📄')
            print ("---" * 10)
            print('¡Usuario gana!\n ')
            usuarioGana += 1
        else: 
            print('🪨 Piedra gana a tijera ✂️')
            print ("---" * 10)
            print('¡Computer gana!\n ')
            computadoraGana += 1

    rondas += 1  # Incrementa el número de rondas después de cada ronda

# Después de completar las 3 rondas, determina quién es el ganador final
if usuarioGana > computadoraGana:
    print('🎖️ El ganador es Usuario 🎖️')
    print(f'Puntaje: {usuarioGana}')
else: 
    print('🎖️ El ganador es Computadora 🎖️')
    print(f'Puntaje: {computadoraGana}')